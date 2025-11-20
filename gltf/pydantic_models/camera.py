from __future__ import annotations

import math
import warnings
from typing import Optional, Literal

from pydantic import model_validator, Field

from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.validation_errors import GLTFSpecError, GLTFSpecWarning


class Camera(GLTFNamed):
    """
    A camera’s projection.

    A node MAY reference a camera to apply a transform to place the camera in the scene.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera
    """

    orthographic: Optional[Camera.Orthographic] = None
    """
    An orthographic camera containing properties to create an orthographic projection matrix.
    
    This property MUST NOT be defined when perspective is defined.
    """

    perspective: Optional[Camera.Perspective] = None
    """
    A perspective camera containing properties to create a perspective projection matrix.
    
    This property MUST NOT be defined when orthographic is defined.
    """

    type: Literal['perspective', 'orthographic']
    """
    Specifies if the camera uses a perspective or orthographic projection.
    
    Based on this, either the camera’s perspective or orthographic property MUST be defined.
    """

    @model_validator(mode='after')
    def _validate_projection_choice_gltf_spec(self):
        if self.type == 'perspective':
            if self.perspective is None or self.orthographic is not None:
                raise GLTFSpecError(
                    'GLTF Spec: For type="perspective", perspective MUST be defined and orthographic MUST NOT be defined.'
                    )
        elif self.type == 'orthographic':
            if self.orthographic is None or self.perspective is not None:
                raise GLTFSpecError(
                    'GLTF Spec: For type="orthographic", orthographic MUST be defined and perspective MUST NOT be defined.'
                    )
        return self

    class Orthographic(GLTFBase):
        """
        An orthographic camera containing properties to create an orthographic projection matrix.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera-orthographic
        """

        x_mag: float = Field(alias='xmag')
        """
        The floating-point horizontal magnification of the view.
        
        This value MUST NOT be equal to zero.
        
        This value SHOULD NOT be negative.
        """

        y_mag: float = Field(alias='ymag')
        """
        The floating-point vertical magnification of the view.
        
        This value MUST NOT be equal to zero.
        
        This value SHOULD NOT be negative.
        """

        z_far: float = Field(alias='zfar', gt=0)
        """
        The floating-point distance to the far clipping plane. 
        
        This value MUST NOT be equal to zero. 
        
        ``zfar`` MUST be greater than ``znear``.
        """

        z_near: float = Field(alias='znear', ge=0)
        """The floating-point distance to the near clipping plane."""

        @model_validator(mode='after')
        def _validate_ortho_ranges_gltf_spec(self):
            if self.z_far <= self.z_near:
                raise GLTFSpecError('GLTF Spec: For orthographic camera, zfar MUST be greater than znear.')
            if self.x_mag == 0 or self.y_mag == 0:
                raise GLTFSpecError('GLTF Spec: xmag and ymag MUST NOT be zero.')
            # SHOULD warnings
            if self.x_mag < 0:
                warnings.warn('GLTF Spec: camera.orthographic.xmag SHOULD NOT be negative.', GLTFSpecWarning)
            if self.y_mag < 0:
                warnings.warn('GLTF Spec: camera.orthographic.ymag SHOULD NOT be negative.', GLTFSpecWarning)
            return self

    class Perspective(GLTFBase):
        """
        A perspective camera containing properties to create a perspective projection matrix.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera-perspective
        """

        aspect_ratio: Optional[float] = Field(default=None, gt=0)
        """
        The floating-point aspect ratio of the field of view.
        
        When undefined, the aspect ratio of the rendering viewport MUST be used.
        """

        y_fov: float = Field(alias='yfov', gt=0)
        """
        The floating-point vertical field of view in radians.
        
        This value SHOULD be less than PI.
        """

        z_far: Optional[float] = Field(alias='zfar', default=None, gt=0)
        """
        The floating-point distance to the far clipping plane.
        
        When defined, ``zfar`` MUST be greater than ``znear``.
        
        If ``zfar`` is undefined, client implementations SHOULD use infinite projection matrix.
        """

        z_near: float = Field(alias='znear', gt=0)
        """The floating-point distance to the near clipping plane."""

        @model_validator(mode='after')
        def _validate_perspective_ranges_gltf_spec(self):
            if self.z_far is not None and not (self.z_far > self.z_near):
                raise GLTFSpecError('GLTF Spec: When defined, perspective zfar MUST be greater than znear.')
            if not (self.y_fov < math.pi):
                warnings.warn('GLTF Spec: camera.perspective.yfov SHOULD be less than π (3.14159…).', GLTFSpecWarning)
            return self

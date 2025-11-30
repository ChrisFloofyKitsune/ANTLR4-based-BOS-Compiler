"""Pydantic models for the glTF 2.0 scene graph and cameras.

Defines :class:`Node`, :class:`Scene`, and :class:`Camera` plus nested
projection helpers used to describe the hierarchical structure and
viewpoints in a glTF asset.
"""

from __future__ import annotations

import math
import warnings

from typing import Optional, Annotated, Literal

from pydantic import Field, model_validator

from util.index_ref import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.geometry import Skin, Mesh
from gltf.pydantic_models.validation_errors import GLTFSpecError, GLTFSpecWarning


class Node(GLTFNamed):
    """
    A node in the node hierarchy.

    When the node contains ``skin``, all ``mesh.primitives`` MUST contain JOINTS_0 and WEIGHTS_0 attributes.

    A node MAY have either a ``matrix`` or any combination of ``translation/rotation/scale`` (TRS) properties.

    TRS properties are converted to matrices and postmultiplied in the ``T * R * S`` order to compose the transformation matrix;
    first the scale is applied to the vertices, then the rotation, and then the translation.

    If none are provided, the transform is the identity.

    When a node is targeted for animation (referenced by an animation.channel.target),
    ``matrix`` MUST NOT be present.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-node
    """

    camera: Annotated[Optional[int], Field(ge=0, default=None), IndexRef[Camera]] = None
    """Index of the camera used by this node."""

    children: Optional[list[Annotated[int, Field(ge=0), IndexRef[Node]]]] = None
    """The indices of this node’s children."""

    skin: Annotated[Optional[int], IndexRef[Skin]] = None
    """
    The index of the skin referenced by this node.

    When a skin is referenced by a node within a scene, all joints
    used by the skin MUST belong to the same scene.

    When defined, ``mesh`` MUST also be defined.
    """

    matrix: list[float] = Field(
        default=[
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        ],
        min_length=16, max_length=16
    )
    """A floating-point 4x4 transformation matrix stored in column-major order."""

    mesh: Annotated[Optional[int], Field(ge=0, default=None), IndexRef[Mesh]]
    """The index of the mesh in this node."""

    rotation: list[float] = Field(
        default=[0.0, 0.0, 0.0, 1.0],
        min_length=4, max_length=4
    )
    """The node’s unit quaternion rotation in the order (x, y, z, w), where w is the scalar."""

    scale: list[float] = Field(
        default=[1.0, 1.0, 1.0],
        min_length=3, max_length=3
    )
    """The node’s non-uniform scale, given as the scaling factors along the x, y, and z axes."""

    translation: list[float] = Field(
        default=[0.0, 0.0, 0.0],
        min_length=3, max_length=3
    )
    """The node’s translation along the x, y, and z axes."""

    weights: Optional[list[float]] = None
    """
    The weights of the instantiated morph target.

    The number of array elements MUST match the number of morph targets of the referenced mesh.

    When defined, ``mesh`` MUST also be defined.
    """

    @model_validator(mode='after')
    def _validate_trs_vs_matrix_gltf_spec(self):
        # If matrix provided in the JSON, TRS MUST NOT be present per spec
        fields_set = getattr(self, 'model_fields_set', set())
        if 'matrix' in fields_set and ({'translation', 'rotation', 'scale'} & set(fields_set)):
            raise GLTFSpecError('GLTF Spec: Node MUST NOT define both matrix and any of translation/rotation/scale.')
        return self


class Scene(GLTFNamed):
    """
    A set of root nodes composing a scene.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-scene
    """

    nodes: Optional[list[Annotated[int, Field(ge=0), IndexRef[Node]]]] = None
    """The indices of each root node."""


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

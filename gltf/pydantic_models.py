"""
Pydantic v2 models for the glTF 2.0 core schema.

This module defines Pydantic models that map the glTF 2.0 JSON
structure to Python classes for loading and validating.

There are spec-enforcing validators (all end with `_gltf_spec`).
    - GLTFSpecError is raised for MUST-level violations.
    - GLTFSpecWarning is raised for SHOULD-level violations (using the built-in warnings module).

Additional properties are allowed for all Pydantic models (per the spec).

GLTFBase and GLTFNamed are base classes that are implied by the spec (and exist in their JSON Schema anyway).

(DDS textures have been added to the default supported image formats since projects I want to work on use it)

Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
"""

from __future__ import annotations

import math
import warnings
from enum import IntEnum
from typing import Optional, Literal, Annotated, ClassVar

from pydantic import BaseModel, JsonValue, Field, ConfigDict, field_validator, model_validator, ValidationInfo
from pydantic.alias_generators import to_camel


class GLTFSpecError(ValueError):
    """Raised when a MUST-level glTF spec violation occurs during validation."""


class GLTFSpecWarning(UserWarning):
    """Emitted for SHOULD-level or advisory glTF spec guidance."""


Extension = dict[str, JsonValue]
"""
JSON object with extension-specific objects.

Additional properties are allowed.

Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-extension
"""

Extras = JsonValue
"""
Application-specific data.

Although ``extras`` MAY have any type, it SHOULD be a JSON object rather than a primitive value for best portability.

Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-extras
"""


class GLenum(IntEnum):
    """
    Enum of OpenGL constants (magic values)

    see: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants
    """

    POINTS = 0x0
    LINES = 0x1
    LINE_LOOP = 0x2
    LINE_STRIP = 0x3
    TRIANGLES = 0x4
    TRIANGLE_STRIP = 0x5
    TRIANGLE_FAN = 0x6

    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406

    NEAREST = 0x2600
    LINEAR = 0x2601

    NEAREST_MIPMAP_NEAREST = 0x2700
    LINEAR_MIPMAP_NEAREST = 0x2701
    NEAREST_MIPMAP_LINEAR = 0x2702
    LINEAR_MIPMAP_LINEAR = 0x2703

    REPEAT = 0x2901
    CLAMP_TO_EDGE = 0x812F
    MIRRORED_REPEAT = 0x8370

    ARRAY_BUFFER = 0x8892
    ELEMENT_ARRAY_BUFFER = 0x8893


class GLTFBase(BaseModel):
    """
    Common base for all glTF schema models.

    Provides consistent Pydantic configuration (aliasing, extra handling) and shared
    extension/extra fields that every top-level object in the glTF 2.0 spec may carry.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
        extra='allow',
    )

    extensions: Optional[Extension] = None
    """JSON object with extension-specific objects."""

    extras: Optional[Extras] = None
    """Application-specific data."""

    @field_validator('extras')
    @classmethod
    def _warn_extras_should_be_object_gltf_spec(cls, v):
        # Spec says extras SHOULD be a JSON object for portability
        if v is not None and not isinstance(v, dict):
            warnings.warn('GLTF Spec: extras SHOULD be a JSON object for best portability.', GLTFSpecWarning)
        return v


class GLTFNamed(GLTFBase):
    """
    Base class for glTF objects that can be user-named.

    Many glTF entities allow an optional, non-unique "name" field for debugging and tooling.
    Names are not identifiers and do not imply uniqueness across or within arrays.
    """

    name: Optional[str] = None
    """
    The user-defined name of this object.
    
    This is not necessarily unique, e.g., an accessor and a buffer
    could have the same name, or two accessors could even have the same name.
    """


class Accessor(GLTFNamed):
    """
    A typed view into a buffer view that contains raw binary data.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor
    """

    buffer_view: Optional[int] = Field(ge=0, default=None)
    """
    The index of the buffer view. 
    
    When undefined, the accessor MUST be initialized with zeros; 
    ``sparse`` property or extensions MAY override zeros with actual values.
    """

    byte_offset: int = Field(default=0, ge=0)
    """
    The offset relative to the start of the buffer view in bytes.
    
    This MUST be a multiple of the size of the component datatype.
    
    This property MUST NOT be defined when ``bufferView`` is undefined.
    """

    component_type: Literal[
        GLenum.BYTE,
        GLenum.UNSIGNED_BYTE,
        GLenum.SHORT,
        GLenum.UNSIGNED_SHORT,
        GLenum.UNSIGNED_INT,
        GLenum.FLOAT
    ]
    """
    The datatype of the accessor’s components.
    
    UNSIGNED_INT type MUST NOT be used for any accessor
    that is not referenced by ``mesh.primitive.indices``.
    """

    normalized: bool = False
    """
    Specifies whether integer data values are normalized before usage.
    
    Specifies whether integer data values are normalized (``true``)
    to [0, 1] (for unsigned types) or
    to [-1, 1] (for signed types) when they are accessed.
    
    This property MUST NOT be set to ``true`` for accessors with
    ``FLOAT`` or ``UNSIGNED_INT`` component type.
    """

    count: int = Field(ge=1)
    """
    The number of elements referenced by this accessor,
    not to be confused with the number of bytes or number of components.
    """

    type: Literal[
        'SCALAR',
        'VEC2',
        'VEC3',
        'VEC4',
        'MAT2',
        'MAT3',
        'MAT4'
    ]
    """Specifies if the accessor’s elements are scalars, vectors, or matrices."""

    max: Optional[list[float]] = Field(default=None, min_length=1, max_length=16)
    """
    Maximum value of each component in this accessor.
    
    Array elements MUST be treated as having the same data type as accessor’s ``componentType``.
    
    Both ``min`` and ``max`` arrays have the same length.
    The length is determined by the value of the ``type`` property;
    it can be 1, 2, 3, 4, 9, or 16.

    ``normalized`` property has no effect on array values: they always correspond
    to the actual values stored in the buffer.
    
    When the accessor is sparse, this property MUST contain maximum values
    of accessor data with sparse substitution applied.
    """

    min: Optional[list[float]] = Field(default=None, min_length=1, max_length=16)
    """
    Minimum value of each component in this accessor.
    
    Array elements MUST be treated as having the same data type as accessor’s ``componentType``.
    
    Both ``min`` and ``max`` arrays have the same length.
    The length is determined by the value of the ``type`` property;
    it can be 1, 2, 3, 4, 9, or 16.

    ``normalized`` property has no effect on array values: they always correspond
    to the actual values stored in the buffer.
    
    When the accessor is sparse, this property MUST contain minimum values
    of accessor data with sparse substitution applied.
    """

    sparse: Optional['Accessor.Sparse'] = None
    """Sparse storage of elements that deviate from their initialization value."""

    # --- Spec helpers & validators ---
    _COMPONENT_TYPE_SIZE: ClassVar[dict[GLenum, int]] = {
        GLenum.BYTE: 1,
        GLenum.UNSIGNED_BYTE: 1,
        GLenum.SHORT: 2,
        GLenum.UNSIGNED_SHORT: 2,
        GLenum.UNSIGNED_INT: 4,
        GLenum.FLOAT: 4,
    }

    _TYPE_COMPONENTS: ClassVar[dict[str, int]] = {
        'SCALAR': 1,
        'VEC2': 2,
        'VEC3': 3,
        'VEC4': 4,
        'MAT2': 4,
        'MAT3': 9,
        'MAT4': 16,
    }

    @field_validator('byte_offset')
    @classmethod
    def _validate_byte_offset_alignment_gltf_spec(cls, v: int, info: ValidationInfo):
        component_type = info.data.get('component_type')
        if component_type is None:
            return v
        size = cls._COMPONENT_TYPE_SIZE.get(component_type)
        if size and v % size != 0:
            raise GLTFSpecError(
                f'GLTF Spec: byteOffset ({v}) must be a multiple of componentType byte length ({size}).'
                )
        return v

    @field_validator('normalized')
    @classmethod
    def _validate_normalized_with_type_gltf_spec(cls, v: bool, info: ValidationInfo):
        component_type = info.data.get('component_type')
        if v and component_type in (GLenum.FLOAT, GLenum.UNSIGNED_INT):
            raise GLTFSpecError('GLTF Spec: normalized MUST NOT be true for FLOAT or UNSIGNED_INT component types.')
        return v

    @field_validator('max')
    @classmethod
    def _validate_max_len_gltf_spec(cls, v: Optional[list[float]], info: ValidationInfo):
        if v is None:
            return v
        type_ = info.data.get('type')
        if type_ is None:
            return v
        expected = cls._TYPE_COMPONENTS.get(type_)
        if expected and len(v) != expected:
            raise GLTFSpecError(
                f'GLTF Spec: max array length must match component count for type {type_} (expected {expected}).'
                )
        return v

    @field_validator('min')
    @classmethod
    def _validate_min_len_gltf_spec(cls, v: Optional[list[float]], info: ValidationInfo):
        if v is None:
            return v
        type_ = info.data.get('type')
        if type_ is None:
            return v
        expected = cls._TYPE_COMPONENTS.get(type_)
        if expected and len(v) != expected:
            raise GLTFSpecError(
                f'GLTF Spec: min array length must match component count for type {type_} (expected {expected}).'
                )
        return v

    @model_validator(mode='after')
    def _validate_no_offset_without_bufferview_gltf_spec(self):
        # If bufferView is not defined, byteOffset must be 0 per spec
        if self.buffer_view is None and self.byte_offset not in (0, None):
            raise GLTFSpecError(
                'GLTF Spec: accessor.byteOffset MUST NOT be defined when bufferView is undefined (must be 0).'
                )
        return self

    class Sparse(GLTFBase):
        """
        Sparse storage of accessor values that deviate from their initialization value.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor-sparse
        """

        count: int = Field(ge=1)
        """Number of deviating accessor values stored in the sparse array."""

        indices: 'Accessor.Sparse.Indices'
        """
        An object pointing to a buffer view containing the indices of deviating accessor values.
        
        The number of indices is equal to ``count``.
        
        Indices MUST strictly increase.
        """

        values: 'Accessor.Sparse.Values'
        """An object pointing to a buffer view containing the deviating accessor values."""

        class Indices(GLTFBase):
            """
            Object specifying the bufferView Index containing the indices of deviating accessor values.

            The number of indices is equal to ``accessor.sparse.count``.

            Indices MUST strictly increase.

            Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor-sparse-indices
            """

            buffer_view: int = Field(ge=0)
            """
            The index of the buffer view with sparse indices.
            
            The referenced buffer view MUST NOT have its ``target`` or ``byteStride`` properties defined.
            The buffer view and the optional ``byteOffset`` MUST be aligned to the ``componentType`` byte length.
            """

            byte_offset: int = Field(default=0, ge=0)
            """The offset relative to the start of the buffer view in bytes."""

            component_type: Literal[
                GLenum.UNSIGNED_BYTE,
                GLenum.UNSIGNED_SHORT,
                GLenum.UNSIGNED_INT
            ]
            """The indices data type."""

        class Values(GLTFBase):
            """
            Object specifying the bufferView Index containing the deviating accessor values.

            The number of elements is equal to ``accessor.sparse.count`` times number of components.
            The elements have the same component type as the base accessor.
            The elements are tightly packed.
            Data MUST be aligned following the same rules as the base accessor.

            Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor-sparse-values
            """

            buffer_view: int = Field(ge=0)
            """
            The index of the bufferView with sparse values.
            
            The referenced buffer view MUST NOT have its ``target`` or ``byteStride`` properties defined.
            """

            byte_offset: int = Field(default=0, ge=0)
            """The offset relative to the start of the bufferView in bytes."""


class Animation(GLTFNamed):
    """
    A keyframe animation.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation
    """

    channels: list['Animation.Channel'] = Field(min_length=1)
    """
    An array of animation channels.
    
    An animation channel combines an animation sampler with a target property being animated.

    Different channels of the same animation MUST NOT have the same targets.
    """

    samplers: list['Animation.Sampler'] = Field(min_length=1)
    """
    An array of animation samplers.
    
    An animation sampler combines timestamps with a sequence of output values
    and defines an interpolation algorithm.
    """

    class Channel(GLTFBase):
        """
        An animation channel combines an animation sampler with a target property being animated.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-channel
        """

        sampler: int = Field(ge=0)
        """
        The index of a sampler in this animation used to compute the value
        for the target, e.g., a node’s translation, rotation, or scale (TRS).
        """

        target: 'Animation.Channel.Target'
        """The descriptor of the animated property."""

        class Target(GLTFBase):
            """
            The descriptor of the animated property.

            Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-channel-target
            """

            node: Optional[int] = Field(default=None, ge=0)
            """
            The index of the node to animate.
            
            When undefined, the animated object MAY be defined by an extension.
            """

            path: Literal[
                'translation',
                'rotation',
                'scale',
                'weights'
            ]
            """
            The name of the node’s TRS property to animate, or the "weights" of
            the Morph Targets it instantiates. For the "translation" property,
            the values that are provided by the sampler are the translation
            along the X, Y, and Z axes.
            
            For the "rotation" property, the values are a quaternion in the
            order (x, y, z, w), where w is the scalar.
            
            For the "scale" property, the values are the scaling factors
            along the X, Y, and Z axes.
            """

    class Sampler(GLTFBase):
        """
        An animation sampler combines timestamps with a sequence of output
        values and defines an interpolation algorithm.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-sampler
        """

        input: int = Field(ge=0)
        """The index of an accessor containing keyframe timestamps."""

        interpolation: Literal['LINEAR', 'STEP', 'CUBICSPLINE'] = 'LINEAR'
        """
        Interpolation algorithm.
        
        ``"LINEAR"``
        
        The animated values are linearly interpolated between keyframes.
        When targeting a rotation, spherical linear interpolation (slerp) SHOULD be used to interpolate quaternions.
        The number of output elements MUST equal the number of input elements.
        
        ``"STEP"``
        
        The animated values remain constant to the output of the first keyframe, until the next keyframe.
        The number of output elements MUST equal the number of input elements.
        
        ``"CUBICSPLINE"``
        
        The animation’s interpolation is computed using a cubic spline with specified tangents.
        The number of output elements MUST equal three times the number of input elements.
        For each input element, the output stores three elements, an in-tangent, a spline vertex, and an out-tangent.
        There MUST be at least two keyframes when using this interpolation.
        """

        output: int = Field(ge=0)
        """The index of an accessor, containing keyframe output values."""


class Asset(GLTFBase):
    """
    Metadata about the glTF asset.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-asset
    """

    copyright: Optional[str] = None
    """A copyright message suitable for display to credit the content creator."""

    generator: Optional[str] = None
    """Tool that generated this glTF model. Useful for debugging."""

    version: str = Field(pattern='^[0-9]+\.[0-9]+$')
    """The glTF version in the form of ``<major>.<minor>`` that this asset targets."""

    min_version: Optional[str] = Field(default=None, pattern='^[0-9]+\.[0-9]+$')
    """
    The minimum glTF version in the form of ``<major>.<minor>`` that this asset targets. 
    
    This property MUST NOT be greater than the asset version.
    """

    @model_validator(mode='after')
    def _validate_versions_gltf_spec(self):
        # Ensure minVersion <= version when both defined
        if self.min_version is None:
            return self
        try:
            mv_major, mv_minor = (int(x) for x in self.min_version.split('.', 1))
            v_major, v_minor = (int(x) for x in self.version.split('.', 1))
        except Exception:
            return self
        if (mv_major, mv_minor) > (v_major, v_minor):
            raise GLTFSpecError('GLTF Spec: asset.minVersion MUST NOT be greater than asset.version.')
        return self


class Buffer(GLTFNamed):
    """
    A buffer points to binary geometry, animation, or skins.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-buffer
    """

    uri: Optional[str] = None
    """
    The URI (or IRI) of the buffer.
    
    Relative paths are relative to the current glTF asset.
    
    Instead of referencing an external file, this field MAY contain a data:-URI.
    """

    byte_length: int = Field(ge=1)
    """The length of the buffer in bytes."""


class BufferView(GLTFNamed):
    """
    A view into a buffer generally representing a subset of the buffer.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-bufferview
    """

    buffer: int = Field(ge=0)
    """The index of the buffer."""

    byte_offset: int = Field(default=0, ge=0)
    """The offset into the buffer in bytes."""

    byte_length: int = Field(ge=1)
    """The length of the bufferView in bytes."""

    byte_stride: Optional[int] = Field(default=None, ge=4, le=252)
    """
    The stride, in bytes, between vertex attributes.
    
    When this is not defined, data is tightly packed.
    
    When two or more accessors use the same buffer view, this field MUST be defined.
    """

    target: Optional[Literal[
        GLenum.ARRAY_BUFFER,
        GLenum.ELEMENT_ARRAY_BUFFER
    ]] = None
    """The hint representing the intended GPU buffer type to use with this buffer view."""

    @field_validator('byte_stride')
    @classmethod
    def _validate_byte_stride_gltf_spec(cls, v: Optional[int]):
        if v is None:
            return v
        if v % 4 != 0:
            raise GLTFSpecError('GLTF Spec: byteStride MUST be a multiple of 4.')
        return v


class Camera(GLTFNamed):
    """
    A camera’s projection.

    A node MAY reference a camera to apply a transform to place the camera in the scene.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera
    """

    orthographic: Optional['Camera.Orthographic'] = None
    """
    An orthographic camera containing properties to create an orthographic projection matrix.
    
    This property MUST NOT be defined when perspective is defined.
    """

    perspective: Optional['Camera.Perspective'] = None
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
        def _validate_persp_ranges_gltf_spec(self):
            if self.z_far is not None and not (self.z_far > self.z_near):
                raise GLTFSpecError('GLTF Spec: When defined, perspective zfar MUST be greater than znear.')
            if not (self.y_fov < math.pi):
                warnings.warn('GLTF Spec: camera.perspective.yfov SHOULD be less than π (3.14159…).', GLTFSpecWarning)
            return self


class GLTFRoot(GLTFBase):
    """
    Top-level glTF container listing all resources and the default scene.

    Cross-references in a glTF file are index-based. Most relationships are expressed as
    0-based integer indices into arrays on this root object (or into arrays on
    a containing object), rather than by IDs or pointers.

    Common examples:
        - ``scene`` is an index into ``scenes`` (the default scene)
        - ``Scene.nodes`` are indices into ``nodes`` (root nodes for the scene)
        - ``Node.children`` are indices into ``nodes`` (forming the node DAG)
        - ``Node.mesh`` is an index into ``meshes``
        - ``Mesh.Primitive.material`` is an index into ``materials``
        - ``Texture.sampler`` and ``Texture.source`` are indices into ``samplers`` and ``images``
        - ``Image.bufferView`` and ``Accessor.bufferView`` are indices into ``bufferViews``; those in turn reference ``buffers``
        - ``Skin.joints`` are indices into ``nodes``
        - ``Animation.channels[*].sampler`` is an index into the animation’s own ``samplers`` array (local to that animation)

    Indices MUST be within bounds of the corresponding array, and omitted (``null`` / ``None``)
    where optional.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-gltf
    """

    asset: Asset
    """Metadata about the glTF asset."""

    extensions_used: Optional[list[str]] = None
    """Names of glTF extensions used in this asset."""

    extensions_required: Optional[list[str]] = None
    """Names of glTF extensions required to properly load this asset."""

    accessors: Optional[list[Accessor]] = None
    """An array of accessors. An accessor is a typed view into a bufferView."""

    animations: Optional[list[Animation]] = None
    """An array of keyframe animations."""

    buffers: Optional[list[Buffer]] = None
    """An array of buffers. A buffer points to binary geometry, animation, or skins."""

    buffer_views: Optional[list[BufferView]] = None
    """An array of bufferViews. A bufferView is a view into a buffer generally representing a subset of the buffer."""

    cameras: Optional[list[Camera]] = None
    """An array of cameras. A camera defines a projection matrix."""

    images: Optional[list['Image']] = None
    """An array of images. Image data is used to create a texture."""

    materials: Optional[list['Material']] = None
    """An array of materials. A material defines the appearance of a primitive."""

    meshes: Optional[list['Mesh']] = None
    """An array of meshes. A mesh is a set of primitives to be rendered."""

    nodes: Optional[list['Node']] = None
    """An array of nodes."""

    samplers: Optional[list['Sampler']] = None
    """An array of samplers. A sampler contains properties for texture filtering and wrapping modes."""

    scene: Optional[int] = None
    """The index of the default scene. This property MUST NOT be defined, when scenes is undefined."""

    scenes: Optional[list['Scene']] = None
    """An array of scenes."""

    textures: Optional[list['Texture']] = None
    """An array of textures."""

    skins: Optional[list['Skin']] = None
    """An array of skins. A skin is defined by joints and matrices."""

    @model_validator(mode='after')
    def _validate_root_constraints_gltf_spec(self):
        # scene index validity and presence rules
        if self.scene is not None:
            if self.scenes is None:
                raise GLTFSpecError('GLTF Spec: scene MUST NOT be defined when scenes is undefined.')
            if not (0 <= self.scene < len(self.scenes)):
                raise GLTFSpecError('GLTF Spec: scene index out of range for scenes array.')
        # extensionsRequired subset of extensionsUsed
        if self.extensions_required:
            used = set(self.extensions_used or [])
            missing = [ext for ext in self.extensions_required if ext not in used]
            if missing:
                raise GLTFSpecError(
                    f'GLTF Spec: extensionsRequired MUST be a subset of extensionsUsed. Missing in used: {missing}'
                    )
        return self


class Image(GLTFNamed):
    """
    Image data used to create a texture.

    Image MAY be referenced by an URI (or IRI) or a buffer view index.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-image
    """

    uri: Optional[str] = None
    """
    The URI (or IRI) of the image.
    
    Relative paths are relative to the current glTF asset.
    
    Instead of referencing an external file, this field MAY contain a data:-URI.
    
    This field MUST NOT be defined when bufferView is defined.
    """

    mime_type: Optional[str] = None
    """
    The image’s media type.
    
    This field MUST be defined when bufferView is defined.
    """

    buffer_view: Optional[int] = Field(default=None, ge=0)
    """
    The index of the bufferView that contains the image.
    
    This field MUST NOT be defined when uri is defined.
    """

    @field_validator('mime_type')
    @classmethod
    def _validate_mime_type_gltf_spec(cls, v: Optional[str]):
        if v is None:
            return v
        # Core glTF 2.0 supports JPEG/PNG. Some workflows use DDS via MSFT_texture_dds.
        allowed = {'image/jpeg', 'image/png', 'image/vnd.ms-dds', 'image/dds'}
        if v not in allowed:
            raise GLTFSpecError(
                'GLTF Spec: mimeType MUST be one of image/jpeg, image/png, image/vnd.ms-dds, or image/dds.'
                )
        return v

    @model_validator(mode='after')
    def _validate_source_gltf_spec(self):
        if self.buffer_view is not None:
            if self.uri is not None:
                raise GLTFSpecError('GLTF Spec: If bufferView is defined, uri MUST NOT be defined.')
            if self.mime_type is None:
                raise GLTFSpecError('GLTF Spec: If bufferView is defined, mimeType MUST be defined.')
        return self


class Material(GLTFNamed):
    """
    Material describing the appearance of a primitive (PBR metallic-roughness core).

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material
    """

    pbr_metallic_roughness: Optional['Material.PbrMetallicRoughness'] = None
    """
    A set of parameter values that are used to define the metallic-roughness
    material model from Physically Based Rendering (PBR) methodology.
    
    When undefined, all the default values of pbrMetallicRoughness MUST apply.
    """

    normal_texture: Optional['Material.NormalTextureInfo'] = None
    """
    The tangent space normal texture.
    
    The texture encodes RGB components with linear transfer function.
    
    Each texel represents the XYZ components of a normal vector in tangent space.
    
    The normal vectors use the convention +X is right and +Y is up. +Z points toward the viewer.
    
    If a fourth component (A) is present, it MUST be ignored.
    
    When undefined, the material does not have a tangent space normal texture.
    """

    occlusion_texture: Optional['Material.OcclusionTextureInfo'] = None
    """
    The occlusion texture.
    
    The occlusion values are linearly sampled from the R channel.
    
    Higher values indicate areas that receive full indirect lighting and lower values indicate no indirect lighting.
    
    If other channels are present (GBA), they MUST be ignored for occlusion calculations.

    When undefined, the material does not have an occlusion texture.
    """

    emissive_texture: Optional['TextureInfo'] = None
    """
    The emissive texture.
    
    It controls the color and intensity of the light being emitted by the material.
    
    This texture contains RGB components encoded with the sRGB transfer function.
    
    If a fourth component (A) is present, it MUST be ignored.
    
    When undefined, the texture MUST be sampled as having 1.0 in RGB components.
    """

    emissive_factor: list[float] = Field(default=[0.0, 0.0, 0.0], min_length=3, max_length=3)
    """
    The factors for the emissive color of the material.
    
    This value defines linear multipliers for the sampled texels of the emissive texture.
    """

    alpha_mode: Literal['OPAQUE', 'MASK', 'BLEND'] = 'OPAQUE'
    """
    The material’s alpha rendering mode enumeration specifying the interpretation
    of the alpha value of the base color.
    
    ``"OPAQUE"``
    
    The alpha value is ignored, and the rendered output is fully opaque.

    ``"MASK"``
    
    The rendered output is either fully opaque or fully transparent depending
    on the alpha value and the specified alphaCutoff value; the exact appearance
    of the edges MAY be subject to implementation-specific techniques such as “Alpha-to-Coverage”.

    ``"BLEND"`` 
    
    The alpha value is used to composite the source and destination areas.
    The rendered output is combined with the background using the
    normal painting operation (i.e. the Porter and Duff over operator).
    """

    alpha_cutoff: float = 0.5
    """
    Specifies the cutoff threshold when in MASK alpha mode.
    
    If the alpha value is greater than or equal to this value then it is
    rendered as fully opaque, otherwise, it is rendered as fully transparent.
    
    A value greater than 1.0 will render the entire material as fully transparent.
    
    This value MUST be ignored for other alpha modes. When alphaMode is not defined,
    this value MUST NOT be defined.
    """

    double_sided: bool = False
    """
    Specifies whether the material is double sided.
    
    When this value is false, back-face culling is enabled.
    
    When this value is true, back-face culling is disabled and double-sided lighting is enabled.
    
    The back-face MUST have its normals reversed before the lighting equation is evaluated.
    """

    class NormalTextureInfo(GLTFBase):
        """
        Texture Index and parameters for normal mapping.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material-normaltextureinfo
        """

        index: int = Field(ge=0)
        """The index of the texture."""

        tex_coord: int = Field(default=0, ge=0)
        """
        This integer value is used to construct a string in the format
        TEXCOORD_<set index> which is a reference to a key in mesh.primitives.attributes
        (e.g. a value of 0 corresponds to TEXCOORD_0).
        
        A mesh primitive MUST have the corresponding texture coordinate attributes
        for the material to be applicable to it.
        """

        scale: float = 1.0
        """
        The scalar parameter applied to each normal vector of the texture.
        
        This value scales the normal vector in X and Y directions using the formula::
        
            scaledNormal = normalize<sampled normal texture value> * 2.0 - 1.0) * vec3(<normal scale>, <normal scale>, 1.0)
        
        """

    class OcclusionTextureInfo(GLTFBase):
        """
        Texture Index and parameters for occlusion mapping.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material-occlusiontextureinfo
        """

        index: int = Field(ge=0)
        """The index of the texture."""

        tex_coord: int = Field(default=0, ge=0)
        """
        This integer value is used to construct a string in the format
        TEXCOORD_<set index> which is a reference to a key in mesh.primitives.attributes
        (e.g. a value of 0 corresponds to TEXCOORD_0).

        A mesh primitive MUST have the corresponding texture coordinate attributes
        for the material to be applicable to it.
        """

        strength: float = 1.0
        """
        A scalar parameter controlling the amount of occlusion applied.
        
        A value of 0.0 means no occlusion. A value of 1.0 means full occlusion.
        
        This value affects the final occlusion value as: ::
        
            1.0 + strength * (<sampled occlusion texture value> - 1.0).
        
        """

    class PbrMetallicRoughness(GLTFBase):
        """
        A set of parameter values that are used to define the metallic-roughness material model from Physically-Based Rendering (PBR) methodology.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material-pbrmetallicroughness
        """

        base_color_factor: list[float] = Field(
            default=[1.0, 1.0, 1.0, 1.0],
            min_length=4, max_length=4,
        )
        """
        The factors for the base color of the material.
        
        This value defines linear multipliers for the sampled texels of the base color texture.
        """

        base_color_texture: Optional['TextureInfo'] = None
        """
        The base color texture.
        
        The first three components (RGB) MUST be encoded with the sRGB transfer function.
        They specify the base color of the material.
        
        If the fourth component (A) is present, it represents the linear alpha coverage of the material.
        Otherwise, the alpha coverage is equal to 1.0.
        
        The material.alphaMode property specifies how alpha is interpreted.
        
        The stored texels MUST NOT be premultiplied.
        
        When undefined, the texture MUST be sampled as having 1.0 in all components.
        """

        metallic_factor: float = Field(default=1.0, ge=0.0, le=1.0)
        """
        The factor for the metalness of the material.
        
        This value defines a linear multiplier for the sampled metalness values of the metallic-roughness texture.
        """

        roughness_factor: float = Field(default=1.0, ge=0.0, le=1.0)
        """
        The factor for the roughness of the material.
        
        This value defines a linear multiplier for the sampled roughness values of the metallic-roughness texture.
        """

        metallic_roughness_texture: Optional['TextureInfo'] = None
        """
        The metallic-roughness texture.
        
        The metalness values are sampled from the B channel.
        
        The roughness values are sampled from the G channel.
        
        These values MUST be encoded with a linear transfer function.
        
        If other channels are present (R or A), they MUST be ignored for
        metallic-roughness calculations.
        
        When undefined, the texture MUST be sampled as having 1.0 in G and B components.
        """


class Mesh(GLTFNamed):
    """
    A set of primitives to be rendered.

    Its global transform is defined by a node that references it.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-mesh
    """

    primitives: list['Mesh.Primitive']
    """An array of primitives, each defining geometry to be rendered."""

    weights: Optional[list[float]] = None
    """
    Array of weights to be applied to the morph targets.
    
    The number of array elements MUST match the number of morph targets.
    """

    class Primitive(GLTFBase):
        """
        Geometry to be rendered with the given material.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-mesh-primitive
        """

        attributes: dict[str, Annotated[int, Field(ge=0)]]
        """
        A plain JSON object, where each key corresponds to a mesh attribute semantic
        and each value is the index of the accessor containing attribute’s data.
        """

        indices: Optional[int] = Field(ge=0, default=None)
        """
        The index of the accessor that contains the vertex indices.
        
        When this is undefined, the primitive defines non-indexed geometry.
        
        When defined, the accessor MUST have SCALAR type and an unsigned integer component type.
        """

        material: Optional[int] = Field(ge=0, default=None)
        """The index of the material to apply to this primitive when rendering."""

        mode: Literal[
            GLenum.POINTS,
            GLenum.LINES,
            GLenum.LINE_LOOP,
            GLenum.LINE_STRIP,
            GLenum.TRIANGLES,
            GLenum.TRIANGLE_STRIP,
            GLenum.TRIANGLE_FAN,
        ] = GLenum.TRIANGLES
        """The topology type of primitives to render."""

        targets: Optional[list[dict[str, Annotated[int, Field(ge=0)]]]] = None
        """
        An array of morph targets, each Morph Target is a dictionary mapping attribute semantic
        (e.g., POSITION, NORMAL, TANGENT) to the index of the accessor containing target attribute data.
        
        Each target MUST have the same set of attributes.
        """


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

    camera: Optional[int] = Field(ge=0, default=None)
    """Index of the camera used by this node."""

    children: Optional[list[Annotated[int, Field(ge=0)]]] = None
    """The indices of this node’s children."""

    skin: Optional[int] = None
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

    mesh: Optional[int] = Field(ge=0, default=None)
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


class Sampler(GLTFNamed):
    """
    Texture sampling parameters.

    Describes magnification/minification filters and wrap modes for the S/T axes.
    Textures may reference a sampler to control how texels are sampled when rendered.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-sampler
    """

    mag_filter: Optional[Literal[
        GLenum.NEAREST,
        GLenum.LINEAR
    ]] = None
    """Magnification filter."""

    min_filter: Optional[Literal[
        GLenum.NEAREST,
        GLenum.LINEAR,
        GLenum.NEAREST_MIPMAP_NEAREST,
        GLenum.NEAREST_MIPMAP_LINEAR,
        GLenum.LINEAR_MIPMAP_NEAREST,
        GLenum.LINEAR_MIPMAP_LINEAR
    ]] = None
    """Minification filter."""

    wrap_s: Literal[
        GLenum.CLAMP_TO_EDGE,
        GLenum.MIRRORED_REPEAT,
        GLenum.REPEAT
    ] = GLenum.REPEAT

    wrap_t: Literal[
        GLenum.CLAMP_TO_EDGE,
        GLenum.MIRRORED_REPEAT,
        GLenum.REPEAT
    ] = GLenum.REPEAT


class Scene(GLTFNamed):
    """
    A set of root nodes composing a scene.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-scene
    """

    nodes: Optional[list[Annotated[int, Field(ge=0)]]] = None
    """The indices of each root node."""


class Skin(GLTFNamed):
    """
    A skin defined by joints and inverse bind matrices.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-skin
    """

    inverse_bind_matrices: Optional[int] = Field(default=None, ge=0)
    """
    The index of the accessor containing the floating-point 4x4 inverse-bind matrices.
    Its ``count`` property MUST be greater than or equal to the number of joints.
    The ``joints`` PRIMITIVE_ARRAY property then defines how the matrix and joint lists are matched.
    """

    skeleton: Optional[int] = Field(default=None, ge=0)
    """The index of the node used as a skeleton root. When undefined, joints transforms resolve to scene root."""

    joints: list[Annotated[int, Field(ge=0)]] = Field(min_length=1)
    """Indices of skeleton nodes, used as joints in this skin.  Must be non-empty."""


class Texture(GLTFNamed):
    """
    A texture that references an image and an optional sampler.

    Combines a source image with sampling parameters (via Sampler).

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-texture
    """

    sampler: Optional[int] = Field(default=None, ge=0)
    """The index of the sampler used by this texture."""

    source: Optional[int] = Field(default=None, ge=0)
    """The index of the image used by this texture."""


class TextureInfo(GLTFBase):
    """
    Texture Index with a texture coordinate set selector.

    Provides the index of a texture and the texCoord set (TEXCOORD_n) that
    a primitive must provide for proper mapping.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-textureinfo
    """

    index: int = Field(ge=0)
    """The index of the texture."""

    tex_coord: int = Field(default=0, ge=0)
    """
    This integer value is used to construct a string in the format TEXCOORD_<set index>
    which is a reference to a key in mesh.primitives.attributes (e.g. a value of 0 corresponds to TEXCOORD_0).
    
    A mesh primitive MUST have the corresponding texture coordinate attributes for the material to be applicable to it.
    """

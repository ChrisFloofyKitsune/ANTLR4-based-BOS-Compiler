from __future__ import annotations

from typing import Optional, Literal, ClassVar, Annotated

from pydantic import Field, field_validator, model_validator
from pydantic_core.core_schema import ValidationInfo

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.gl_constant import GLConstant
from gltf.pydantic_models.validation_errors import GLTFSpecError


class Accessor(GLTFNamed):
    """
    A typed view into a buffer view that contains raw binary data.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor
    """

    buffer_view: Annotated[Optional[int], Field(ge=0, default=None), IndexRef('BufferView')]
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
        GLConstant.BYTE,
        GLConstant.UNSIGNED_BYTE,
        GLConstant.SHORT,
        GLConstant.UNSIGNED_SHORT,
        GLConstant.UNSIGNED_INT,
        GLConstant.FLOAT
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

    sparse: Optional[Accessor.Sparse] = None
    """Sparse storage of elements that deviate from their initialization value."""

    # --- Spec helpers & validators ---
    _COMPONENT_TYPE_SIZE: ClassVar[dict[GLConstant, int]] = {
        GLConstant.BYTE: 1,
        GLConstant.UNSIGNED_BYTE: 1,
        GLConstant.SHORT: 2,
        GLConstant.UNSIGNED_SHORT: 2,
        GLConstant.UNSIGNED_INT: 4,
        GLConstant.FLOAT: 4,
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
        if v and component_type in (GLConstant.FLOAT, GLConstant.UNSIGNED_INT):
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

        indices: Accessor.Sparse.Indices
        """
        An object pointing to a buffer view containing the indices of deviating accessor values.
        
        The number of indices is equal to ``count``.
        
        Indices MUST strictly increase.
        """

        values: Accessor.Sparse.Values
        """An object pointing to a buffer view containing the deviating accessor values."""

        class Indices(GLTFBase):
            """
            Object specifying the bufferView Index containing the indices of deviating accessor values.

            The number of indices is equal to ``accessor.sparse.count``.

            Indices MUST strictly increase.

            Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-accessor-sparse-indices
            """

            buffer_view: Annotated[int, Field(ge=0), IndexRef('BufferView')]
            """
            The index of the buffer view with sparse indices.
            
            The referenced buffer view MUST NOT have its ``target`` or ``byteStride`` properties defined.
            The buffer view and the optional ``byteOffset`` MUST be aligned to the ``componentType`` byte length.
            """

            byte_offset: int = Field(default=0, ge=0)
            """The offset relative to the start of the buffer view in bytes."""

            component_type: Literal[
                GLConstant.UNSIGNED_BYTE,
                GLConstant.UNSIGNED_SHORT,
                GLConstant.UNSIGNED_INT
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

            buffer_view: Annotated[int, Field(ge=0), IndexRef('BufferView')]
            """
            The index of the bufferView with sparse values.
            
            The referenced buffer view MUST NOT have its ``target`` or ``byteStride`` properties defined.
            """

            byte_offset: int = Field(default=0, ge=0)
            """The offset relative to the start of the bufferView in bytes."""


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

    buffer: Annotated[int, Field(ge=0), IndexRef('Buffer')]
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
        GLConstant.ARRAY_BUFFER,
        GLConstant.ELEMENT_ARRAY_BUFFER
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

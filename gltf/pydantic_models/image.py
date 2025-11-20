from __future__ import annotations

from typing import Optional, Annotated

from pydantic import Field, field_validator, model_validator

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed
from gltf.pydantic_models.validation_errors import GLTFSpecError


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

    buffer_view: Annotated[Optional[int], Field(default=None, ge=0), IndexRef('BufferView')]
    """
    The index of the bufferView that contains the image.
    
    This field MUST NOT be defined when uri is defined.
    """

    @field_validator('mime_type')
    @classmethod
    def _validate_mime_type_gltf_spec(cls, v: Optional[str]):
        if v is None:
            return v
        # Core glTF 2.0 supports JPEG/PNG, however many extensions to use other formats exist.
        # dds is listed as supported because I currently cannot be bothered to implement extension validation stuff.
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

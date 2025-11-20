from __future__ import annotations

import warnings
from typing import Optional

from pydantic import BaseModel, JsonValue, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

from gltf.pydantic_models.validation_errors import GLTFSpecWarning

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

from __future__ import annotations

from typing import Optional, Annotated

from pydantic import Field

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed


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

    skeleton: Annotated[Optional[int], Field(default=None, ge=0), IndexRef('Node')]
    """The index of the node used as a skeleton root. When undefined, joints transforms resolve to scene root."""

    joints: list[Annotated[int, Field(ge=0)]] = Field(min_length=1)
    """Indices of skeleton nodes, used as joints in this skin.  Must be non-empty."""

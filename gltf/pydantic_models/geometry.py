"""Pydantic models for glTF 2.0 geometry and skinning.

Defines :py:class:`Mesh`, its nested :class:`Mesh.Primitive`, and
:class:`Skin`, which together describe the renderable geometry and
skinning weights of a glTF asset.


"""

from __future__ import annotations

from typing import Optional, Annotated, Literal, TYPE_CHECKING

from pydantic import Field

from util.index_ref import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.data import Accessor
from gltf.pydantic_models.gl_constant import GLConstant

if TYPE_CHECKING:
    from gltf.pydantic_models.scene import Node


class Mesh(GLTFNamed):
    """
    A set of primitives to be rendered.

    Its global transform is defined by a node that references it.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-mesh
    """

    primitives: list[Mesh.Primitive]
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
            GLConstant.POINTS,
            GLConstant.LINES,
            GLConstant.LINE_LOOP,
            GLConstant.LINE_STRIP,
            GLConstant.TRIANGLES,
            GLConstant.TRIANGLE_STRIP,
            GLConstant.TRIANGLE_FAN,
        ] = GLConstant.TRIANGLES
        """The topology type of primitives to render."""

        targets: Optional[list[dict[str, Annotated[int, Field(ge=0), IndexRef[Accessor]]]]] = None
        """
        An array of morph targets, each Morph Target is a dictionary mapping attribute semantic
        (e.g., POSITION, NORMAL, TANGENT) to the index of the accessor containing target attribute data.
        
        Each target MUST have the same set of attributes.
        """


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

    skeleton: Annotated[Optional[int], Field(default=None, ge=0), IndexRef['Node']]
    """The index of the node used as a skeleton root. When undefined, joints transforms resolve to scene root."""

    joints: list[Annotated[int, Field(ge=0), IndexRef['Node']]] = Field(min_length=1)
    """Indices of skeleton nodes, used as joints in this skin.  Must be non-empty."""

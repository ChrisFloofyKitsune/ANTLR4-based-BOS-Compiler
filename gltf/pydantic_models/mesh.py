from __future__ import annotations

from typing import Optional, Annotated, Literal

from pydantic import Field

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.gl_constant import GLConstant


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

        targets: Optional[list[dict[str, Annotated[int, Field(ge=0), IndexRef('Accessor')]]]] = None
        """
        An array of morph targets, each Morph Target is a dictionary mapping attribute semantic
        (e.g., POSITION, NORMAL, TANGENT) to the index of the accessor containing target attribute data.
        
        Each target MUST have the same set of attributes.
        """

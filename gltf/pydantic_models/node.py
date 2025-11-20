

from __future__ import annotations

from typing import Optional, Annotated

from pydantic import Field, model_validator

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed
from gltf.pydantic_models.validation_errors import GLTFSpecError


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

    camera: Annotated[Optional[int], Field(ge=0, default=None), IndexRef('Camera')] = None
    """Index of the camera used by this node."""

    children: Optional[list[Annotated[int, Field(ge=0), IndexRef('Node')]]] = None
    """The indices of this node’s children."""

    skin: Annotated[Optional[int], IndexRef('Skin')] = None
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

    mesh: Annotated[Optional[int], Field(ge=0, default=None), IndexRef('Mesh')]
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

    nodes: Optional[list[Annotated[int, Field(ge=0), IndexRef('Node')]]] = None
    """The indices of each root node."""

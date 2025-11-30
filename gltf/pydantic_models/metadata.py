"""Pydantic models for glTF 2.0 asset- and file-level metadata.

Defines :class:`Asset` and :class:`GLTFRoot`, the top-level container
for all other pydantic models in this package.
"""

from __future__ import annotations

from typing import Optional

from pydantic import Field, model_validator

from gltf.pydantic_models.data import Buffer, BufferView, Accessor
from gltf.pydantic_models import material
from gltf.pydantic_models.animation import Animation
from gltf.pydantic_models.base_definitions import GLTFBase
from gltf.pydantic_models.validation_errors import GLTFSpecError
from gltf.pydantic_models.scene import Node, Scene, Camera
from gltf.pydantic_models.material import Image, Texture, Material
from gltf.pydantic_models.geometry import Mesh, Skin


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

        mv_major, mv_minor = (int(x) for x in self.min_version.split('.', 1))
        v_major, v_minor = (int(x) for x in self.version.split('.', 1))

        if (mv_major, mv_minor) > (v_major, v_minor):
            raise GLTFSpecError('GLTF Spec: asset.minVersion MUST NOT be greater than asset.version.')
        return self


class GLTFRoot(GLTFBase):
    """
    Top-level glTF container listing all resources and the default scene.

    Cross-references in a glTF file are index-based. Most relationships are expressed as
    0-based integer indices into arrays on this root object (or into a property of some other object).

    Non-exhaustive list of index based references:
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

    images: Optional[list[Image]] = None
    """An array of images. Image data is used to create a texture."""

    materials: Optional[list[Material]] = None
    """An array of materials. A material defines the appearance of a primitive."""

    meshes: Optional[list[Mesh]] = None
    """An array of meshes. A mesh is a set of primitives to be rendered."""

    nodes: Optional[list[Node]] = None
    """An array of nodes."""

    samplers: Optional[list[material.Sampler]] = None
    """An array of samplers. A :class:`~gltf.pydantic_models.material.Sampler` contains properties for texture filtering and wrapping modes."""

    scene: Optional[int] = None
    """The index of the default scene. This property MUST NOT be defined, when scenes is undefined."""

    scenes: Optional[list[Scene]] = None
    """An array of scenes."""

    textures: Optional[list[Texture]] = None
    """An array of textures."""

    skins: Optional[list[Skin]] = None
    """An array of skins. A skin is defined by joints and matrices."""

    @model_validator(mode='after')
    def _validate__root_constraints__scene_index_in_scenes__gltf_spec(self):
        if self.scene is not None:
            if self.scenes is None:
                raise GLTFSpecError('GLTF Spec: scene MUST NOT be defined when scenes is undefined.')
            if not (0 <= self.scene < len(self.scenes)):
                raise GLTFSpecError('GLTF Spec: scene index out of range for scenes array.')
        return self

    @model_validator(mode='after')
    def _validate__root_constraints__ext_req_subset_of_ext_used__gltf_spec(self):
        if self.extensions_required:
            used = set(self.extensions_used or [])
            missing = [ext for ext in self.extensions_required if ext not in used]
            if missing:
                raise GLTFSpecError(
                    f'GLTF Spec: extensionsRequired MUST be a subset of extensionsUsed. Missing in used: {missing}'
                )
        return self

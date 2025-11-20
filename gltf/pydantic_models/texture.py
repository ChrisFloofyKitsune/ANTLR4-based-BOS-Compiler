from __future__ import annotations

from typing import Optional, Literal, Annotated

from pydantic import Field

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed
from gltf.pydantic_models.gl_constant import GLConstant


class Sampler(GLTFNamed):
    """
    Texture sampling parameters.

    Describes magnification/minification filters and wrap modes for the S/T axes.
    Textures may reference a sampler to control how texels are sampled when rendered.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-sampler
    """

    mag_filter: Optional[Literal[
        GLConstant.NEAREST,
        GLConstant.LINEAR
    ]] = None
    """Magnification filter."""

    min_filter: Optional[Literal[
        GLConstant.NEAREST,
        GLConstant.LINEAR,
        GLConstant.NEAREST_MIPMAP_NEAREST,
        GLConstant.NEAREST_MIPMAP_LINEAR,
        GLConstant.LINEAR_MIPMAP_NEAREST,
        GLConstant.LINEAR_MIPMAP_LINEAR
    ]] = None
    """Minification filter."""

    wrap_s: Literal[
        GLConstant.CLAMP_TO_EDGE,
        GLConstant.MIRRORED_REPEAT,
        GLConstant.REPEAT
    ] = GLConstant.REPEAT

    wrap_t: Literal[
        GLConstant.CLAMP_TO_EDGE,
        GLConstant.MIRRORED_REPEAT,
        GLConstant.REPEAT
    ] = GLConstant.REPEAT


class Texture(GLTFNamed):
    """
    A texture that references an image and an optional sampler.

    Combines a source image with sampling parameters (via Sampler).

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-texture
    """

    sampler: Annotated[Optional[int], Field(default=None, ge=0), IndexRef('Sampler')]
    """The index of the sampler used by this texture."""

    source: Annotated[Optional[int], Field(default=None, ge=0), IndexRef('Image')]
    """The index of the image used by this texture."""

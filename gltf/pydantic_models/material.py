"""Pydantic models for glTF 2.0 materials, textures, samplers, and images.

Defines :class:`Image`, :class:`Sampler`, :class:`Texture`, and
:class:`Material` plus nested helper models used to express the core
PBR metallic-roughness material model.
"""

from __future__ import annotations

from typing import Optional, Literal, Annotated

from pydantic import Field, model_validator

from util.index_ref import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase
from gltf.pydantic_models.data import BufferView
from gltf.pydantic_models.gl_constant import GLConstant
from gltf.pydantic_models.validation_errors import GLTFSpecError


class Image(GLTFNamed):
    """
    Image data used to create a texture.

    Image MAY be referenced by a URI (or IRI) or a buffer view index.

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

    buffer_view: Annotated[Optional[int], Field(default=None, ge=0), IndexRef[BufferView]]
    """
    The index of the bufferView that contains the image.

    This field MUST NOT be defined when uri is defined.
    """

    @model_validator(mode='after')
    def _validate_source_gltf_spec(self):
        if self.buffer_view is not None:
            if self.uri is not None:
                raise GLTFSpecError('GLTF Spec: If bufferView is defined, uri MUST NOT be defined.')
            if self.mime_type is None:
                raise GLTFSpecError('GLTF Spec: If bufferView is defined, mimeType MUST be defined.')
        return self


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

    sampler: Annotated[Optional[int], Field(default=None, ge=0), IndexRef[Sampler]]
    """The index of the sampler used by this texture."""

    source: Annotated[Optional[int], Field(default=None, ge=0), IndexRef[Image]]
    """The index of the image used by this texture."""



class Material(GLTFNamed):
    """
    Material describing the appearance of a primitive (PBR metallic-roughness core).

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material
    """

    pbr_metallic_roughness: Optional[Material.PbrMetallicRoughness] = None
    """
    A set of parameter values that are used to define the metallic-roughness
    material model from Physically Based Rendering (PBR) methodology.
    
    When undefined, all the default values of pbrMetallicRoughness MUST apply.
    """

    normal_texture: Optional[Material.NormalTextureInfo] = None
    """
    The tangent space normal texture.
    
    The texture encodes RGB components with linear transfer function.
    
    Each texel represents the XYZ components of a normal vector in tangent space.
    
    The normal vectors use the convention +X is right and +Y is up. +Z points toward the viewer.
    
    If a fourth component (A) is present, it MUST be ignored.
    
    When undefined, the material does not have a tangent space normal texture.
    """

    occlusion_texture: Optional[Material.OcclusionTextureInfo] = None
    """
    The occlusion texture.
    
    The occlusion values are linearly sampled from the R channel.
    
    Higher values indicate areas that receive full indirect lighting and lower values indicate no indirect lighting.
    
    If other channels are present (GBA), they MUST be ignored for occlusion calculations.

    When undefined, the material does not have an occlusion texture.
    """

    emissive_texture: Optional[Material.TextureInfo] = None
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

    class TextureInfo(GLTFBase):
        """
        Texture Index with a texture coordinate set selector.

        Provides the index of a texture and the texCoord set (TEXCOORD_n) that
        a primitive must provide for proper mapping.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-textureinfo
        """

        index: Annotated[int, Field(ge=0), IndexRef[Texture]]
        """The index of the texture."""

        tex_coord: int = Field(default=0, ge=0)
        """
        This integer value is used to construct a string in the format TEXCOORD_<set index>
        which is a reference to a key in mesh.primitives.attributes (e.g. a value of 0 corresponds to TEXCOORD_0).

        A mesh primitive MUST have the corresponding texture coordinate attributes for the material to be applicable to it.
        """

    class NormalTextureInfo(TextureInfo):
        """
        Texture Index and parameters for normal mapping.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material-normaltextureinfo
        """

        scale: float = 1.0
        """
        The scalar parameter applied to each normal vector of the texture.
        
        This value scales the normal vector in X and Y directions using the formula::
        
            scaledNormal = normalize<sampled normal texture value> * 2.0 - 1.0) * vec3(<normal scale>, <normal scale>, 1.0)
        
        """

    class OcclusionTextureInfo(TextureInfo):
        """
        Texture Index and parameters for occlusion mapping.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-material-occlusiontextureinfo
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

        base_color_texture: Optional[Material.TextureInfo] = None
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

        metallic_roughness_texture: Optional[Material.TextureInfo] = None
        """
        The metallic-roughness texture.
        
        The metalness values are sampled from the B channel.
        
        The roughness values are sampled from the G channel.
        
        These values MUST be encoded with a linear transfer function.
        
        If other channels are present (R or A), they MUST be ignored for
        metallic-roughness calculations.
        
        When undefined, the texture MUST be sampled as having 1.0 in G and B components.
        """

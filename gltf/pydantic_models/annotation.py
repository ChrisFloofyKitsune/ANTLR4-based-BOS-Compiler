from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from gltf.pydantic_models.metadata import GLTFRoot
    from gltf.pydantic_models.animation import Animation


class IndexRef:
    def __init__(
        self,
        target: Literal[
            'Accessor',
            'Animation',
            'Animation.Sampler',
            'Buffer',
            'BufferView',
            'Camera',
            'Image',
            'Material',
            'Mesh',
            'Node',
            'Scene',
            'Texture',
            'Skin',
        ]
    ):
        self.target = target

    def resolve(self, source: GLTFRoot | Animation, index: int):
        from gltf.pydantic_models import animation, metadata

        if index <= 0:
            return None

        try:
            if isinstance(source, animation.Animation) and self.target == 'Animation.Sampler':
                return source.samplers[index]
            elif isinstance(source, metadata.GLTFRoot):
                match self.target:
                    # @formatter:off
                    case 'Accessor':    return source.accessors[index]
                    case 'Animation':   return source.animations[index]
                    case 'Buffer':      return source.buffers[index]
                    case 'BufferView':  return source.buffer_views[index]
                    case 'Camera':      return source.cameras[index]
                    case 'Image':       return source.images[index]
                    case 'Material':    return source.materials[index]
                    case 'Mesh':        return source.meshes[index]
                    case 'Node':        return source.nodes[index]
                    case 'Scene':       return source.scenes[index]
                    case 'Texture':     return source.textures[index]
                    case 'Skin':        return source.skins[index]
                # @formatter:on
        except IndexError as error:
            if str(error) != 'list index out of range':
                raise
        except TypeError as error:
            if str(error) != "'NoneType' object is not subscriptable":
                raise

        return None

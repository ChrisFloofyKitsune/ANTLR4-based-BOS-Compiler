import base64
import io
import mimetypes
import pathlib
import typing
import urllib.parse
from collections.abc import Sequence

from gltf.pydantic_models import GLTFRoot
from gltf.summary_tool import summarize_gltf_counts

GLTF_MAGIC_BYTE_HEADER = 0x46546C67 # 'gltf'
GLTF_CHUNK_TYPE_JSON = 0x4E4F534A # 'JSON'
GLTF_CHUNK_TYPE_BINARY = 0x004E4942 # 'bin\0'

class GLTFModel:
    """ High-level representation of a glTF model. """

    path: pathlib.Path
    raw_buffer_data: list[bytes]
    raw_image_data: list[tuple[bytes | memoryview, str]]
    gltf_root: GLTFRoot

    def __init__(self, path: pathlib.Path):
        self.path = path

        self.raw_buffer_data = []
        self.raw_image_data = []

        if self.path.suffix == '.gltf':
            self._load_from_gltf()
        elif self.path.suffix == '.glb':
            self._load_from_glb()

    def _load_from_gltf(self):
        self.gltf_root = GLTFRoot.model_validate_json(self.path.read_text())

        for buffer in self.gltf_root.buffers or []:
            buffer_bytes, buffer_mtype = self._handle_uri(buffer.uri, 'application/gltf-buffer')

            if not ('application/octet-stream' in buffer_mtype or 'application/gltf-buffer' in buffer_mtype):
                raise ValueError('Invalid media/MIME type for gltf buffer data uri')

            self.raw_buffer_data.append(buffer_bytes)

        for image in self.gltf_root.images or []:
            if image.uri is not None:
                image_bytes, image_mtype = self._handle_uri(image.uri, image.mime_type)

                if image_mtype is None:
                    image_mtype = mimetypes.guess_type(image.uri)[0]

                self.raw_image_data.append((image_bytes, image_mtype))

            if image.buffer_view is not None:
                image_mem_view = memoryview()
                image_mtype = image.mime_type




    def _handle_uri(self, uri: str, mime_type: str | None = None) -> tuple[bytes, str]:
        if uri.startswith('data:'):
            return self._handle_data_uri(uri)
        else:
            return self._handle_file_uri(uri), mime_type

    @staticmethod
    def _handle_data_uri(uri: str) -> tuple[bytes, str]:
        if not uri.startswith('data:'):
            raise ValueError('Invalid data uri, does not start with "data:"')

        parts = uri.split(sep=',', maxsplit=1)
        if len(parts) != 2:
            raise ValueError('Invalid data uri, could not split header and data parts')

        header = parts[0]
        data = parts[1]

        mediatype = 'text/plain;charset=US-ASCII'
        is_base64 = header.endswith(';base64')
        header = header.removesuffix(';base64')
        if len(header) != 0:
            mediatype = header

        byte_data = b''
        if len(data) != 0:
            if is_base64:
                byte_data = base64.standard_b64decode(data)
            else:
                byte_data = urllib.parse.unquote_to_bytes(data)

        return byte_data, mediatype

    def _handle_file_uri(self, path_str: str):
        file_path = self.path.parent / path_str;
        return file_path.resolve().read_bytes()

    def get_buffer_view_data(self, buffer_view_index: int):
        buffer_view = self.gltf_root.buffer_views[buffer_view_index]
        buffer = self.gltf_root.buffers[buffer_view.buffer]

        start_idx = buffer_view.byte_offset
        end_idx = start_idx + buffer_view.byte_length

        return memoryview(buffer)[start_idx:end_idx]


if __name__ == '__main__':
    model = GLTFModel(pathlib.Path(__file__).parent / '../animation_viewer/resources/fox/Fox.gltf')
    print(summarize_gltf_counts(model.gltf_root))
    print([f'buffer of {len(d)} bytes' for d in model.raw_buffer_data])
    print([f'image of {len(d)} bytes and media type {t}' for d, t in model.raw_image_data])


import argparse
import pathlib

from gltf.pydantic_models.metadata import GLTFRoot
from summary_tool import (
    summarize_gltf_counts,
    summarize_nodes,
    summarize_meshes,
    summarize_animations,
)

def _default_fox_path() -> pathlib.Path:
    here = pathlib.Path(__file__).parent
    return (here / '../animation_viewer/resources/fox/Fox.gltf').resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Local glTF dev viewer')
    parser.add_argument('-f', '--file', dest='file', default=None, help='Path to glTF (.gltf) JSON file')
    args = parser.parse_args(argv)

    gltf_path = pathlib.Path(args.file) if args.file else _default_fox_path()
    file_string = gltf_path.read_text(encoding='utf-8')
    gltf_root = GLTFRoot.model_validate_json(file_string)

    print(summarize_gltf_counts(gltf_root))
    print()
    print(summarize_nodes(gltf_root))
    print()
    print(summarize_meshes(
        gltf_root,
        attr_limit=None,
        include_material_names=True,
        include_targets=True,
        include_mesh_weights=True,
    ))
    print()
    print(summarize_animations(
        gltf_root,
        include_channel_details=True,
        include_sampler_details=True,
        include_targeted_nodes=True,
    ))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

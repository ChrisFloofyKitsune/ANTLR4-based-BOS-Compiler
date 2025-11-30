import os
from pathlib import Path


def walk_files(path: str | os.PathLike[str], extensions: list[str]):
    """Yield file Paths under `path` that have suffixes in `extensions`.

    This is a test-friendly copy of the original function that avoids
    importing heavy parser libraries at module import time.
    """
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            if Path(file).suffix in extensions:
                yield Path(dirpath).joinpath(file)


def purge_preproc_nodes(ast_dict: dict):
    """Return a new dict with keys/values containing 'Preproc' removed.

    This is a faithful copy of the pure transformation used in
    `tree_sitter_research.purge_preproc_nodes` and is intentionally
    standalone so unit tests can run without the full tree-sitter
    environment.
    """
    new_values = {}
    for key, value in ast_dict.items():
        if 'Preproc' in key:
            continue

        if isinstance(value, dict):
            value = purge_preproc_nodes(value)
            if value is not None and len(value) > 0:
                new_values[key] = purge_preproc_nodes(value)
        elif isinstance(value, list):
            list_values = []
            for item in value:
                if isinstance(item, dict):
                    list_values.append(purge_preproc_nodes(item))
                else:
                    list_values.append(item)
            new_values[key] = [v for v in list_values if v]
        else:
            new_values[key] = value
    return new_values


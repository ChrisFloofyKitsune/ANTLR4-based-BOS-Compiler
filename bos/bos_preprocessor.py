import os
from dataclasses import dataclass
from os import PathLike
from pathlib import PurePosixPath
from typing import Protocol

import pcpp

from unit_value_nums import UnitValue


class BosPreprocessor(pcpp.Preprocessor):

    class _PcppToken(Protocol):
        value: str
        type: str
        lineno: int
        expanded_from: list[str]
        source: str
        include_depth: int

    @dataclass
    class Chunk:
        source: PurePosixPath
        expanded_from: str | None
        text: str
        original_text: str

        @classmethod
        def _from_pcpp_token(cls, token: 'BosPreprocessor._PcppToken'):
            return cls(
                source=PurePosixPath(token.source),
                expanded_from=token.expanded_from[-1] if getattr(token, 'expanded_from', None) else None,
                original_text=token.expanded_from[0] if getattr(token, 'expanded_from', None) else token.value,
                text=token.value
            )

        def __repr__(self):
            return f'Chunk(source={self.source}, expanded_from={self.expanded_from}, original_text={repr(self.original_text)}, text={repr(self.text)})'

        def __str__(self):
            return f'[Chunk]\n  source: {self.source}\n  expanded_from: {self.expanded_from}\n  original_text: {repr(self.original_text)}\n           text: {repr(self.text)}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for def_str in [
            "TRUE 1",
            "true 1",
            "FALSE 0",
            "false 0",
            "UNKNOWN_UNIT_VALUE(val) val",
            *[f'{val.name.upper()} {val.value}' for val in UnitValue]
        ]:
            self.define(def_str)

        self.comments = []

    def define(self, tokens):
        # strip comment tokens from defines so things do not break
        if isinstance(tokens, list):
            tokens = [t for t in tokens if t.type not in self.t_COMMENT]

        return super().define(tokens)

    def on_comment(self, tok):
        # retain comments
        return True

    def on_directive_handle(self, *_, **__):
        # process and pass through
        return None

    def include(self, tokens, original_line):
        current_include_depth = self.include_depth

        def note_include_depth(tok):
            tok.include_depth = current_include_depth
            return tok

        yield from map(note_include_depth, super().include(tokens, original_line))

    def process_file(
        self,
        file_text: str,
        file_path: str | PathLike[str],
        include_paths: list[str | PathLike[str]] = None
    ):
        source_path = PurePosixPath(file_path)

        if include_paths:
            for include_path in include_paths:
                self.add_path(include_path)

        self.parse(file_text, source_path)

        preproc_chunks = [BosPreprocessor.Chunk(
            source=source_path,
            expanded_from=None,
            text=f'#line 1 "{source_path}"\n',
            original_text=''
        )]

        for token in self.parser:
            prev_chunk = preproc_chunks[-1]
            new_chunk = BosPreprocessor.Chunk._from_pcpp_token(token)

            if new_chunk.source != source_path:
                if getattr(token, 'include_depth', 0) == 1:
                    new_chunk.original_text = f'#include "{os.path.relpath(new_chunk.source, source_path.parent)}"\n'
                else:
                    new_chunk.original_text = ''

            if prev_chunk.source != new_chunk.source:
                # emit a new #line directive each time the source file changes
                preproc_chunks.append(
                    BosPreprocessor.Chunk(
                        source=source_path,
                        expanded_from=None,
                        text=f'#line {token.lineno} "{new_chunk.source}"\n',
                        original_text=''
                    )
                )
                preproc_chunks.append(new_chunk)
            else:
                if new_chunk.source != source_path:
                    # always concatenate included files, we don't really care about their macro expansions
                    prev_chunk.text += new_chunk.text
                else:
                    if prev_chunk.expanded_from == new_chunk.expanded_from:
                        prev_chunk.text += new_chunk.text
                        if new_chunk.expanded_from is None:
                            prev_chunk.original_text += new_chunk.original_text
                    else:
                        preproc_chunks.append(new_chunk)

        return (
            ''.join(c.text for c in preproc_chunks),
            ''.join(c.original_text for c in preproc_chunks),
            preproc_chunks
        )

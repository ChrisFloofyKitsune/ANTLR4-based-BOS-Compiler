from dataclasses import dataclass

from code_location import CodeLocation


class CodeError(Exception):
    def __init__(self, message: str, error_loc: CodeLocation | None):
        super().__init__(message, error_loc)
        self.message = message
        self.error_loc = error_loc

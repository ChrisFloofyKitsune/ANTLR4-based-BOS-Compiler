class GLTFSpecError(ValueError):
    """Raised when a MUST-level glTF spec is broken during validation."""


class GLTFSpecWarning(UserWarning):
    """Emitted when a SHOULD-level glTF spec (or advisory glTF spec guidance) is broken during validation."""

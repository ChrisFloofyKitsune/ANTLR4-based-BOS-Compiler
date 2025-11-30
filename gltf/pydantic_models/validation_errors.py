"""Custom error and warning types used by the glTF pydantic models.

These distinguish MUST-level violations (:class:`GLTFSpecError`) from
SHOULD-level guidance (:class:`GLTFSpecWarning`) in the glTF 2.0
specification.
"""

class GLTFSpecError(ValueError):
    """Raised when a MUST-level glTF spec is broken during validation."""


class GLTFSpecWarning(UserWarning):
    """Emitted when a SHOULD-level glTF spec (or advisory glTF spec guidance) is broken during validation."""

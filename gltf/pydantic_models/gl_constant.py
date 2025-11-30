"""
Enumeration of the special constants used in the glTF 2.0 spec.

See :obj:`gltf.pydantic_models.GLConstant`.
"""

from __future__ import annotations

from enum import IntEnum


class GLConstant(IntEnum):
    """Enum of OpenGL constants used in the glTF specification.

    .. seealso::
       - WebGL constants documentation: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants
       - GL constants lookup/translator: https://javagl.github.io/GLConstantsTranslator/GLConstantsTranslator.html
    """

    POINTS = 0x0
    LINES = 0x1
    LINE_LOOP = 0x2
    LINE_STRIP = 0x3
    TRIANGLES = 0x4
    TRIANGLE_STRIP = 0x5
    TRIANGLE_FAN = 0x6

    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406

    NEAREST = 0x2600
    LINEAR = 0x2601

    NEAREST_MIPMAP_NEAREST = 0x2700
    LINEAR_MIPMAP_NEAREST = 0x2701
    NEAREST_MIPMAP_LINEAR = 0x2702
    LINEAR_MIPMAP_LINEAR = 0x2703

    REPEAT = 0x2901
    CLAMP_TO_EDGE = 0x812F
    MIRRORED_REPEAT = 0x8370

    ARRAY_BUFFER = 0x8892
    ELEMENT_ARRAY_BUFFER = 0x8893

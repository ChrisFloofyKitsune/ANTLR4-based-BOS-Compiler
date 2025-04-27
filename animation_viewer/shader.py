import sys
from typing import TypeAlias

import pyglm.glm as glm
from OpenGL.GL import *

UniformTypes: TypeAlias = (
    bool | glm.bvec1 | glm.bvec2 | glm.bvec3 | glm.bvec4 |
    int | glm.ivec1 | glm.ivec2 | glm.ivec3 | glm.ivec4 |
    glm.uint32 | glm.uvec1 | glm.uvec2 | glm.uvec3 | glm.uvec4 |
    float | glm.vec1 | glm.vec2 | glm.vec3 | glm.vec4 |
    glm.mat2x2 | glm.mat2x3 | glm.mat2x4 | glm.mat2 |
    glm.mat3x2 | glm.mat3x3 | glm.mat3x4 | glm.mat3 |
    glm.mat4x2 | glm.mat4x2 | glm.mat4x4 | glm.mat4
)


class ShaderProgram:

    @classmethod
    def from_files(cls, vertex_shader_path: str, fragment_shader_path: str) -> 'ShaderProgram':
        with open(vertex_shader_path, 'r') as f:
            vertex_shader = f.read()
        with open(fragment_shader_path, 'r') as f:
            fragment_shader = f.read()
        return cls(vertex_shader, fragment_shader)

    def __init__(self, vertex_shader: str, fragment_shader: str):
        self.program_id = glCreateProgram()
        self._compile_shader(vertex_shader, GL_VERTEX_SHADER)
        self._compile_shader(fragment_shader, GL_FRAGMENT_SHADER)

        glLinkProgram(self.program_id)
        if not glGetProgramiv(self.program_id, GL_LINK_STATUS):
            raise Exception(glGetProgramInfoLog(self.program_id).replace(b'\\n', b'\n'))

    def _compile_shader(self, shader_source: str, shader_type: int):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, shader_source)
        glCompileShader(shader)
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            msg: bytearray = glGetShaderInfoLog(shader).replace(b'\\n', b'\n')
            sys.stderr.write(msg.decode('utf-8'))
            raise Exception(msg)

        glAttachShader(self.program_id, shader)
        glDeleteShader(shader)

    def use(self):
        glUseProgram(self.program_id)

    def set_uniform(
        self, location: int | str, value: UniformTypes
    ):
        if isinstance(location, str):
            location = glGetUniformLocation(self.program_id, location)
            if location == -1:
                raise ValueError(f"Uniform '{location}' not found in the current program.")

        if isinstance(value, (glm.bvec1 | bool | glm.ivec1 | int)):
            glProgramUniform1i(self.program_id, location, value)
        elif isinstance(value, (glm.bvec2 | glm.ivec2)):
            glProgramUniform2i(self.program_id, location, value.x, value.y)
        elif isinstance(value, (glm.bvec3 | glm.ivec3)):
            glProgramUniform3i(self.program_id, location, value.x, value.y, value.z)
        elif isinstance(value, (glm.bvec4 | glm.ivec4)):
            glProgramUniform4i(self.program_id, location, value.x, value.y, value.z, value.w)

        elif isinstance(value, (glm.uint32 | glm.uvec1)):
            glProgramUniform1ui(self.program_id, location, value)
        elif isinstance(value, glm.uvec2):
            glProgramUniform2ui(self.program_id, location, value.x, value.y)
        elif isinstance(value, glm.uvec3):
            glProgramUniform3ui(self.program_id, location, value.x, value.y, value.z)
        elif isinstance(value, glm.uvec4):
            glProgramUniform4ui(self.program_id, location, value.x, value.y, value.z, value.w)

        elif isinstance(value, (float | glm.vec1)):
            glProgramUniform1f(self.program_id, location, value)
        elif isinstance(value, glm.vec2):
            glProgramUniform2f(self.program_id, location, value.x, value.y)
        elif isinstance(value, glm.vec3):
            glProgramUniform3f(self.program_id, location, value.x, value.y, value.z)
        elif isinstance(value, glm.vec4):
            glProgramUniform4f(self.program_id, location, value.x, value.y, value.z, value.w)

        elif isinstance(value, (glm.mat2 | glm.mat2x2)):
            glProgramUniformMatrix2fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, glm.mat2x3):
            glProgramUniformMatrix2x3fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, glm.mat2x4):
            glProgramUniformMatrix2x4fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))

        elif isinstance(value, glm.mat3x2):
            glProgramUniformMatrix3x2fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, (glm.mat3 | glm.mat3x3)):
            glProgramUniformMatrix3fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, glm.mat3x4):
            glProgramUniformMatrix3x4fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))

        elif isinstance(value, glm.mat4x2):
            glProgramUniformMatrix4x2fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, glm.mat4x3):
            glProgramUniformMatrix4x3fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        elif isinstance(value, (glm.mat4 | glm.mat4x4)):
            glProgramUniformMatrix4fv(self.program_id, location, 1, GL_FALSE, glm.value_ptr(value))
        else:
            raise TypeError(f"value {repr(value)} of type {type(value)} is not supported")

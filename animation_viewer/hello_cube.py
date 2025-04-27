import OpenGL

from animation_viewer.shader import ShaderProgram

OpenGL.USE_ACCELERATE = False

import sys
import traceback

from OpenGL.GL import *
from ctypes import c_void_p, sizeof
import math, time
from pyglm import glm

from tkinter import *
from tkinter import ttk


import pyopengltk

from animation_viewer.RootTk import RootTk
from animation_viewer.texture_dds import TextureDDS
from unit_animation_engine.math import float3, float2
from unit_animation_engine.s3o import S3OModel

with open("E:/bar_dev/Beyond-All-Reason/objects3d/Units/legcom.s3o", "rb") as file:
    s3o_model = S3OModel.from_bytes(file.read())

with open("E:/bar_dev/Beyond-All-Reason/unittextures/leg_color.dds", "rb") as texture_file:
    texture = TextureDDS.from_bytes(texture_file.read())

positions: list[float3] = []
normals: list[float3] = []
tex_coords: list[float2] = []
indices: list[int] = []

for piece in s3o_model.pieces():
    parent_offset = piece.parent_offset
    if piece.parent:
        parent_offset += piece.parent.parent_offset

    indices.extend([len(positions) + i for i in piece.indices])

    for vertex in piece.vertices:
        positions.append(parent_offset + vertex.position)
        normals.append(vertex.normal)
        tex_coords.append(vertex.tex_coords)

attributes: list[float] = []

for i in range(len(positions)):
    attributes.extend([
        positions[i][0], positions[i][1], positions[i][2],
        normals[i][0], normals[i][1], normals[i][2],
        tex_coords[i][0], tex_coords[i][1],
    ])

no_of_indices = len(indices)
gl_attributes = (GLfloat * len(attributes))(*attributes)
gl_indices = (GLuint * len(indices))(*indices)


class OpenGLApp(pyopengltk.OpenGLFrame):

    def __init__(self, *args, spin_vector, **kwds):
        super().__init__(*args, kwds)
        self.__opengl_initialized = False
        self.rotation = 0.0
        self.last_time = time.monotonic()
        self.spin_vector = spin_vector
        self.shader_program: ShaderProgram | None = None
        self.drawing = False

    def initgl(self):
        if self.__opengl_initialized:
            return

        self.__opengl_initialized = True

        @GLDEBUGPROC
        def __CB_OpenGL_DebugMessage(source, type, id, severity, length, message, userParam):
            msg = message[0:length]
            print(msg.decode("utf-8"))

        glDebugMessageCallback(__CB_OpenGL_DebugMessage, None)
        errors_only = False
        if errors_only:
            glDebugMessageControl(GL_DONT_CARE, GL_DONT_CARE, GL_DONT_CARE, 0, None, GL_FALSE)
            glDebugMessageControl(GL_DEBUG_SOURCE_API, GL_DEBUG_TYPE_ERROR, GL_DONT_CARE, 0, None, GL_TRUE)
        else:
            glDebugMessageControl(GL_DONT_CARE, GL_DONT_CARE, GL_DONT_CARE, 0, None, GL_TRUE)
        glEnable(GL_DEBUG_OUTPUT)
        glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS)
        glDebugMessageInsert(GL_DEBUG_SOURCE_APPLICATION, GL_DEBUG_TYPE_MARKER, 0, GL_DEBUG_SEVERITY_NOTIFICATION,
                             -1, "Starting debug messaging service")

        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)

        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, gl_attributes, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 8 * sizeof(GLfloat), c_void_p(0 * sizeof(GLfloat)))
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 8 * sizeof(GLfloat), c_void_p(3 * sizeof(GLfloat)))
        glVertexAttribPointer(2, 2, GL_FLOAT, False, 8 * sizeof(GLfloat), c_void_p(6 * sizeof(GLfloat)))

        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, gl_indices, GL_STATIC_DRAW)

        self.shader_program = ShaderProgram.from_files('./basic_shader.vert.glsl', './basic_shader.frag.glsl')

        glEnable(GL_MULTISAMPLE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        glClearColor(0.5, 0.5, 0.5, 1)
        self.start_time = time.time()

        glViewport(0, 0, self.width, self.height)
        aspect = self.width / self.height
        self.projection_matrix = glm.perspective(glm.radians(90), aspect, 0.01, 1000)

        texture.load_into_opengl()

    def redraw(self):
        if self.drawing:
            return

        self.drawing = True
        try:
            new_time = time.monotonic()
            delta_time = new_time - self.last_time
            self.last_time = new_time
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.rotation += delta_time * 1

            # view_matrix = glm.lookAt(glm.vec3(0, -3, 0), glm.vec3(0, 0, 0), glm.vec3(0, 0, 1))

            center_pos = sum(positions)  / len(positions)

            view_matrix = glm.lookAt(glm.vec3(50,50,0), center_pos, glm.vec3(0, 1, 0))
            # model_matrix = glm.rotate(glm.identity(glm.mat4), glm.radians(elapsed_time * 90), glm.vec3(0.5, 0, 1))
            model_matrix = glm.rotate(self.rotation, self.spin_vector)
            # model_matrix = glm.identity(glm.mat4)

            self.shader_program.set_uniform('u_projection', self.projection_matrix)
            self.shader_program.set_uniform('u_view', view_matrix)
            self.shader_program.set_uniform('u_model', model_matrix)
            self.shader_program.set_uniform('u_team_color', float3(0.05, 0.91, 0.1))

            self.shader_program.use()

            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, texture.gl_texture_id)

            glDrawElements(GL_TRIANGLES, no_of_indices, GL_UNSIGNED_INT, None)

            gl_framebuffer_status = glCheckFramebufferStatus(GL_FRAMEBUFFER)
            if gl_framebuffer_status != GL_FRAMEBUFFER_COMPLETE:
                print(f"Framebuffer incomplete: {gl_framebuffer_status}")

            gl_error = glGetError()
            if gl_error != GL_NO_ERROR:
                print(f"OpenGL error: {gl_error}")
        except Exception as err:
            print(f"Error in redraw: {err}")
            traceback.print_exception(err)

        self.drawing = False


if __name__ == '__main__':
    root = RootTk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    mainframe = ttk.Frame(root, padding=10)
    mainframe.grid(column=0, row=0, sticky="nsew")
    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_rowconfigure(0, weight=1)

    app = OpenGLApp(
        mainframe,
        width=640,
        height=480,
        spin_vector=float3(0, 1, 0),
    )
    app.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
    app.animate = 10

    root.mainloop()
    exit()

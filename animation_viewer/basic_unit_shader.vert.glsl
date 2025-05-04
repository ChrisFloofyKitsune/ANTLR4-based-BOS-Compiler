#version 460 core

uniform mat4 u_projection;
uniform mat4 u_view;
uniform mat4 u_model;
uniform mat3 u_normal_matrix;

layout(std430, binding = 0) buffer MatrixBuffer
{
    mat4 mat[];
};

in vec3 in_position;
in vec3 in_normal;
in vec2 in_uv;
in ivec2 in_piece_info;

#define PIECE_ID (in_piece_info.x)
#define PARENT_ID (in_piece_info.y)
#define PIECE_MATRIX (mat[PIECE_ID])

out vec3 v_nv;
out vec2 v_uv;

void main()
{
    vec4 pos = PIECE_MATRIX * vec4(in_position, 1);
    gl_Position = (u_projection * u_view * u_model * pos);
    v_nv = normalize(u_normal_matrix * in_normal);

    v_uv = vec2(in_uv.x, 1 - in_uv.y);
}
#version 460 core

uniform mat4 u_projection;
uniform mat4 u_view;
uniform mat4 u_model;
uniform mat3 u_normal_matrix;

in vec3 in_position;
in vec3 in_normal;
in vec2 in_uv;

out vec3 v_nv;
out vec2 v_uv;

void main()
{
    gl_Position = (u_projection * u_view * u_model * vec4(in_position, 1));

    mat3 normal_matrix = transpose(inverse(mat3(u_model)));
    v_nv = normalize(u_normal_matrix * in_normal);

    v_uv = vec2(in_uv.x, 1 - in_uv.y);
}
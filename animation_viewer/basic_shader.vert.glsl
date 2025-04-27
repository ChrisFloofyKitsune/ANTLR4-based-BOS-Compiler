#version 460 core

uniform mat4 u_projection;
uniform mat4 u_view;
uniform mat4 u_model;

in vec3 a_position;
in vec3 a_normal;
in vec2 a_uv;

out vec3 v_pos;
out vec3 v_nv;
out vec2 v_uv;

void main()
{
    mat3 normal_matrix = transpose(inverse(mat3(u_model)));
    vec4 world_pos = u_model * vec4(a_position, 1);
    v_pos = world_pos.xyz;
    v_nv = normal_matrix * a_normal;
    v_uv = vec2(1, -1) * a_uv;
    gl_Position = (u_projection * u_view * world_pos);
}
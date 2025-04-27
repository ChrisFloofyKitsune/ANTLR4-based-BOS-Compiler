#version 460 core

uniform mat4 u_view;
uniform vec3 u_team_color = vec3(1);

uniform sampler2D u_texture;

in vec3 v_pos;
in vec3 v_nv;
in vec2 v_uv;

out vec3 frag_color;

void main()
{
    vec4 tex_color = texture(u_texture, v_uv);
    frag_color = mix(tex_color.rgb, u_team_color, tex_color.a);
}

#version 460 core

uniform mat4 u_view;
uniform vec3 u_team_color = vec3(1);

uniform sampler2D u_texture;

uniform int dbg_piece_select = -1;

in vec3 v_nv;
in vec2 v_uv;
in flat ivec2 v_piece_info;

#define PIECE_ID (v_piece_info.x)
#define PARENT_ID (v_piece_info.y)

out vec3 frag_color;

void main()
{
    if (dbg_piece_select != -1 && dbg_piece_select != PIECE_ID) {
        discard;
    }

    vec4 tex_color = texture(u_texture, v_uv);
    float alignedness = 0.25 + pow(dot(normalize(v_nv), vec3(0, 1, 0)), 2);
    frag_color = min(vec3(1), mix(tex_color.rgb, u_team_color, tex_color.a) * alignedness);
    //frag_color = normalize((vec3(2) + v_nv) / 2);
}

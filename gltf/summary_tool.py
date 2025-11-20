"""
Utilities and CLI tool for generating high-level summaries of glTF files

File generated pretty much entirely using GitHub Copilot. (sorry)
"""

from __future__ import annotations

from pathlib import Path
import argparse
from typing import Optional

from pydantic_models.metadata import GLTFRoot

# ---------- Pretty table helpers ----------

def _stringify(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ",".join(str(v) for v in value)
    return str(value)


def _compute_col_widths(headers: list[str] | None, rows: list[list[str]], max_col_widths: list[Optional[int]] | None = None) -> list[int]:
    col_count = len(headers) if headers else (len(rows[0]) if rows else 0)
    widths = [0] * col_count
    if headers:
        for i, h in enumerate(headers):
            widths[i] = max(widths[i], len(_stringify(h)))
    for r in rows:
        for i, cell in enumerate(r):
            if i >= col_count:
                widths.extend([0] * (i + 1 - len(widths)))
                col_count = len(widths)
            widths[i] = max(widths[i], len(_stringify(cell)))
    if max_col_widths:
        for i, cap in enumerate(max_col_widths):
            if i < len(widths) and cap is not None and cap > 0:
                widths[i] = min(widths[i], cap)
    return widths


def _align_cell(text: str, width: int, align: str) -> str:
    text = _stringify(text)
    if len(text) > width:
        return text[: max(0, width - 1)] + "…" if width > 0 else ""
    if align == 'r':
        return f"{text:>{width}}"
    if align == 'c':
        return f"{text:^{width}}"
    return f"{text:<{width}}"


def render_table(
    headers: list[str] | None,
    rows: list[list[str]],
    *,
    aligns: list[str] | None = None,
    max_col_widths: list[Optional[int]] | None = None,
    sep: str = " | ",
) -> str:
    widths = _compute_col_widths(headers, rows, max_col_widths)
    if not widths:
        return ""
    if aligns is None:
        aligns = ['l'] * len(widths)
    lines: list[str] = []
    if headers:
        head_cells = [_align_cell(h, widths[i], aligns[i]) for i, h in enumerate(headers)]
        lines.append(sep.join(head_cells))
        sep_line = sep.join('-' * widths[i] for i in range(len(widths)))
        lines.append(sep_line)
    for r in rows:
        row_cells = [_align_cell((r[i] if i < len(r) else ''), widths[i], aligns[i]) for i in range(len(widths))]
        lines.append(sep.join(row_cells))
    return "\n".join(lines)


def _heading(title: str) -> str:
    underline = '-' * len(title)
    return f"{title}\n{underline}"


# ---------- Public summary API ----------

def summarize_gltf_counts(gltf: GLTFRoot) -> str:
    def c(seq) -> int:
        return len(seq) if seq else 0
    primitives = sum((len(m.primitives) for m in (gltf.meshes or [])), 0)
    lines = [
        f"GLTF summary (version {gltf.asset.version}):",
        f"- scenes: {c(gltf.scenes)} (default: {gltf.scene if gltf.scene is not None else 'none'})",
        f"- nodes: {c(gltf.nodes)}",
        f"- meshes: {c(gltf.meshes)} (primitives: {primitives})",
        f"- materials: {c(gltf.materials)}",
        f"- animations: {c(gltf.animations)}",
        f"- images: {c(gltf.images)}",
        f"- textures: {c(gltf.textures)}",
        f"- samplers: {c(gltf.samplers)}",
        f"- skins: {c(gltf.skins)}",
        f"- accessors: {c(gltf.accessors)}",
        f"- bufferViews: {c(gltf.buffer_views)}",
        f"- buffers: {c(gltf.buffers)}",
        f"- cameras: {c(gltf.cameras)}",
    ]
    return "\n".join(lines)


def summarize_meshes(
    gltf: GLTFRoot,
    *,
    attr_limit: int | None = 6,
    include_material_names: bool = True,
    include_targets: bool = False,
    include_mesh_weights: bool = False,
) -> str:
    meshes = gltf.meshes or []
    if not meshes:
        return "Meshes: 0"
    lines: list[str] = [_heading(f"Meshes ({len(meshes)})")]

    def fmt_attr_keys(keys: list[str]) -> str:
        keys_sorted = sorted(keys)
        if attr_limit is None or len(keys_sorted) <= attr_limit:
            return ",".join(keys_sorted)
        return ",".join(keys_sorted[:attr_limit]) + ",…"

    for i, m in enumerate(meshes):
        name = m.name or f"mesh_{i}"
        overview = f"  Mesh [{i}] {name} — primitives: {len(m.primitives)}"
        if include_mesh_weights and m.weights:
            overview += f", weights: {len(m.weights)}"
        lines.append(overview)
        prim_headers = ["prim", "#attrs", "attributes", "targets", "indexed", "mode", "material"]
        prim_rows: list[list[str]] = []
        any_targets = False
        for j, p in enumerate(m.primitives):
            attr_keys = sorted(list((p.attributes or {}).keys()))
            attr_keys_str = ",".join(attr_keys) if (attr_limit is None or len(attr_keys) <= attr_limit) else ",".join(attr_keys[:attr_limit]) + ",…"
            targets = p.targets or []
            any_targets = any_targets or bool(targets)
            indices_str = "yes" if p.indices is not None else "no"
            mode_name = getattr(p.mode, 'name', str(p.mode)) if getattr(p, 'mode', None) is not None else 'TRIANGLES'
            if p.material is None:
                material_label = 'none'
            else:
                mat_idx = p.material
                if include_material_names and gltf.materials and 0 <= mat_idx < len(gltf.materials):
                    mat_name = gltf.materials[mat_idx].name or f"material_{mat_idx}"
                    material_label = f"{mat_idx}({mat_name})"
                else:
                    material_label = str(mat_idx)
            prim_rows.append([
                str(j), str(len(attr_keys)), attr_keys_str, str(len(targets)), indices_str, mode_name, material_label,
            ])
        table = render_table(prim_headers, prim_rows, aligns=['r', 'r', 'l', 'r', 'c', 'l', 'l'])
        if table:
            lines.append(table)
            lines.append("")
        if include_targets and any_targets:
            lines.append("    Morph targets:")
            tgt_headers = ["prim", "target", "#attrs", "attributes"]
            tgt_rows: list[list[str]] = []
            for j, p in enumerate(m.primitives):
                targets = p.targets or []
                for t_i, t in enumerate(targets):
                    t_keys = sorted(list(t.keys()))
                    t_keys_str = ",".join(t_keys) if (attr_limit is None or len(t_keys) <= attr_limit) else ",".join(t_keys[:attr_limit]) + ",…"
                    tgt_rows.append([str(j), str(t_i), str(len(t_keys)), t_keys_str])
            tgt_table = render_table(tgt_headers, tgt_rows, aligns=['r', 'r', 'r', 'l'])
            if tgt_table:
                lines.append(tgt_table)
                lines.append("")
    return "\n".join(lines).rstrip()


def summarize_nodes(
    gltf: GLTFRoot,
    *,
    include_parents: bool = True,
    include_counts: bool = True,
    name_col_width: int | None = 28,
) -> str:
    nodes = gltf.nodes or []
    if not nodes:
        return "Nodes: 0"
    parent_of: dict[int, int] = {}
    for idx, n in enumerate(nodes):
        for ch in (n.children or []):
            parent_of[ch] = idx
    headers = ["node", "name"]
    aligns = ['r', 'l']
    if include_parents:
        headers.append("parent"); aligns.append('r')
    if include_counts:
        headers.append("children"); aligns.append('r')
    headers += ["mesh", "camera", "skin"]; aligns += ['r', 'r', 'r']
    rows: list[list[str]] = []
    for i, n in enumerate(nodes):
        row = [str(i), n.name or ""]
        if include_parents:
            p = parent_of.get(i); row.append("-" if p is None else str(p))
        if include_counts:
            row.append(str(len(n.children or [])))
        row += ["-" if n.mesh is None else str(n.mesh), "-" if n.camera is None else str(n.camera), "-" if n.skin is None else str(n.skin)]
        rows.append(row)
    maxw = None if name_col_width is None else [None, name_col_width] + [None] * (len(headers) - 2)
    lines: list[str] = [_heading(f"Nodes ({len(nodes)})")]
    table = render_table(headers, rows, aligns=aligns, max_col_widths=maxw)
    if table:
        lines.append(table)
        lines.append("")
    return "\n".join(lines).rstrip()


def summarize_animations(
    gltf: GLTFRoot,
    *,
    include_channel_details: bool = False,
    include_sampler_details: bool = False,
    include_targeted_nodes: bool = False,
) -> str:
    animations = gltf.animations or []
    if not animations:
        return "Animations: 0"
    lines: list[str] = [_heading(f"Animations ({len(animations)})")]
    for i, a in enumerate(animations):
        name = a.name or f"animation_{i}"
        ch = a.channels or []
        sp = a.samplers or []
        path_counts: dict[str, int] = {"translation": 0, "rotation": 0, "scale": 0, "weights": 0}
        targeted_nodes: list[int] = []
        for c in ch:
            if c.target and c.target.path in path_counts:
                path_counts[c.target.path] += 1
            if c.target and c.target.node is not None:
                targeted_nodes.append(c.target.node)
        seen: set[int] = set(); uniq_nodes: list[int] = []
        for n in targeted_nodes:
            if n not in seen:
                seen.add(n); uniq_nodes.append(n)
        lines.append(
            f"  Animation [{i}] {name} — channels: {len(ch)} (T={path_counts['translation']}, R={path_counts['rotation']}, "
            f"S={path_counts['scale']}, W={path_counts['weights']}), samplers: {len(sp)}, nodes: {len(uniq_nodes)}"
        )
        if include_targeted_nodes and uniq_nodes:
            tn_headers = ["node", "name"]
            tn_rows: list[list[str]] = []
            for n_idx in uniq_nodes:
                nm = ""
                if gltf.nodes and 0 <= n_idx < len(gltf.nodes):
                    nm = gltf.nodes[n_idx].name or ""
                tn_rows.append([str(n_idx), nm])
            tn_table = render_table(tn_headers, tn_rows, aligns=['r', 'l'])
            if tn_table:
                lines.append(tn_table)
                lines.append("")
        if include_channel_details and ch:
            ch_headers = ["ch", "sampler", "node", "node_name", "path"]
            ch_rows: list[list[str]] = []
            for j, c in enumerate(ch):
                node = c.target.node if (c.target and c.target.node is not None) else None
                node_name = ""
                if node is not None and gltf.nodes and 0 <= node < len(gltf.nodes):
                    node_name = gltf.nodes[node].name or ""
                ch_rows.append([str(j), str(c.sampler), "" if node is None else str(node), node_name, c.target.path if c.target else 'n/a'])
            ch_table = render_table(ch_headers, ch_rows, aligns=['r', 'r', 'r', 'l', 'l'])
            if ch_table:
                lines.append(ch_table)
                lines.append("")
        if include_sampler_details and sp:
            smp_headers = ["smp", "input", "output", "interp"]
            smp_rows: list[list[str]] = []
            for j, s in enumerate(sp):
                interp = getattr(s, 'interpolation', 'LINEAR')
                smp_rows.append([str(j), str(s.input), str(s.output), str(interp)])
            smp_table = render_table(smp_headers, smp_rows, aligns=['r', 'r', 'r', 'l'])
            if smp_table:
                lines.append(smp_table)
                lines.append("")
    return "\n".join(lines).rstrip()


# ---------- Loader and CLI ----------

def load_gltf_from_path(path: Path | str) -> GLTFRoot:
    text = Path(path).read_text(encoding='utf-8')
    return GLTFRoot.model_validate_json(text)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description='glTF summary tool')
    parser.add_argument('-f', '--file', dest='file', required=True, help='Path to glTF (.gltf) JSON file')
    parser.add_argument('--no-channel-details', dest='channel_details', action='store_false', help='Omit per-channel table')
    parser.add_argument('--no-sampler-details', dest='sampler_details', action='store_false', help='Omit per-sampler table')
    parser.add_argument('--no-targeted-nodes', dest='targeted_nodes', action='store_false', help='Omit targeted nodes table')
    parser.add_argument('--no-material-names', dest='material_names', action='store_false', help='Do not show material names')
    parser.set_defaults(channel_details=True, sampler_details=True, targeted_nodes=True, material_names=True)
    args = parser.parse_args(argv)

    gltf = load_gltf_from_path(args.file)

    print(summarize_gltf_counts(gltf))
    print()
    print(summarize_nodes(gltf))
    print()
    print(summarize_meshes(
        gltf,
        attr_limit=None,
        include_material_names=args.material_names,
        include_targets=True,
        include_mesh_weights=True,
    ))
    print()
    print(summarize_animations(
        gltf,
        include_channel_details=args.channel_details,
        include_sampler_details=args.sampler_details,
        include_targeted_nodes=args.targeted_nodes,
    ))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

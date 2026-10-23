# -*- coding: utf-8 -*-
"""
TextureAudit.py - salt okunur texture envanteri.

Editorde: Output Log -> Cmd kutusunu "Python" yap ve sunu yaz:
    exec(open(r"C:/Users/Niyazi/KutunYukselisi/Tools/TextureAudit.py").read())

CSV ciktisi: <Proje>/Saved/TextureAudit.csv
Hicbir asset'e dokunmaz, sadece rapor uretir.
"""
import os
import unreal

OUT = os.path.join(unreal.Paths.project_saved_dir(), "TextureAudit.csv")

# Her klasor icin hedef cozunurluk tavani (bkz. butce tablosu).
BUDGET = [
    ("/Game/Kutun/UI/",                      0),      # 0 = elle, UI'da upscale istemiyoruz
    ("/Game/Kutun/Characters/Player/",       2048),
    ("/Game/Kutun/Characters/Enemies/",      2048),
    ("/Game/Kutun/Characters/",              2048),
    ("/Game/Kutun/Weapons/",                 2048),
    ("/Game/Kutun/Environment/Materials/",   2048),
    ("/Game/Kutun/Environment/Props/",       1024),
    ("/Game/Kutun/VFX/",                     512),
]

def budget_for(path):
    for prefix, cap in BUDGET:
        if path.startswith(prefix):
            return cap
    return 1024

def role_of(name):
    n = name.lower()
    if "normal" in n:
        return "normal"
    if any(k in n for k in ("orm", "mask", "roughness", "metallic", "ao", "occlusion", "height", "opacity", "alpha")):
        return "mask"
    if any(k in n for k in ("basecolor", "diffuse", "albedo", "color", "emissive")):
        return "color"
    return "?"

def main():
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    f = unreal.ARFilter(class_names=["Texture2D"], package_paths=["/Game"],
                        recursive_paths=True, recursive_classes=True)
    assets = ar.get_assets(f)

    rows = []
    total = 0
    for a in assets:
        path = str(a.package_name)
        tex = unreal.EditorAssetLibrary.load_asset(path)
        if not tex:
            continue
        try:
            x = tex.blueprint_get_size_x()
            y = tex.blueprint_get_size_y()
        except Exception:
            x = y = -1
        disk = 0
        fn = unreal.Paths.convert_relative_path_to_full(
            unreal.PackageTools.package_name_to_filename(path) + ".uasset") \
            if hasattr(unreal, "PackageTools") else ""
        if fn and os.path.isfile(fn):
            disk = os.path.getsize(fn)
        total += disk
        name = path.rsplit("/", 1)[-1]
        cap = budget_for(path)
        rows.append({
            "path": path,
            "x": x, "y": y,
            "disk_mb": round(disk / 1048576.0, 2),
            "comp": str(tex.get_editor_property("compression_settings")).split(".")[-1],
            "srgb": tex.get_editor_property("srgb"),
            "lod_group": str(tex.get_editor_property("lod_group")).split(".")[-1],
            "max_size": tex.get_editor_property("max_texture_size"),
            "never_stream": tex.get_editor_property("never_stream"),
            "role": role_of(name),
            "budget": cap,
            "over_budget": (cap > 0 and max(x, y) > cap),
        })

    rows.sort(key=lambda r: -r["disk_mb"])
    with open(OUT, "w") as fh:
        fh.write("path,width,height,disk_mb,compression,srgb,lod_group,max_texture_size,never_stream,role,budget,over_budget\n")
        for r in rows:
            fh.write("{path},{x},{y},{disk_mb},{comp},{srgb},{lod_group},{max_size},{never_stream},{role},{budget},{over_budget}\n".format(**r))

    over = [r for r in rows if r["over_budget"]]
    unreal.log("=== TextureAudit ===")
    unreal.log("{} texture, diskte {:.0f} MB".format(len(rows), total / 1048576.0))
    unreal.log("Butce ustu: {} texture, {:.0f} MB".format(
        len(over), sum(r["disk_mb"] for r in over)))
    for r in rows[:25]:
        unreal.log("  {:7.1f} MB  {}x{}  {:12s} {}".format(
            r["disk_mb"], r["x"], r["y"], r["comp"], r["path"]))
    unreal.log("CSV: " + OUT)

main()

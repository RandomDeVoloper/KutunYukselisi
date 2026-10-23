# -*- coding: utf-8 -*-
"""
TextureOptimize.py - texture ayarlarini butceye gore toplu duzeltir.

VARSAYILAN DRY_RUN = True -> hicbir sey degismez, sadece ne yapacagini yazar.
Uygulamak icin asagidaki DRY_RUN'i False yap.

Editorde: Output Log -> Cmd = Python:
    exec(open(r"C:/Users/Niyazi/KutunYukselisi/Tools/TextureOptimize.py").read())

NE YAPAR (kaynak dosyaya DOKUNMAZ, geri alinabilir):
  - max_texture_size  -> klasor butcesi (cook/VRAM boyutunu kirpar)
  - compression       -> normal map = TC_Normalmap, maske/ORM = TC_Masks, renk = TC_Default
  - srgb              -> normal ve maskelerde kapali, renkte acik
  - lod_group         -> Character / Weapon / World / UI
  - mip_gen_settings  -> FromTextureGroup (UI haric)
  - never_stream      -> UI haric kapali (streaming acik)

NE YAPMAZ: .uasset'in diskteki boyutunu kucultmez. Onun icin kaynak PNG'yi
kucultup reimport etmek gerekir (bkz. README notu / 2. faz).
"""
import unreal

DRY_RUN = True
SAVE = True

TG = unreal.TextureGroup
TC = unreal.TextureCompressionSettings
MIP = unreal.TextureMipGenSettings

# (yol oneki, max boyut, lod group)
RULES = [
    ("/Game/Kutun/UI/",                     None, TG.TEXTUREGROUP_UI),
    ("/Game/Kutun/Characters/",             2048, TG.TEXTUREGROUP_CHARACTER),
    ("/Game/Kutun/Weapons/",                2048, TG.TEXTUREGROUP_WEAPON),
    ("/Game/Kutun/Environment/Materials/",  2048, TG.TEXTUREGROUP_WORLD),
    ("/Game/Kutun/Environment/Props/",      1024, TG.TEXTUREGROUP_WORLD),
    ("/Game/Kutun/VFX/",                    512,  TG.TEXTUREGROUP_EFFECTS),
]
# Bu yollara hic dokunma (marketplace / sablon icerik)
SKIP = ("/Game/Fab/", "/Game/FirstPerson/", "/Game/ThirdPerson/", "/Game/NeonGrid/",
        "/Game/CombatMagicAnims/", "/Game/Characters/Mannequins/", "/Game/Developers/",
        "/Game/Splash/")

NORMAL_KEYS = ("normal",)
MASK_KEYS = ("orm", "mask", "roughness", "metallic", "_ao", "occlusion", "height",
             "opacity", "alpha", "specular")

def rule_for(path):
    for prefix, cap, group in RULES:
        if path.startswith(prefix):
            return cap, group
    return None, None

def role_of(name):
    n = name.lower()
    if any(k in n for k in NORMAL_KEYS):
        return "normal"
    if any(k in n for k in MASK_KEYS):
        return "mask"
    return "color"

def main():
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    f = unreal.ARFilter(class_names=["Texture2D"], package_paths=["/Game"],
                        recursive_paths=True, recursive_classes=True)
    changed = []
    for a in ar.get_assets(f):
        path = str(a.package_name)
        if any(path.startswith(s) for s in SKIP):
            continue
        cap, group = rule_for(path)
        if group is None:
            continue
        tex = unreal.EditorAssetLibrary.load_asset(path)
        if not tex:
            continue

        name = path.rsplit("/", 1)[-1]
        role = role_of(name)
        is_ui = group == TG.TEXTUREGROUP_UI

        want = {}
        if role == "normal":
            want["compression_settings"] = TC.TC_NORMALMAP
            want["srgb"] = False
        elif role == "mask":
            want["compression_settings"] = TC.TC_MASKS
            want["srgb"] = False
        else:
            want["compression_settings"] = TC.TC_DEFAULT
            want["srgb"] = True

        want["lod_group"] = group
        if cap is not None:
            want["max_texture_size"] = cap
        if not is_ui:
            want["mip_gen_settings"] = MIP.TMGS_FROM_TEXTURE_GROUP
            want["never_stream"] = False

        diff = {}
        for k, v in want.items():
            cur = tex.get_editor_property(k)
            if cur != v:
                diff[k] = (cur, v)
        if not diff:
            continue

        changed.append(path)
        unreal.log("{}  [{}]".format(path, role))
        for k, (cur, v) in diff.items():
            unreal.log("    {}: {} -> {}".format(k, cur, v))
        if not DRY_RUN:
            for k, (_cur, v) in diff.items():
                tex.set_editor_property(k, v)
            if SAVE:
                unreal.EditorAssetLibrary.save_loaded_asset(tex, only_if_is_dirty=False)

    unreal.log("=== TextureOptimize {} ===".format("DRY RUN" if DRY_RUN else "UYGULANDI"))
    unreal.log("{} texture etkilendi".format(len(changed)))

main()

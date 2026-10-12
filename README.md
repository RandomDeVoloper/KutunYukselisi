# Kutun Yükselişi (ISIK)

Unreal Engine ile geliştirilen bir oyun projesi. Depo adı `KutunYukselisi`, Unreal proje adı `ISIK`.

## Gereksinimler

- Unreal Engine **5.8** (`ISIK.uproject` içindeki `EngineAssociation`)
- [Git LFS](https://git-lfs.com/): `.uasset`, `.umap`, `.fbx`, `.png`, `.wav` ve `.mp3` dosyaları LFS ile izlenir (bkz. `.gitattributes`). `ISIK.uproject` bilerek düz metindir, LFS'te değildir.

## Kurulum

```bash
git lfs install
git clone https://github.com/RandomDeVoloper/KutunYukselisi.git
```

Ardından `ISIK.uproject` dosyasını Unreal Editor ile açın.

## Proje yapısı

Proje pratikte yalnızca Blueprint kullanır; `Source/ISIK` içinde C++ kodu yoktur. Oyun mantığı `Content/` altındaki `.uasset` / `.umap` dosyalarındadır. Bu dosyalar ikilidir ve metin olarak okunup karşılaştırılamaz, bu yüzden Unreal Editor ile düzenlenmelidir.

| Ayar | Değer |
| --- | --- |
| Editör başlangıç haritası | `/Game/Kutun/Maps/L_Tutorial_New` |
| Paketlenmiş oyun varsayılan haritası | `/Game/Kutun/Maps/L_Main3DMenu` |
| Varsayılan GameMode | `/Game/Kutun/Core/GameMode/BP_TelekineziGameMode` |

Bu değerler `Config/DefaultEngine.ini` içinde tanımlıdır. Paketlenecek haritalar `Config/DefaultGame.ini` içindeki `MapsToCook` listesindedir.

### Klasör düzeni

Oyunun kendi içeriği `Content/Kutun/` altındadır:

| Klasör | İçerik |
| --- | --- |
| `Core` | Interface'ler (`BPI_*`), enum'lar (`E_*`), `UC_HealthComponent`, `SG_Settings`, `GameMode/BP_TelekineziGameMode` |
| `Characters` | `Player` (`BP_Telekinezi`, Kam modeli, animasyonlar), `Enemies/{Base,Mongol,Bizans,Chinese,Spawners}`, `Souls`, `Animals`, `Uldiz` |
| `Weapons` | `BP_Throwable`, `Sword`, `SwordMount`, `Axe`, `Spear`, `Balbal` |
| `VFX` | `SaberTrail`, `SwordTrailPack`, `ItadoriAura`, `Materials`, `CameraShakes` |
| `Environment` | `Props/<Obje>`, `Materials/Landscape`, `Foliage` |
| `UI` | `Widgets` (`WBP_*`), `Textures` (`T_UI_*`), `Fonts` |
| `Audio` | `Music`, `Ambience`, `SFX`, `UI`, `Voice` (`SW_*`, `ATT_*`) |
| `Gameplay` | `BP_TutorialTrigger` |
| `Maps` | `L_Main3DMenu`, `L_Tutorial_New`, `Oba_L`, `Cinematics` |

İsimler tür ön eki + PascalCase kullanır: `BP_`, `WBP_`, `ABP_`, `BPI_`, `E_`, `SG_`, `SM_`, `SK_`, `SKEL_`, `PHYS_`, `M_`, `MI_`, `T_`, `NS_`, `SW_`, `ATT_`, `LS_`, `L_`. `Fab`, `NeonGrid`, `ThirdPerson`, `FirstPerson`, `CombatMagicAnims`, `Characters/Mannequins`, `Input` ve `Weapons/GrenadeLauncher` şablon veya marketplace içeriğidir ve yerinde bırakılmıştır. Kişisel test haritaları `Developers/` altındadır.

`Content/Kutun` klasör renkleri `Config/DefaultEditorPerProjectUserSettings.ini` içinde tanımlıdır.

## Üretilen klasörler

`Binaries/`, `Intermediate/`, `DerivedDataCache/` ve `Saved/` Unreal tarafından üretilir ve `.gitignore` ile dışarıda bırakılır. Bu klasörleri elle düzenlemeyin.

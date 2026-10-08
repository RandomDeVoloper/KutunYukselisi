# Kutun Yükselişi (ISIK)

Unreal Engine ile geliştirilen bir oyun projesi. Depo adı `KutunYukselisi`, Unreal proje adı `ISIK`.

## Gereksinimler

- Unreal Engine **5.6** (`ISIK.uproject` içindeki `EngineAssociation`)
- [Git LFS](https://git-lfs.com/): `.uasset`, `.umap` ve `.uproject` dosyaları LFS ile izlenir (bkz. `.gitattributes`)

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
| Editör başlangıç haritası | `/Game/Levels/L_Tutorial` |
| Paketlenmiş oyun varsayılan haritası | `/Game/Levels/L_Main3DMenu` |
| Varsayılan GameMode | `/Game/Telekinezi/Blueprints/GameMode/BP_TelekineziGameMode` |

Bu değerler `Config/DefaultEngine.ini` içinde tanımlıdır.

## Üretilen klasörler

`Binaries/`, `Intermediate/`, `DerivedDataCache/` ve `Saved/` Unreal tarafından üretilir ve `.gitignore` ile dışarıda bırakılır. Bu klasörleri elle düzenlemeyin.

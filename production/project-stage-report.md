# Project Stage Analysis — TOYGARD

**Tarih:** 5 Kasım 2026
**Stage:** Production
**Stage Confidence:** PASS — net sinyal
**Analiz:** `project-stage-detect` skill (CCGS v1.2.0)

---

## Proje Özeti

**Ad:** TOYGARD (repo: KutunYukselisi)
**Motor:** Unreal Engine 5.8, Blueprint-only
**Konsept:** Türk mitolojisi evreni; telekinezi + nesne ölçeklendirme + kılıç sörfü mekanikleri

---

## Completeness Overview

| Alan | Durum | Detay |
|---|---|---|
| Oyun İçeriği | ✅ Aktif | 559 asset (.uasset/.umap), 27 BP, 4 harita, 18 widget |
| GDD | ✅ Var | `docs/TOYGARD_GDD.md` — pitch, core loop, MoSCoW |
| Sprint Planı | ✅ Var | `docs/HAFTALIK_PLAN.md` (20–26 Ekim 2026) |
| Blueprint Denetimi | ✅ Var | `docs/BLUEPRINT_DENETIMI.md` — Faz 1–3 tamam |
| Mimari | ⚠️ Kısmi | `docs/architecture/tr-registry.yaml` var, ADR yok |
| Test | ❌ Yok | Blueprint-only projede beklenen durum |
| Epics/Stories | ❌ Yok | Haftalık plan bunun yerini tutuyor |

**Rigor tier:** `minimal` (project.yaml'da `modes:` bloğu yok — default).
Bu tier'da ADR, art bible ve sprint dosyaları zorunlu değil.

---

## Harita Durumu

| Harita | Yol | Durum |
|---|---|---|
| L_Main3DMenu | `/Game/Kutun/Maps/L_Main3DMenu` | ✅ Ana menü |
| Stand_Arena | `/Game/Kutun/Maps/Stand_Arena` | ✅ Ana oyun + sinematik giriş |
| Oba_L | `/Game/Kutun/Maps/Oba_L` | ⚠️ Son commit'te dokunulmadı |
| L_Trailer | `/Game/Kutun/Maps/L_Trailer` | ⚠️ Yalnızca cook listesinde |

---

## Blueprint Durumu

| Blueprint | Node | Durum |
|---|---|---|
| BP_Telekinezi | 1114 (320 EventGraph) | ⚠️ Çok büyük, bölünmeli |
| BP_Enemy | 166 | ✅ Temiz |
| BP_Axe | 217 | ✅ Temiz |
| UC_HealthComponent | 50 | ✅ Temiz |

---

## Açık Maddeler

### Yüksek Öncelik

1. **WBP_LoadingScreen hâlâ BP_Telekinezi'de**
   - `BeginPlay` zincirinde `CreateWidget(WBP_LoadingScreen) → AddToViewport → Delay(5s) → RemoveFromParent` bloğu koparılmadı
   - Sinematik giriş sahnesi ilk 5 saniye loading screen tarafından kapatılıyor
   - Düzeltme: `BindEventToOnDepleted`'in exec çıkışını `GetAllActorsOfClass(BP_Sword)`'a bağla, ara 5 node'u sil

2. **BP_Telekinezi dead node temizliği (21 node)**
   - `BLUEPRINT_DENETIMI.md` Faz 4 henüz tamamlanmadı
   - Ölü node'lar: `CreateWidget_1/7/8/10`, eski HUD zinciri parçaları

### Orta Öncelik

3. **BP_Telekinezi EventGraph bölünmeli**
   - 320 node, 29 event — tek graph'ta çok fazla sorumluluk
   - `BLUEPRINT_DENETIMI.md`'de belgelendi, refactor planlanıyor

4. **GDD dosya yolu uyumsuzluğu**
   - `TOYGARD_GDD.md` `docs/` altında, `design/gdd/game-concept.md` yolunda değil
   - Artifact-check tarafından ABSENT olarak raporlanıyor

---

## Recommended Next Steps

```
1. [YÜKSEK] Editörde BP_Telekinezi → WBP_LoadingScreen node'larını sil (2 dk)
2. [YÜKSEK] BP_Telekinezi dead node temizliği — BLUEPRINT_DENETIMI Faz 4
3. [ORTA]   TOYGARD_GDD.md → design/gdd/game-concept.md olarak taşı/kopyala
4. [ORTA]   BP_Telekinezi EventGraph'ı fonksiyonlara böl
5. [DÜŞÜK]  Oba_L haritasına ilerleyin
```

---

## Sonuç

Proje **Production** aşamasında ve sağlıklı durumda. Oyun mekanikleri çalışıyor:
telekinezi, nesne ölçeklendirme, kılıç fırlatma/geri çağırma, kılıç sörfü,
düşman AI (PawnSensing), sağlık sistemi, sinematik giriş sahnesi, ana menü,
pause menu, can barı, restart akışı.

Öncelikli iş: `BP_Telekinezi` temizliği (WBP_LoadingScreen + dead nodes).

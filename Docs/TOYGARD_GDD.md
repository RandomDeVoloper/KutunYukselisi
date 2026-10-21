# TOYGARD — Oyun Tasarım Belgesi (GDD)

**Versiyon:** 1.0 | **Tarih:** Ekim 2026 | **Motor:** Unreal Engine 5.8

---

## Pitch

> "Oyuncu, Türk mitolojisindeki Kut inancını silah olarak kullanan, hem tanrılardan hem de düşmanlarından intikam arayan bir savaşçıyı canlandırır."

Toygard, **aksiyon-puzzle** mekaniklerini Türk mitolojisi evreniyle buluşturan, **telekinezi** ve **nesne ölçeklendirme** güçlerini temel alan bir UE5 prototip projesidir.

---

## Oyuncu Fantazisi

> "Kut'u ellerinde tutan, fizik yasalarını büken, düşmanlarını kendi silahlarıyla yok eden bir efsane kahraman."

---

## Temel Mekanikler (Core Loop)

```
Keşfet → Düşmanla Karşılaş → Kut Güçlerini Kullan → Karar Ver → Ödül Al → İlerle
                                      ↑
                    (Telekinezi / Ölçeklendirme / Kılıç Uçuşu)
```

### Kut Güçleri

| Güç | Tuş | Açıklama |
|-----|-----|----------|
| Telekinezi | Fare Orta | Nesne tut / fırlat |
| Ölçeklendirme | Scroll Up/Down | Tuttuğun nesneyi büyüt/küçült |
| Eksen Maskesi | 1 / 2 / 3 | X / Y / Z eksenini aç-kapat |
| Kılıç Uçuşu | F | Kılıcı fırlat, geri çağır |
| Kılıç Sörfü | Kılıç üzerindeyken | Kılıcın üzerinde uçuş |

---

## Teknik Mimari

- **Motor:** UE 5.8, Blueprint-only (C++ modül yok)
- **Oyuncu:** `BP_Telekinezi` (Character)
- **Düşman:** `BP_Enemy` (Character, PawnSensing AI)
- **Sağlık:** `UC_HealthComponent` (bağımsız ActorComponent)
- **GameMode:** `BP_TelekineziGameMode`
- **Input:** Enhanced Input (`IMC_Default`, `IMC_MouseLook`)

### İçerik Yapısı

```
Content/Kutun/
├── Characters/    (Player, Enemies, Animals)
├── Weapons/       (Sword, Axe, Spear, Balbal)
├── UI/            (WBP_* widget'ları)
├── Audio/         (Music, SFX, Voice)
├── VFX/           (trail, aura, shake)
├── Environment/   (Props, Materials, Foliage)
├── Core/          (BPI_*, UC_Health, GameMode)
└── Maps/          (L_Main3DMenu, L_Tutorial_New, Oba_L)
```

---

## MoSCoW Önceliklendirme

### Must Have (Prototip için zorunlu)
- [x] Telekinezi sistemi (tut, fırlat, ölçeklendir)
- [x] Temel düşman AI (PawnSensing, saldırı, ölüm)
- [x] Sağlık sistemi (UC_HealthComponent)
- [x] Stand Modu (arena dalgaları)
- [x] Ana menü + pause menü

### Should Have (Beta için)
- [ ] Kılıç sörfü polish
- [ ] Düşman çeşitliliği (Moğol, Bizans, Çin)
- [ ] Save sistemi (SG_Settings)
- [ ] Ses tasarımı tamamlama

### Could Have (İleride)
- [ ] Uldiz karakteri
- [ ] At mekaniği
- [ ] Sinematik sekanslar

### Won't Have (Bu prototipte yok)
- Multiplayer
- Tam Türkçe seslendirme

---

## Teknik Borç (Blueprint Denetimi Sonuçları)

> Ölçüm 21 Ekim 2026'da Unreal MCP ile canlı proje üzerinde yapıldı.
> Ayrıntı: [BLUEPRINT_DENETIMI.md](BLUEPRINT_DENETIMI.md)

| Blueprint | Sorun | Öncelik | Durum |
|-----------|-------|---------|-------|
| BP_Enemy | `CameraBoom` — oyuncudan kopya, 0 referans | KRİTİK | Silinecek |
| BP_Enemy | `MaxEnemies` + `CurrentSpawns` — 0 referans | KRİTİK | Silinecek |
| BP_Telekinezi | `/Engine/VREditor/.../Camera_Shutter` — cook riski | KRİTİK | Değişecek |
| BP_Telekinezi ↔ BP_Enemy | Döngüsel hard referans | YÜKSEK | BPI_CombatTarget'a geçilecek |
| BP_Telekinezi | EventGraph'ta 21 ölü node (eski HUD zinciri) | YÜKSEK | Doğrulanıp silinecek |
| BP_Telekinezi | 1114 node / 48 graph — EventGraph'ta 29 giriş | ORTA | Bölünecek |
| BP_Telekinezi | `WBP_ScaleAxes` kullanılmıyor olabilir | ORTA | Doğrulanacak |
| BP_Enemy | `Spawner` write-only, generic `Object` tipli | İZLE | Eski spawner'lara bağlı |
| BP_Telekinezi | `MATERIALCHANGE` kollapslı graph (çift chain) | İZLE | Elle refactor |

**Temiz çıkanlar:** `UC_HealthComponent` (50 node, 0 ölü), `BP_Axe` (217 node, 1 kopuk — CLAUDE.md'deki "323 ölü node" notu güncel değil), `BP_EnemySpawner` (72 node).

---

## Haftalık Plan — 20–26 Ekim 2026

| Gün | Dev Ajan | Tasarım Ajan | Sanat Ajan |
|-----|----------|--------------|------------|
| Pzt | Blueprint denetimi başlat | GDD finalize | Silah prop listesi |
| Sal | Teknik borç belgesi | Core loop diyagramı | Referans görseller |
| Çar | BP_Enemy CameraBoom sil | Düşman davranış tablosu | Düşman görsel kiti |
| Per | Duplicate kod → fonksiyon | Level tasarım brifingi | Environment moodboard |
| Cum | Hard ref → Soft ref | Yeni mekanik önerisi | VFX placeholder listesi |
| Cmt | Prototip build test | Playtest notları | Build için asset listesi |
| Paz | Retrospektif ve hata düzeltme | Sonraki sprint planı | Eksik asset tamamlama |

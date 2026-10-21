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

> Bu bölüm BP denetimi tamamlandıkça güncellenecek.

| Blueprint | Sorun | Öncelik | Durum |
|-----------|-------|---------|-------|
| BP_Enemy | CameraBoom component (oyuncudan kopya) | KRİTİK | Bekliyor |
| BP_Axe | ~323 ölü node birikmiş | YÜKSEK | Bekliyor |
| BP_Telekinezi | Hard ref texture/mesh assetleri | ORTA | Bekliyor |
| BP_Telekinezi | MATERIALCHANGE kollapslı graph (çift chain) | ORTA | Bekliyor |
| UC_HealthComponent | OnDepleted pin kopukluğu riski | KRİTİK | Doğrula |

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

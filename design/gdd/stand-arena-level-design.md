# Stand_Arena — Seviye Tasarımı GDD

**Harita:** `/Game/Kutun/Maps/Stand_Arena`
**Durum:** Taslak (2026-11-09)

---

## 1. Overview

Stand_Arena tek bir sürekli haritada iki deneyim sunar: oyuncuyu mekaniklere alıştıran bir **tutorial bölgesi** ve ardından terkedilmiş antik bir savaş alanında patlayan **toplu savaş**. Türk/Orta Asya ve Bizans mimarisinin karışımı, harabeye dönmüş bir savaş alanı atmosferi yaratır.

---

## 2. Player Fantasy

> "Yalnızca ben kaldım. Önümde düşmanlarla dolu bir alan var. Silahım benim iradem."

Oyuncu önce güçlerini küçük, güvenli bir alanda öğrenir; sonra geniş, kaotik bir savaş alanına adım atar ve hem telekinezi hem kılıç yeteneklerini özgürce birleştirerek hayatta kalmaya çalışır.

---

## 3. Bölge Düzeni

### Bölge A — Tutorial Koridoru

Oyuncunun spawn olduğu dar, kapalı alan. `PlayerStart`'ın **en az 500 ünite uzağında** başlayan tetikleyiciler (spawn noktasına trigger koymak ilk adımı atlatabilir).

| Adım | BP_TutorialTrigger metni (örnek) | Öğretilen mekanik |
|------|----------------------------------|-------------------|
| 1 | "Tutmak için **[Sol Tık]** basılı tut" | Grab / telekinezi tutma |
| 2 | "Fırlat! **[Sol Tık]** bırak" | Nesne fırlatma |
| 3 | "Büyüt / Küçült: **[Fare Tekerleği]**" | Ölçekleme |
| 4 | "Eksen kilidi: **X / Y / Z**" | Eksen maskeleme |
| 5 | "Kılıcı çağır: **[E]**" | SwordRecall |

**Ortam:** Dar taş koridorlar, ahşap fıçılar ve küpler (fırlatma hedefleri), bir barikat (kılıç pratiği için).

### Bölge B — Geçiş Kapısı

İki bölge arasındaki görsel sınır. Yıkılmış bir kale kapısı ya da çökmüş kemer. Oyuncu geçince geri dönüş yok.

Geçiş sırasında kamera hafifçe geri çekilerek arenayı tanıtır (**savaş alanı reveal**).

### Bölge C — Antik Savaş Alanı (Ana Arena)

Geniş, açık, engebeli zemin. Çevrede:
- Bizans kolonları (bir kısmı yıkık)
- Orta Asya çadır kalıntıları (yanmış ahşap direkleri)
- Dağılmış silahlar, kalkanlar, iskeletler (atmosfer)
- Birkaç yükseltilmiş platform (taktiksel konum fırsatı)

**Düşman yerleşimi (toplu savaş):**

| Grup | Tür | Adet | Başlangıç konumu |
|------|-----|------|-----------------|
| Öncü | Mongol | 3 | Arena girişi yakını |
| Flanklayıcı | Bizans | 4 | Sağ-sol kanatlar |
| Merkez | Karışık | 5-6 | Orta hat |
| **Toplam** | | **~12-13** | |

Hepsi aynı anda aktif — spawn efekti ile değil, zaten alanda duruyor gibi; oyuncu kapıdan geçince `AI` aktive olur.

---

## 4. Akış (Pacing)

```
Spawn → [Tutorial A, ~3 dk] → Geçiş kapısı → [Kısa kamera reveal] → Toplu savaş başlar
```

- Tutorial sessiz, müziksiz ya da hafif ambient.
- Kapıdan geçince savaş müziği başlar (`Kutun/Audio/Music`).
- Savaş bittikten sonra ambience geri döner.

---

## 5. Edge Cases

| Durum | Beklenen davranış |
|-------|-------------------|
| Oyuncu tutorial'ı bitirmeden Bölge C'ye geçerse | Düşmanlar yine de aktive olur — tutorial tamamlanmış sayılır |
| Düşman tutorial koridoruna girerse | Olmamalı; kapı geçiş trigger'ı AI'ı yalnızca Bölge C içinde aktive etmeli |
| Oyuncu tutorial sırasında ölürse | Normal respawn (`WBP_Restart`), trigger durumları sıfırlanmamalı (`bTriggerOnce = true`) |
| Fırlatılan nesne kapı geçiş trigger'ını erken tetiklerse | Trigger sadece `BP_Telekinezi` overlap'ine tepki vermeli (`ActorClass` filtresi) |
| Tüm düşmanlar öldürüldükten sonra bir düşman hâlâ hayatta kalırsa | `BP_DeathZone` yedek olarak devreye girer |

---

## 6. Bağımlılıklar

| Sistem | Notlar |
|--------|--------|
| `BP_TutorialTrigger` | Zaten `Stand_Arena`'da örnekler mevcut |
| `BP_Enemy` (Mongol, Bizans) | `Kutun/Characters/Enemies` altında mevcut |
| `UC_HealthComponent` | Düşman ölüm yolu |
| `BP_DeathZone` | Zaten arenada bir örnek var (z ~= -2500) |
| Savaş müziği | `Kutun/Audio/Music` — hangi track kullanılacak belirlenmeli |

---

## 6. Tuning Knobs

| Parametre | Şu anki değer | Açıklama |
|-----------|--------------|----------|
| Düşman sayısı | ~12-13 | Zor hissettirmeli ama bunaltmamalı |
| AI aktive mesafesi | Kapı geçişi | Trigger box ile kontrol |
| Tutorial adım sayısı | 5 | Uzun sürerse sıkıcı; kesilebilir |
| Kapı reveal kamera süresi | ~2 sn | Çok uzun sürerse tempo kırılır |

---

## 7. Kabul Kriterleri

- [ ] Tutorial'da her adım doğru sırayla tetikleniyor, önceki kapanmadan sonraki açılmıyor
- [ ] `PlayerStart`'ın üzerinde trigger yok (spawn anında patlamamalı)
- [ ] Kapıdan geçince tüm Bizans + Mongol düşmanları aktive oluyor
- [ ] Hiçbir düşman tutorial bölgesine girmeden önce aktive olmuyor
- [ ] Oyuncu arenadan dışarı çıkarsa `BP_DeathZone` yakalıyor

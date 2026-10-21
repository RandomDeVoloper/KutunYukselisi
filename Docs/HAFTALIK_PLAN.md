# Toygard — Haftalık Sprint Planı
**20–26 Ekim 2026**

---

## Özet

| Gün | Odak |
|-----|------|
| Pazartesi | Blueprint denetimi — ölçüm ve haritalama |
| Salı | Teknik borç belgesi + core loop diyagramı |
| Çarşamba | BP_Enemy düzeltmeleri (CameraBoom, LoopAttacking) |
| Perşembe | Duplicate kod → fonksiyon refactor |
| Cuma | Hard ref → Soft ref dönüşümü |
| Cumartesi | Prototip build testi + playtest notları |
| Pazar | Retrospektif + sonraki sprint planlaması |

---

## Pazartesi — Blueprint Denetimi

**Dev:**
- [ ] BP_Telekinezi node sayısı ölç
- [ ] BP_Enemy hard ref ve component taraması
- [ ] UC_HealthComponent bağımsızlık kontrolü
- [ ] BP_Axe ölü node temizliği
- [ ] `Docs/BLUEPRINT_DENETIMI.md` bulgularla güncelle

**Tasarım:**
- [ ] GDD draft tamamla (pitch + core loop + MoSCoW)
- [ ] Oyuncu fantazisini netleştir

**Sanat:**
- [ ] Silah prop listesi çıkar (SM_Sword, SM_Axe, SM_Spear)
- [ ] Eksik texture rolleri tespit et

---

## Salı — Teknik Borç + Diyagram

**Dev:**
- [ ] BP denetim bulgularını önceliklendir (Kritik / Yüksek / Orta)
- [ ] `TOYGARD_GDD.md` Teknik Borç tablosunu doldur
- [ ] Alfa öncesi fix listesini belirle

**Tasarım:**
- [ ] Core loop flowchart'ını Milanote'a aktar
- [ ] Düşman davranış tablosu (Agro range, saldırı çeşidi)

**Sanat:**
- [ ] Düşman görsel referans kiti (Moğol, Bizans, Çin)
- [ ] Mevcut texture kalitesi puanla

---

## Çarşamba — BP_Enemy Düzeltmeleri

**Dev:**
- [ ] `BP_Enemy`: CameraBoom component sil (editor'da)
- [ ] `BP_Enemy`: LoopAttacking timer doğrula / düzelt
- [ ] `BP_Enemy`: Die → bIsDead guard var mı kontrol et
- [ ] Compile + PIE test → düşman ölümü çalışıyor mu?

---

## Perşembe — Refactor

**Dev:**
- [ ] `BP_Telekinezi`: Tekrarlayan highlight chain → tek fonksiyon
- [ ] Yeni fonksiyon BP_Telekinezi:EventGraph'a wire et
- [ ] `write_graph_dsl` değil, Function graph kullan (MCP kısıtlaması)
- [ ] Compile + test

---

## Cuma — Hard Ref → Soft Ref

**Dev:**
- [ ] BP_Telekinezi hard texture referansları → TSoftObjectPtr
- [ ] BP_Enemy animasyon montage → Async Load Blueprint
- [ ] Önce/sonra Size Map ekran görüntüsü karşılaştırması

---

## Cumartesi — Build Test

**Dev:**
- [ ] L_Tutorial_New'de tam oynanış testi
- [ ] Stand Modu (Oba_L) 3 dalga tamamlanabiliyor mu?
- [ ] Bilinen crash/bug listesi

**Tasarım:**
- [ ] Playtest notları (ilk 5 dakika deneyimi)
- [ ] Tutorial prompt metinleri yeterli mi?

**Sanat:**
- [ ] Build için eksik asset listesi
- [ ] Placeholder mı, final mı? — her asset için etiketle

---

## Pazar — Retrospektif

- [ ] Bu hafta tamamlananlar / tamamlanamayanlар
- [ ] Sonraki sprint için taşınanlar
- [ ] Sprint 2 odak alanı belirle (Kılıç sörfü? Düşman çeşidi? Save sistemi?)

---

## Linkler

- [GDD](TOYGARD_GDD.md)
- [Blueprint Denetim Planı](BLUEPRINT_DENETIMI.md)
- [Stand Mode Notları](../STAND_MODE_PROGRESS.md)

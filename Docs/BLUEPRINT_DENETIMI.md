# Blueprint Denetimi — Görev Listesi

**Tarih:** 20 Ekim 2026 (Pazartesi)
**Ajan:** Dev (Lead Developer)
**Tahmini Süre:** ~85 dakika

---

## Faz 1 — Hazırlık (~10 dk)

- [ ] **Editörü aç** — tek UE5Editor.exe instance olduğunu doğrula (Task Manager)
- [ ] **Size Map plugin'ini aç** — `Tools → Size Map`

---

## Faz 2 — Ana Blueprint'leri Tara (~40 dk)

### BP_Telekinezi
- [ ] EventGraph açık → `Ctrl+A` → node sayısını not al (hedef: < 150)
- [ ] Size Map'te BP_Telekinezi'yi bul → hard referansları listele
- [ ] `MATERIALCHANGE` kollapslı graph'ı bul → içini `find_nodes` ile listele
- [ ] Tekrarlayan highlight chain'leri işaretle (CLAUDE.md: 2 adet var)
- [ ] `Return Value Rotation` vs `Return__Value__Rotation` — kopya temizlendi mi doğrula

### BP_Enemy
- [ ] Components paneli → **CameraBoom var mı?** (oyuncudan kopya — silinmeli)
- [ ] EventGraph → node sayısını not al (hedef: < 100)
- [ ] `LoopAttacking` fonksiyonu → timer looping=true mi? bIsDead guard var mı?
- [ ] `Die` custom event → OnDepleted pin kopuk değil mi?
- [ ] Size Map → hangi animasyon assetlerini hard çekiyor?

### UC_HealthComponent
- [ ] Reference Viewer → kimler bu component'e referans veriyor?
- [ ] BeginPlay → oyuncu kontrolü yapılıyor mu?
- [ ] OnDepleted delegate → BP_Enemy Die'da bağlantı sağlam mı?

### BP_Axe
- [ ] EventGraph → `Ctrl+A` → başlangıç node sayısı
- [ ] `Find Unreferenced Nodes` → ölü node'ları seç ve sil
- [ ] Silme sonrası node sayısını tekrar ölç

---

## Faz 3 — Hard Referans Haritası (~20 dk)

- [ ] BP_Telekinezi → Reference Viewer (Depth: 2) → hard ref listesi çıkar
- [ ] BP_Enemy → Reference Viewer → AnimMontage soft mu, hard mı?
- [ ] Kritik bulgular: Hard + büyük asset → Soft Reference'a çevrilecekler listesi
- [ ] Duplicate kod blokları → 2+ yerde aynı zincir varsa fonksiyon adayı olarak işaretle

---

## Faz 4 — Teknik Borç Belgesi (~15 dk)

- [ ] `TOYGARD_GDD.md` → Teknik Borç tablosunu bulgularla güncelle
- [ ] Alfa öncesi kritik / Beta'ya bırakılabilir / İzle olarak kategorize et
- [ ] Commit: `docs: blueprint denetimi bulguları eklendi`

---

## Bilinen Sorunlar (Denetim öncesi)

Bunlar CLAUDE.md ve STAND_MODE_PROGRESS.md'den alınan mevcut borçlar:

| Sorun | Kaynak | Durum |
|-------|--------|-------|
| BP_Enemy'de CameraBoom var (oyuncudan kopya) | CLAUDE.md | Onaylanmamış |
| BP_Telekinezi EventGraph'ta MCP cycle hatası | CLAUDE.md | Aktif kısıtlama |
| MATERIALCHANGE kollapslı graph okunmuyor | CLAUDE.md | Aktif kısıtlama |
| BP_Axe'de ~323 ölü node birikmiş | CLAUDE.md | Temizlenmedi |
| UC_HealthComponent OnDepleted pin riski | STAND_MODE | Doğrulanmadı |

---

## MCP Araçları (Editör açıkken kullanılabilir)

```
# Graph okuma (read-only, güvenli)
find_nodes       → bir graph'taki node'ları listele
get_node_infos   → seçilen node'ların detayını al
get_properties   → component property'lerini oku
get_referencers  → bir asset'e kimlerin referans verdiğini bul

# Yazma (onay gerektirir)
set_properties   → property değeri yaz
write_graph_dsl  → graph yeniden yaz (dikkatli kullan)
delete_node      → node sil
```

> **Not:** `read_graph_dsl` BP_Telekinezi:EventGraph'ta çalışmıyor ("Cycle detected").
> Kollapslı (composite) graph'larda `create_node` ve `find_node_types` başarısız olur.
> Yeni mantık için EventGraph'a kollapslı graph içine değil, ayrı bir Function graph'a ekle.

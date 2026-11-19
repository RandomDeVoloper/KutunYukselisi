# Codex Yapılacaklar Listesi — 2026-11-19

Bu dosya `Toygard` (repo: KutunYukselisi) için Codex'in sırayla devralabileceği
görev listesidir. Her görev: **Neden** (sorun) → **Kabul kriteri** (bitti sayılma
şartı) → **Dokunulacak yer** biçiminde yazıldı.

## ÖNCE BUNU OKU

- Proje **Blueprint-only** UE 5.8. `Source/` ve C++ modülü **yok**.
- `.uasset` / `.umap` dosyalarını metin olarak okuyamaz/düzenleyemezsin, diff de alamazsın.
  Hook'lar `Edit(**/*.uasset)` ve `Edit(**/*.umap)` çağrılarını reddeder.
- Blueprint değiştirmenin tek yolu: **Unreal Editor açıkken** `unreal-mcp`
  (`http://127.0.0.1:8000/mcp`). Editör kapalıysa `ECONNREFUSED`.
- MCP tuzaklarının tam listesi repo kökündeki `CLAUDE.md` → "Workflow notes
  (learned the hard way)" başlığında. Oraya bakmadan iş yapma.
- Editör açıkken **branch değiştirme**. Metin olarak düzenlenebilenler:
  `Config/*.ini`, `Docs/*.md`, `.claude/`, `project.yaml`.
- Çalışma protokolü: Soru → Seçenek → Karar → Taslak → Onay. Dosya yazmadan önce
  kullanıcıya sor (`Docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`).
- Oyuncu-gözlemlenebilir her değişiklik PIE/Standalone'da **çalıştırılıp**
  ekran görüntüsü `production/qa/evidence/` altına bırakılır. Parse kontrolü run sayılmaz.

---

## ÖNCELİK 1 — Hasar geri bildirimi (en acil, mevcut bug)

### T1.1 — Düşmanlara health bar ekle

**Neden:** Düşmana hasar verip veremediğimiz anlaşılmıyor. Oyuncu kılıcı düşmanın
içinde dolaştırdığında hiçbir görsel/işitsel tepki yok, bu yüzden "hasar vermiyor"
hissi doğuyor. Bu önce bir **feedback** problemi, sonra bir collision problemi.

**Yapılacak:**
1. `Kutun/UI/Widgets/` altında `WBP_EnemyHealthBar` oluştur: ince progress bar,
   `Docs/UI_PALETTE.md` paletine uyumlu (Kut Altını dolgu, Gece Mavisi zemin).
2. `BP_Enemy` üzerine bir `WidgetComponent` ekle (Screen space, kafanın ~20 cm üstü,
   `DrawSize` ~120x12).
3. `UC_HealthComponent`'in hasar/ölüm yoluna bağla — **yeni bir sağlık sistemi
   kurma**, mevcut component tek kaynak olmalı.
4. Görünürlük kuralı: tam sağlıkta ve hasar almadan 3 sn geçince gizle; hasar
   alınca göster. Ölümde gizle.

**Kabul kriteri:** Kılıçla/baltayla/fırlatmayla vurulan düşmanın barı anında düşüyor;
Standalone'da çekilmiş ekran görüntüsü `production/qa/evidence/` altında.

**Dokunulacak:** `Kutun/Characters/Enemies/Base/BP_Enemy`,
`Kutun/Core/Components/UC_HealthComponent`, yeni `WBP_EnemyHealthBar`.

### T1.2 — Vuruş anı geri bildirimi (hit feedback)

**Neden:** Bar tek başına yetmez; vuruşun "oturduğu" anlaşılmalı.

**Yapılacak:** Hasar anında hasar sayısı / flash materyali / kısa hit-stop + ses.
`game-feel` skill'ini ve mevcut `ApplyHitFeedback` + `CS_Crush` yapısını kullan.

**Kabul kriteri:** Vuruş sırasında en az iki kanal (görsel + ses) tepki veriyor.

### T1.3 — Kılıç collision/hasar bug'ını çöz

**Neden:** Bilinen açık bug: büyütülmüş kılıcın collision'ı ıskalıyor,
`SetTimerByEvent` global bir hit-lock yaratıyor (bir düşmana vurunca diğerleri
kilitleniyor), görsel feedback yok.

**Yapılacak:**
1. Hit-lock'u **aktör başına** yap (global timer yerine `DamagedActors` benzeri
   per-actor set + süre).
2. Scale değişince collision kapsamının güncellendiğini doğrula (sweep/trace
   yarıçapı scale ile çarpılmalı).
3. T1.1'in barını kullanarak regresyonu gözle doğrula.

**Kabul kriteri:** Büyütülmüş kılıçla üst üste üç düşmana vurulduğunda üçünün de
barı düşüyor.

**Dokunulacak:** `Kutun/Weapons/Sword/BP_Sword`, `BP_Throwable`.

---

## ÖNCELİK 2 — Tutorial eksikleri

Mevcut tutorial sistemi: `Kutun/Gameplay/BP_TutorialTrigger` örnekleri +
`WBP_TutorialPrompt` + `WBP_TutorialControls`. Sıra `TutorialOrder` ile veriliyor,
ders ayarları `Tools/TutorialFlow/lessons.json`'da. Durum: `Docs/TUTORIAL_PROGRESS.md`.
**Level Blueprint'e ders ekleme** — yeni bir trigger instance'ı yerleştir.

### T2.1 — Balta ile düşman öldürme dersi

**Neden:** Oyuncu baltanın bir silah olduğunu öğrenmiyor.

**Yapılacak:** Yeni `BP_TutorialTrigger` instance'ı; tamamlanma şartı = baltayla
bir düşmanın ölmesi. Mevcut ders sırasına (`TutorialOrder`) fırlatma pratiğinden
sonra gir. Kontrol ipucu panelinde balta tuşu görünsün.

**Kabul kriteri:** Ders yalnızca baltayla gerçekleşen bir ölümde tamamlanıyor;
zaman aşımında ilk adımdan tekrar başlıyor.

### T2.2 — X / Y / Z eksen kilitleme dersi

**Neden:** Eksen maskeleme (X/Y/Z tuşları) oyunun en gizli mekaniği; kimse bulamıyor.

**Yapılacak:** Ölçekleme dersinden **sonra** gelen iki adımlı bir ders:
(1) bir eksen kapat, (2) kapalı eksende ölçekleme olmadığını gör.
`WBP_HudGrab`'ın `HB_Axes` göstergesine (Txt_X/Y/Z opaklığı) dikkat çek.
Ezme (crush) için **Y ekseninin açık olması gerektiğini** açıkça söyle.

**Kabul kriteri:** `bScaleAxisX/Y/Z` bayraklarından biri değişince adım 1 tamamlanıyor.

### T2.3 — Uzuv kesme dersi

**Neden:** Uzuv kesme sistemi var ama oyuncuya hiç gösterilmiyor.

**Önce oku:** `Docs/UZUV_KESME_DEVIR_20261118.md`. Dikkat: o dokümandaki
`BP_DismembermentRegression` test aktörü ana haritadan kaldırıldı — **geri koyma**,
BeginPlay'de düşman öldürüyordu.

**Yapılacak:** Düşmanın uzvunun kesilebildiğini gösteren bir ders; tamamlanma
şartı = bir uzvun kopması.

**Kabul kriteri:** Kesilen uzuv görünür şekilde ayrılıyor, ders tamamlanıyor,
ekran görüntüsü kanıt olarak saklanıyor.

---

## ÖNCELİK 3 — Hikâye temeli (tasarım işi, kod yok)

Bu üç görev **doküman** üretir, Blueprint değiştirmez. Önce `/brainstorm` ile
seçenek çıkar, kullanıcıyla karar ver, sonra yaz. Mevcut tasarım kaydı:
`Docs/TOYGARD_GDD.md`.

### T3.1 — "Neden?" — temel motivasyon

**Yapılacak:** Oyuncunun kim olduğu, telekinezi/kılıç gücünü nereden aldığı ve
neyi durdurmaya çalıştığına dair tek sayfalık bir çekirdek. En az 3 alternatif
sun, kullanıcı seçsin. Mevcut Türk/Göktürk temasına (Kutun, Uldiz, Balbal, Oba)
yabancı bir şey uydurma.

**Kabul kriteri:** `Docs/TOYGARD_GDD.md` içine yazılmış, onaylanmış tek bir premise.

### T3.2 — Arena ve heykellerin hikâyeye katkısı

**Neden:** `Stand_Arena`'da heykeller (Balbal) var ama anlatıya bağlı değil.

**Yapılacak:** Balbalların ne olduğu (atalar? hapsedilmiş ruhlar? güç kaynağı?),
arenada **ne olacağı** (kimle dövüşüyoruz, neden burada) ve bunun mekaniklerle
nasıl bağlandığı. Mevcut `BP_Soul`, `BP_Balbal`, `BP_Balbals` aktörlerini kullan —
hikâye zaten orada duran şeyleri açıklasın.

**Kabul kriteri:** Her heykel/alan için tek cümlelik bir anlatı işlevi listesi.

### T3.3 — Çevresel anlatım geçişi

**Yapılacak:** T3.1/T3.2 kararlarını oyuncunun göreceği şeye çevir: tutorial
metinleri, menü yazıları, arenaya giriş anı. Yeni sistem yazma, var olan
`BP_TutorialTrigger` metinlerini ve `L_Main3DMenu`'yu kullan.

---

## ÖNCELİK 4 — Vertical slice'ı oturtmak

### T4.1 — Vertical slice kapsamını yaz

**Yapılacak:** `/vertical-slice` skill'ini çalıştır. Çıktı: başı-sonu belli,
5–10 dakikalık tek bir oynanış dilimi — giriş, tutorial, arena dövüşü, kapanış.
Neyin **dahil olmadığını** da yaz.

**Kabul kriteri:** Onaylanmış kapsam dokümanı + eksik işlerin listesi.

### T4.2 — Boşluk analizi

**Yapılacak:** T4.1'in kapsamını mevcut duruma karşı denetle
(`/project-stage-detect` ve `/gate-check`). T1–T3 görevlerinin hangilerinin slice
için **zorunlu**, hangilerinin "sonra" olduğunu işaretle.

### T4.3 — Uçtan uca oynanış doğrulaması

**Yapılacak:** Slice'ı Standalone'da (PIE değil — Escape PIE'yi kapatıyor,
duraklatma menüsü test edilemiyor) baştan sona oyna. Her kopma noktasını
`/playtest-report` ile rapora yaz.

**Kabul kriteri:** Tek bir oturumda sıkışmadan baştan sona gidilebiliyor;
ekran görüntüleri `production/qa/evidence/` altında.

---

## Çalışma sırası önerisi

1. T1.3 → T1.1 → T1.2 (hasar hissini düzelt; bu olmadan dövüş test edilemez)
2. T3.1 → T3.2 (hikâye çekirdeği; tutorial metinleri buna dayanıyor)
3. T2.1 → T2.2 → T2.3 (tutorial dersleri)
4. T4.1 → T4.2 → T4.3 (slice'ı kapat)

Her görev kendi commit'ini alır (binary asset'ler merge edilemez — branch başına
tek değişiklik seti). Commit mesajı Conventional Commits: `feat:`, `fix:`, `docs:`.

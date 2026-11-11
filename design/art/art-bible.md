# Art Bible: Toygard

> **Status**: Draft
> **Owned By**: art-director
> **Last Updated**: 2026-11-11
> **Art Director Sign-Off (AD-ART-BIBLE)**: SKIPPED 2026-11-11 — solo mode

## 1. Visual Identity Statement

**Tek Satır Görsel Kural**

> Her görsel unsur ya Kut'un varlığını hissettirir ya da düşmanın yokluğunu hazırlar; ikisi arasında kalan hiçbir şeyin ekranda yeri yoktur.

**Destekleyici Prensipler**

**1. Kutsal Kontrast** — Işık kaynaklardan değil, Kut'tan gelir.
- **Tasarım testi:** Karanlık/aydınlık kararı belirsizleştiğinde → oyuncu veya aktif silah yakındaysa aydınlat, değilse karanlığı koru. Ortam ışığı pasif, Kut enerjisi aktif ışık kaynağıdır.
- **Hizmet:** "Kut'u ellerinde tutan efsane kahraman" fantazisi; oyuncunun her sahneye hakim hissi.

**2. Kasıtlı Yalınlık** — Her objede okunabilir silüet, en fazla iki malzeme katmanı.
- **Tasarım testi:** Asset veya UI paneli karmaşıklık kararı belirsizleştiğinde → 50px thumbnail'da tanınabiliyorsa devam et, tanınamıyorsa detay düşür. Meshy low-poly budgeti avantajdır, engel değil.
- **Hizmet:** Telekinezi ve ölçeklendirme mekaniği — hedefin anında tanınması hem gameplay hem estetik gereksinimi.

**3. Türk-Bozkır Renk Önceliği** — Altın, kızıl toprak ve gece mavisi ana renk üçgenidir.
- **Tasarım testi:** Yeni renk eklenmesi belirsizleştiğinde → `(0.823, 0.701, 0.479)` altın, `(0.445, 0.042, 0.016)` kızıl veya koyu lacivert grubuna giriyorsa onayla; girmiyor ve Kut enerjisini veya tehlikeyi temsil etmiyorsa reddet.
- **Hizmet:** Türk mitolojisi özgünlüğü; Moğol/Bizans/Çin düşman varyantlarında kültürel ayrışma.

## 2. Mood & Atmosphere

**Ana Menü**
- Duygu hedefi: Büyüklük öncesi sessizlik; "bu hikaye başlamadan seni bekliyor"
- Işıklandırma: Gece-mavi ortam (2800 K), tek altın ışık ekseni yukarıdan çapraz; alacakaranlık / ay ışığı yönü
- Atmosferik sıfatlar: anıtsal, dingin, gerilimli, kadim, beklentili
- Enerji seviyesi: derin

**Keşif / Yürüyüş**
- Duygu hedefi: Sahiplenme; düşmanlar gelmeden önce alanı okuyan kahraman hissi
- Işıklandırma: Sıcak bozkır güneşi (4800–5500 K), uzun gölgeler yatay açıdan; renk sıcaklığı mesafede soğuyor
- Atmosferik sıfatlar: açık, uyanık, sessiz-tehditkar, uçsuz, nefes alan
- Enerji seviyesi: ölçülü

**Savaş**
- Duygu hedefi: Tanrısal kontrol; kaos içinde hakim olma egzaltasyonu
- Işıklandırma: Kut enerjisi birincil ışık kaynağı (altın-amber, 3200 K); ortam maviye kayıyor; yüksek kontrast; trail efektleri sahneyi her kare yeniden çerçeveler
- Atmosferik sıfatlar: şiddetli, parıltılı, ritimli, dramatik, ezici
- Enerji seviyesi: çılgın

**Ölüm / Restart**
- Duygu hedefi: Kayıp ve yeniden doğuş arasındaki an; teslim değil, duraksamak
- Işıklandırma: Desatürasyon (%20–30 renk doygunluğu), soğuk kül-mavi (1800–2200 K); vignette koyulaşır; Kut enerjisi söner
- Atmosferik sıfatlar: sessiz, donuk, boş, ağır, geçici
- Enerji seviyesi: derin (en düşük enerji noktası)

**Zafer**
- Duygu hedefi: Kut'un tam gerçekleşmesi; figürün mitosu
- Işıklandırma: Altın saat (3600 K), yukarıdan ışık sütunu oyuncuyu vurgular; en yüksek parlaklık bütçesi bu duruma ayrılır
- Atmosferik sıfatlar: görkemli, kazanılmış, parlayan, yükselişli, hatırlanan
- Enerji seviyesi: ölçülü → derin (patlama sonrası yerleşme)

**Tutarlılık Notu:** Her durum için "Kut varlığı = ışık, Kut yokluğu = soğuk ve karanlık" kuralı korunur. Ölüm tek istisna — Kut'un sönmesi görsel dili kırar, bu kırılma kasıtlıdır.

## 3. Shape Language

**Oyuncu Karakter Silüet Felsefesi**
- Tanımlayıcı özellik: geniş omuz-dar bel oranı + başın üzerinde yükselen enerji alanı (ItadoriAura); bu iki unsur 50px thumbnail'da kaybolmaz
- Kol pozisyonu: telekinezi aktifken asimetrik duruş (bir kol öne uzanmış); simetrik durma "güçsüz" okunur
- Silüet testi: karakter beyaz dolgu, zemin siyah — siluet tek başına "telekinetik savaşçı" mı söylüyor? Hayır ise kostüm/rig revizyonu
- Uçan/süzülen kılıç her zaman karakterin çevresinde; silüetin parçasıdır, ayrı prop gibi okunmamalı

**Environment Geometrisi**
- Bozkır ve dış alan: açısal — yatay yatık kayalar, belirgin horizon çizgisi, diagonal kaya kesitleri; organiklik yalnızca bitki örtüsünde
- Mağara ve iç mekan: organik + açısal melezi — tavan organik (doğal), duvar ve zemin açısal (insan eliyle)
- Düşman yapıları: keskin açılı, dikey ağırlıklı; kültüre göre ayrışır: Moğol → konik; Bizans → yay ve kubbe; Çin → çatı kıvrımı
- Genel kural: 60° ve 90° tercihli; 45°lik diagonal kullanım dramatik anlara saklanır (kılıç çizgisi, kamera açısı)

**UI Şekil Grameri**
- Köşeli clip-path çerçeveler (Türk geometrik motiflerinden soyutlanmış), düz çizgi kenarlar
- Paneller tam dikdörtgen değil — tek köşe kırpılmış; okunabilirlik kaybetmeden dünya hissini taşır
- **Yuvarlak hiç kullanılmaz** — bozkır estetiğinde yuvarlaklık yumuşaklık/zayıflık okur
- Diegetic HUD: sağlık göstergesi karakterin Kut enerjisi parıltısıyla görsel bağ kurar; can düştükçe aura rengi soluklaşır

**Kahraman Şekilleri vs. Destekleyici Şekiller**
- Kahraman şekiller: dikey ve V-formu (omuz genişliği, yükselen enerji); altın renk grubuyla çalışır; keskin kenar + parlak merkez
- Destekleyici şekiller (çevre, prop): yatay ve kütle; nötr-sıcak renk grubu; mat yüzey
- Düşman şekilleri: ters-V veya konik (tepe ağır, taban dar) → dengesizlik ve tehdit; kızıl veya soğuk renk grubuyla çalışır
- Kural: Kahraman ve düşman siluetleri aynı sahne karesi içinde çakışmamalı

## 4. Color System

**Ana Palet (7 renk)**

| İsim | sRGB | Bu Evrende Anlamı |
|------|------|-------------------|
| Kut Altını | `(0.823, 0.701, 0.479)` | Kutsal güç, oyuncu enerjisi, aktif mekanik durumu |
| Kut Parlağı | `(1.000, 0.920, 0.700)` | Kritik etki anı, zafer patlaması, maksimum güç |
| Bozkır Kızılı | `(0.445, 0.042, 0.016)` | Tehlike, düşman enerjisi, sağlık kaybı uyarısı |
| Gece Mavisi | `(0.055, 0.082, 0.180)` | Çevre ortamı, Kut yokluğu, ölüm durumu |
| Küllü Beyaz | `(0.820, 0.800, 0.760)` | Nötr UI yüzeyi, okuma için zemin, ikincil metin |
| Toprak Kahvesi | `(0.310, 0.200, 0.120)` | Ortam prop malzeme, zemin dokusu |
| Sönük Çelik | `(0.250, 0.270, 0.310)` | Düşman zırhı, metalik nötr, tehdidin malzeme dili |

**Semantik Renk Kullanımı**
- Altın → yalnızca oyuncu veya oyuncunun aktif kontrolündeki nesne; ortamda altın varsa Kut'la bağlantılı olmalı
- Kızıl → tehlike ve düşman; UI'da "yanlış eylem / hasar alma"; hiçbir çevresel unsur kızıl kullanmaz
- Gece mavisi → pasif ortam, oyuncunun olmadığı yer, ölüm ekranı; Kut geldiğinde mavi geri çekilir
- Küllü beyaz → yalnızca UI ve diegetic prompt; sahnede beyaz nesne olmamalı
- Toprak kahvesi → ortam; oyuncu veya UI'ya dokunmaz
- Sönük çelik → düşman malzeme dili; oyuncu üzerinde kullanılmaz

**Alan Başına Renk Sıcaklığı Kuralları**
- Arena / Dış savaş alanı: sıcak-nötr taban (4500–5000 K) + altın accent; mavi yalnızca gökyüzü uzağında
- Mağara / İç mekan: soğuk taban (2000–2800 K); "mağaranın kendi ışığı yoktur" kuralı; Kut kaynağı aktifse altın nokta ışık kontrastı
- Ana Menü: gece mavisi hakim (1800–2500 K), tek altın accent; sıcak renk yalnızca etkileşimli öğelere
- Zafer / Kesme sahneleri: altın saat paleti (3400–3800 K); mavi sadece uzak arka plana sıkışır

**UI Paleti — Dünya Paletinden Ayrılan Noktalar**
- Birincil: Kut Altını + Küllü Beyaz
- Hover: Kut Altını → Bozkır Kızılı (mevcut teknik veride onaylı)
- Arka plan paneli: Gece Mavisi %75 opasite
- UI hiçbir zaman Toprak Kahvesi veya Sönük Çelik kullanmaz — bu renkler dünyaya aittir

**Renk Körlüğü Güvenliği**

| Semantik Renk | Risk | Yedek Destek |
|---|---|---|
| Bozkır Kızılı (tehlike) | YÜKSEK — kırmızı körü altınla karıştırır | Kalın kenar + uyarı ikonu (ünlem veya kılıç kırığı) zorunlu |
| Kut Altını (aktif güç) | ORTA — sarı-kahve grubuna kayar | Parlaklık farkı korunursa yeterli; trail animasyonu ek ipucu |
| Gece Mavisi (ölüm) | DÜŞÜK — mavi körlük nadirdir | Desatürasyon efekti ana ipucu |
| Kut Parlağı (zafer) | DÜŞÜK | Yüksek parlaklık körlükten bağımsız okunur |

**Kural:** Bozkır Kızılının taşıdığı hiçbir kritik bilgi renk dışında görsel ipucu olmadan iletilmez. Sağlık barı için ikon + şekil değişimi zorunludur.

## 5. Character Design Direction

### 5.1 Oyuncu Karakter Görsel Arketipi

**Kültürel kaynak:** Türk-Bozkır şamanı (Kam) — ruhani otorite ve savaşçı kimliği tek bedende. Referans: Göktürk taş heykelleri (balbal) ve kaya sanatındaki geyikli savaşçı siluetleri. Bizans zırhı veya Çin akrobatizmi kasıtlı ayrım — bunlar düşmana aittir.

**Güç düzeyi sinyali:** Hafif ama dikey; Kut yer çekimini ikincil yapar. Kumaş katmanları rüzgarda yaşar; zırhın olmadığı yerler güçsüzlük değil koruma kanıtı. ItadoriAura figürün taç çizgisini uzatır.

**50 piksel thumbnail'da korunması gereken 3 unsur (öncelik sırasıyla):**
1. V-omuz genişliği
2. Başın üzerindeki altın enerji tepesi
3. Uçan kılıcın yörüngesi

### 5.2 Düşman / NPC / Müttefik Ayırt Etme Kuralları

**Katman 1 — Silüet (0–10 kare):**
- Oyuncu: dikey + V + tepede enerji çıkıntısı
- Düşman: ters-V veya konik; varyasyonlar: Moğol → geniş kürkten konik sivri başlık; Bizans → yay şekilli miğfer; Çin → uzun mızrak ucunun zirveye çıktığı ince dikey

**Katman 2 — Renk grubu (100ms):**
- Oyuncu: Kut Altını dominant
- Düşman: Bozkır Kızılı veya Sönük Çelik dominant; kültüre göre accent: Moğol → koyu bordo; Bizans → mor-gri; Çin → soluk jade-gri
- NPC / tarafsız: Toprak Kahvesi dominant; anlatı kritik NPC'lerde tek altın accent detay

**Katman 3 — Hareket dili (ilk 3 saniye):**
- Oyuncu: akıcı ve asimetrik; telekinezi aktifken kol uzanır
- Düşman: ağır ve köklenmiş; birden patlar — tehdidin her zaman birikme fazı vardır

**Kural:** Renk körü bir oyuncu bile silüet farkından, hareketlilik farkından düşmanı tanımalıdır.

### 5.3 İfade ve Poz Stili

**Ton:** Dramatik-gerçekçi. Göktürk heykellerinin sessiz ağırlığı + Türk minyatürlerinin yoğun dinamizmi.

- **Dinlenme pozu:** Hafif hazır duruş; "tamamen rahat" anı yoktur — Kut her zaman biraz canlıdır
- **Savaş pozu:** Açık göğüs, kol uzanmış veya kılıca yönelmiş; kontrol mesafeden okunmalı
- **Zafer/duraksaması:** Figür dikeydir, kılıç çevrede süzülür; figür hiçbir zaman eğilmez veya çökmez
- **Poz testi:** "Bu poz Kam'ın kontrolde mi yoksa kontrolden çıkmış mı gösteriyor?" — kontrolde ise onayla

### 5.4 LOD Felsefesi

| Mesafe | Korunan Detay | Düşen Detay |
|--------|---------------|-------------|
| 0–200 ü. (yakın) | Kumaş kıvrım gölgesi, Kut parıltı detayı | 2048→1024 güvenli |
| 200–500 ü. (orta) | Silüet kesin, renk grubu okunabilir | Yüz detayı, dikiş/perçin geometrisi |
| 500–1000 ü. (uzak) | V-silüet ve enerji tepesi — bunlar son düşen | Kumaş simülasyonu dondurulabilir |
| 1000+ ü. (çok uzak) | Yalnızca siluet ve dominant renk | Tüm yüzey detayı |

**Düşman ek kural:** Aktif savaştaki düşman (`bIsEngaging`) hiçbir zaman LOD-2'ye geçmez.

## 6. Environment Design Language

### 6.1 Mimari Stil ve Kültürel İlişki

**Oyuncu alanı — bozkır mimarisi:**
- İnsan eli yoksa hiçbir şey inşa edilmemiştir; doğal jeoloji hakimdir
- İnsan eli varsa: Türk-Göktürk stilinde taş temel + ahşap çatı; süsleme minimumda, fonksiyon önce
- Yüzey grameri: kaba taş dokusu + toprak sıva; oyma varsa geometrik, figüratif değil
- Referans form: Orhun bölgesi balbal dizileri ve erken Türk kaya mezarlarının form ekonomisi

**Düşman alanları — kültürel ayrışma:**
- Moğol: çadır formu dominant (konik çatı); deri ve kemik malzeme dili
- Bizans: taş kemer ve sütun; yüzey işleme ve mozaik parıltısı; dikey oran
- Çin: çatı kıvrımı + koyu ahşap + kırmızı-siyah accent; kapı geçişlerinde güçlü çerçeveleme

### 6.2 Doku Felsefesi

PBR "doğruluk" için değil "okunabilirlik" için kullanılır:

1. **Roughness yüksek:** Ortam normu 0.6–0.9. Parlak yüzey = Kut varlığı veya düşman metalik zırhı; başka hiçbir şey parlamaz.
2. **Albedo doygunluğu kısıtlı:** Toprak, kaya, ahşap → Saturation %15–35. Kut nesneleri dışında ortam "canlı" renk taşımaz.
3. **Normal map derinliği mesafeyle uyumlu:** Yakın nesne → yüksek frekans; uzak ortam → macro form baskın.
4. **Stylized yalnızca Kut materyallerinde:** ItadoriAura, kılıç trail, highlight shader — fiziksel olarak imkansız parlaklık burada mantıklıdır çünkü Kut'un dünyaya müdahalesidir.

### 6.3 Prop Yoğunluğu Kuralları

| Alan Tipi | Yoğunluk | Neden |
|-----------|----------|-------|
| Savaş alanı (açık) | Seyrek; 10m çaplı hareket alanları boş | Fırlatılabilir nesne anında okunabilmeli |
| Keşif koridoru | Orta — 2–3 prop kümesi, aralarında açıklık | Yönlendirme + görsel nefes |
| Hikaye geçiş alanı | Orta-yoğun | Oyuncuyu kasıtlı yavaşlatır |
| Mağara / iç mekan | Doku yoğun, geometri seyrek | Yüzey dokusu mekan hissini verir |
| Düşman kamp alanı | Yoğun | "Bu topraklar düşmanın" mesajı |

**Fırlatılabilir nesne kuralı:** Her savaş alanında en az 3, en fazla 7 fırlatılabilir prop görünür durumda.

### 6.4 Çevresel Hikaye Anlatımı

Oyuncu anlatı bilgisinin %60'ını metne bakmadan görselden okumalıdır.

- **Kut izleri:** Taze = parlak altın-amber; eski = solmuş toprak rengi
- **Düşman işgal göstergeleri:** Bozulmuş/devrilmiş Türk sembolleri (balbal); kap ve silah düzeni düşmanın nereye hazırlandığını söyler
- **Hayatta kalan izleri:** Söndürülmüş ateş + dağılmış eşya + kan yok → kaçış. Kan izi → savaş olmuş, kazanan belli değil.
- **Coğrafyanın taraf tutması:** Oyuncunun ilerleyeceği yön horizon'da her zaman açık gökyüzüne bakar; düşman tarafı horizon kapalı.

**Okunabilirlik garantisi:** Yeni environment asset her zaman 200–500 birim mesafede karakter silüetiyle test edilir. Doku yoğunluğu silüeti boğarsa yoğunluk düşürülür — environment asla oyuncunun okunabilirliğinden önce gelmez.

## 7. UI/HUD Visual Direction

### 7.1 Diegetic vs. Screen-space HUD

**Diegetic (dünya içi):**
- Sağlık / Kut enerjisi — ItadoriAura parıltısı; can düştükçe Kut Altınından Gece Mavisine kayar; ayrı can barı eklenmez
- Aktif kılıç durumu — trail yoğunluğu ve rengi güç seviyesini iletir

**Screen-space:**
- `WBP_HudGrab` — telekinezi aktifken XYZ eksen göstergesi
- `WBP_TutorialPrompt` — öğrenme aşamasına özgü
- `WBP_PauseMenu`, `WBP_Restart`, `WBP_MainMenu` — meta UI

**Geçiş kuralı:** "Bu bilgi Kut enerjisinde zaten var mı?" → Evetse diegetic çöz. Hayırsa screen-space; ama görsel dili kır — Gece Mavisi panel + altın metin standardını koru.

### 7.2 Tipografi

| Rol | Font | Boyut | Renk |
|-----|------|-------|------|
| Ekran başlığı | Gelio Fasolada | 48 pt | Kut Altını |
| Buton etiketi | Gelio Fasolada | 28 pt | Altın → Kızıl (hover) |
| Vücut / açıklama | Gelio Fasolada | 20 pt | Küllü Beyaz |
| HUD etiketi (XYZ) | Roboto Bold | 18 pt | Altın (aktif) / %25 opasite (pasif) |

- **HUD için Roboto Bold:** Gelio Fasolada küçük pt'de karakter ayrımı kaybeder (I/İ/l karışıklığı). Bilinçli karışım: "menü = Kut mirasının sesi" / "HUD = anın işlevsel bilgisi"
- **Minimum okunur boyut:** 16 pt (1080p; 1.15x render scale compensate eder)
- **Letter-spacing:** başlıkta +0.05em; vücut ve HUD'da 0
- **Türkçe karakter:** Ğ/ğ, İ/ı, Ö/ö, Ü/ü, Ş/ş, Ç/ç glyph'leri zorunlu. Fallback: Cinzel veya Trajan Pro. Unreal font import'ta Unicode mod seçilmeli.

### 7.3 İkonografi Stili

Outlined/lineer, köşeli:
- Çizgi ağırlığı: 2px (1080p), hover'da 3px; köşe radyusu 0px
- Hat açısı: 90° veya 45° tercihli
- Çerçeve: tek köşe kırpılmış dikdörtgen; sol üst veya sağ alt köşe
- Aktif: Kut Altını; pasif/kilitli: %40 opasite Gece Mavisi
- Boyutlar: HUD 32×32px tuval / 24×24px aktif alan; menü 24×24px; vurgu 64×64px

### 7.4 UI Animasyon Hissi

| Geçiş | Süre | Eğri |
|-------|------|------|
| Menü açılış/kapanış | 180 ms | ease-out cubic |
| Hover renk (altın→kızıl) | 120 ms | linear |
| HUD belirme | 80 ms | ease-in |
| Tutorial prompt fade-in | 300 ms | ease-out |
| Ölüm/restart ekranı | 400 ms | ease-in |

- **HudGrab pulse:** XYZ etiketleri 100ms aralıkla 1.0→0.85→1.0 opasite döngüsü (sabit ritim — "Kut nefes alıyor")
- **Crush flash:** `WBP_HudGrab` tüm panel 2 frame (33ms) Kut Parlağı beyaz spike → kaybolur; CS_Crush ile eş zamanlı
- **Ölüm:** Tüm screen-space UI desatüre → Gece Mavisine 400ms; yalnızca `WBP_Restart` metni yeniden altınla gelir

### 7.5 Sanat Yönü vs. Okunabilirlik Çatışmaları

| Çatışma | Şiddet | Çözüm |
|---------|--------|-------|
| 800px sabit wrap → küçük ekranda kırılır | **Yüksek** | Viewport genişliğinin %60'ı; `SizeBox` + HFill + padding ile göreli yapı |
| Hover kızılı "tehlike" semantiğiyle çakışıyor | Orta | Hover kızılı ayrı ton (MI_ renk sabiti); anlam = "seçim iradesi = tehlikeye hazır" |
| Renk körü: altın→kızıl renk-only sinyal | Orta | İkincil sinyal: render scale artışı + outline kalınlaşması (zaten var) |
| Diegetic sağlık + renk körlüğü | Orta | Kritik (%25) eşik altında renk-nötr vignette; aura renk + parlaklık ikili sinyal |
| UMG varsayılan köşe yarıçapı | Düşük | Tüm `WBP_*`'da `BorderRadius = 0` zorunlu kural |

## 8. Asset Standards

### 8.1 Poly Count Bütçesi (Steam PC, 1080p, 60fps hedef)

| Kategori | Triangle Üst Sınır (LOD 0) |
|----------|---------------------------|
| Oyuncu karakteri (Kam) | 15.000 tri |
| Düşman karakterleri | 8.000 tri |
| Fırlatılabilir silah | 3.000 tri |
| Büyük environment prop | 5.000 tri |
| Küçük/tekrarlayan prop | 1.500 tri |
| Background dolgu prop | 800 tri |

Meshy çıktıları genellikle 2.000–8.000 tri — düşman ve prop kategorileri için bütçe içinde. Oyuncu 15.000'i aşıyorsa Meshy "Polygon Reduction" ile export öncesi düşürülmeli.

### 8.2 Texture Resolution Tier Sistemi

| Kategori | Tercih | Maks | Format |
|----------|--------|------|--------|
| Oyuncu karakteri | 2048×2048 | 4096×2048 | BC7/BC5/BC4 |
| Silahlar | 1024×1024 | 2048×1024 | BC7/BC5 |
| Düşman karakterleri | 1024×1024 | 2048×1024 | BC7/BC5 |
| Büyük env prop | 1024×1024 | 2048×1024 | BC7/BC5 |
| Küçük/tekrarlayan prop | 512×512 | 1024×512 | BC7 |
| VFX sprite sheet | 512×512 | 1024×1024 | BC7/R8 |
| UI / HUD elementleri | 256–512×256–512 | 1024×1024 | BC7, NoMipMaps |

Tüm texture boyutları power-of-two. Non-power-of-two yalnızca UI atlas'larında kabul edilir.

### 8.3 LOD — Nanite Değil, Engine LOD

**Nanite kapalı.** Gerekçe: Meshy low-poly (2.000–8.000 tri) Nanite eşiğinin altında; Kut materyalleri WPO/emisyon animasyonu kullanır (Nanite uyumsuz); skeletal mesh zaten desteklenmiyor.

**Engine LOD sistemi:**

| Seviye | Triangle | Ekran Boyutu | Mesafe |
|--------|----------|--------------|--------|
| LOD 0 | Tam bütçe | > %15 | 0–200 ü |
| LOD 1 | %50 | %5–15 | 200–500 ü |
| LOD 2 | %20 | %1–5 | 500–1000 ü |
| LOD 3 | 100–200 tri imposter | < %1 | 1000+ ü |

Aktif savaştaki düşman (`bIsEngaging`) LOD 2'ye geçmez — `ForceLOD 1` kullanılır (gameplay programmer sorumluluğu).

### 8.4 Meshy → UE Import Checklist

| Parametre | Değer |
|-----------|-------|
| Scale | `Import Uniform Scale: 100` (Meshy metre → UE cm) |
| Axis | Z-Up, Y-Forward |
| Smoothing Groups | Açık |
| Tangents | Mikkt Space |
| Combine Meshes | false (ayrı bileşenler ayrı mesh) |
| LOD export | Hayır — UE Engine LOD kullanılır |
| Build Nanite | **KAPALI** |
| Generate Lightmap UVs | Açık (tüm statik mesh) |
| Auto Generate Collision | Açık (interaktif prop: elle UCX_ convex) |
| Normal map G kanalı | `bFlipGreenChannel` kontrol et (Meshy OpenGL normal → UE DirectX) |

**Pivot kuralı:** Fırlatılabilir prop → taban merkezi; skeletal mesh → root kemiği zemin seviyesinde. Pivot UE Static Mesh Editor'da düzeltilir, kaynak `.fbx`'e dokunulmaz.

### 8.5 Material Slot Kuralı

| Nesne Tipi | Hedef | Maks |
|------------|-------|------|
| Oyuncu | 3 | 4 |
| Düşman | 2 | 3 |
| Fırlatılabilir prop | 1 | 1 |
| Büyük env prop | 2 | 3 |
| Küçük prop | 1 | 1 |

Renk/doku varyantları her zaman `MI_` (Material Instance) ile çözülür; ana `M_` asset'e dokunulmaz. M_Highlight telekinezi sırasında slot eklenmeden Dynamic Material Instance parametresi olarak uygulanır (mevcut `ChangeMaterial` bu yolu kullanıyor).

### 8.6 Teknik Çatışma Kayıtları

| Çatışma | Çözüm |
|---------|-------|
| M_Highlight + single-slot kuralı | Post Process Material veya DynMat parametresi |
| Nanite + Kut WPO materyali | Nanite kapalı → çatışma ortadan kalkar |
| Landscape 4 layer sınırı | 3 temel layer (kaya, toprak, ot) + 1 Kut overlay; 5. ihtiyaç makro blend ile birleştirilir |
| **⚠️ Substrate doğrulaması** | `Config/DefaultEngine.ini`'de `r.Substrate` kontrol edilmeli. 1 ise `M_Highlight` ve landscape material'ların Substrate migration'ı gerekli. |

## 9. Reference Direction

**1. God of War (2018) — Santa Monica Studio**
- Alınacak: Yakın-kamera çerçeveleme tekniği — karakterin yarısını çerçeve dışında bırakarak küçük alanda anıtsallık hissi üretmek. Kam'ın idle duruşları ve kamera açıları bu mantıkla kurulur.
- Alınmayacak: Norse mitolojisinin gri/ıslak/soğuk yüzey dili ve kışlık renk paleti. Toygard sıcak toprak ve kızıl renk baskındır.

**2. Shadow of the Colossus (2005) — Team Ico**
- Alınacak: Boşluk kompozisyonu — sahnenin %60–70'ini boş gökyüzü veya açık bozkır olarak bırakmak. Ölçek dramını konuşmadan anlatır.
- Alınmayacak: Melankolik, yorgun dünya tonu ve desatüre sis filtresi. Toygard'ın bozkırı tehditkardır ama canlıdır; Kut enerjisi sahneye güç verir.

**3. Nomad — Olga Drebas (dijital illüstrasyon serisi)**
- Alınacak: Bozkır karakter kıyafet silüet dili — her aksesuar (pelerin, kılıç kını, saç örgüsü) 50px thumbnail'da ayrı okunabilir katman. Kam kostümü tasarımına doğrudan uygulanır.
- Alınmayacak: Suluboya/serbest fırça yüzey dokusu. Referans silüet mantığıyla sınırlı kalır, el çizgisi dokusu PBR diline girmez.

**4. Nioh 2 (2020) — Team Ninja**
- Alınacak: Şaman/yokai efektlerinin savaş sırasında birincil ışık kaynağına dönüşmesi. Kut enerjisinin trail ve aura aracılığıyla sahnenin ışığını devralması bu referanstan türer.
- Alınmayacak: Japon ikonografisi (torii, mon desenleri, Japon kaligrafi motifleri). Toygard Türk-Göktürk ikonografisi kullanır; semboller karıştırılmaz.

**5. Okami (2006) — Clover Studio**
- Alınacak: Efektin ifade aracı olarak kullanılması — kılıç trail ve telekinezi efektleri "görünmez teknik gösterge" değil kasıtlı görsel dil. Kut enerjisinin aktif ışık kaynağı prensibini pekiştirir.
- Alınmayacak: Fırça-vuruşu cel-shading ve ukiyo-e düzlemsel perspektif. Efektin anlatımsal rolü alınır, görsel üslup dili alınmaz.

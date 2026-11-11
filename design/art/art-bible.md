# Art Bible: Toygard

> **Status**: Draft
> **Owned By**: art-director
> **Last Updated**: 2026-11-11
> **Art Director Sign-Off (AD-ART-BIBLE)**: SKIPPED 2026-11-11 — solo mode

`/art-bible` writes these nine sections in this order and replaces each
section's `[To be designed]` line as that section is approved. A section still
holding its placeholder is incomplete; a later run fills only those.

> Pillar yok. İlkeler GDD'deki pitch ("Kut'u silah olarak kullanan, tanrılardan ve
> düşmanlardan intikam arayan savaşçı") ve oyuncu fantezisine ("Kut'u ellerinde
> tutan, fizik yasalarını büken, düşmanlarını kendi silahlarıyla yok eden efsane
> kahraman") dayanır. Aşağıda bunlar **[Pitch]** ve **[Fantezi]** diye anılır.
> Hedef: Deepjam finali ve yatırımcı demosu. Her kural, 3 saniyelik bir trailer
> kesitinde okunabilirliği korumak için var.

## 1. Visual Identity Statement

**Tek satırlık kural:** *Ağır, mat, toprak renkli bir bozkır dünyasında yalnızca Kut parlar — ekranda altın ışık varsa, onu oyuncu kontrol ediyordur.*

- **İlke 1 — Altın = oyuncunun iradesi.** [Fantezi]
  - Kut Altını yalnızca şunlarda kullanılır: oyuncunun elleri/aurası, tutulan nesnenin vurgusu (`M_Highlight`), fırlatılan/çağrılan kılıç ve balta izi, kılıç sörfü, UI.
  - Düşman silahı telekinezi ile yakalandığı anda altına döner: "kendi silahıyla yok etme" böyle okunur.
  - **Test:** Bir prop, ışık veya VFX için altın tonu düşünülüyorsa, onu oyuncu kontrol ediyor mu? Hayırsa altın kullanma; Bozkır Okru'na ya da Balbal Grisi'ne in.
- **İlke 2 — Ağır dünya, hafif güç.** [Pitch]
  - Dünya taş, keçe, ahşap, deri, toprak: mat, yüksek roughness, emissive yok.
  - Kut düşük roughness, emissive, hareketli. Kontrast, gücün fizik kurallarını bükme hissini taşır.
  - **Test:** Bir çevre yüzeyi "biraz parlasın" isteniyorsa, Kut veya ruh (`BP_Soul`) değilse emissive 0 kalır, parlaklığı ışıkla verirsin.
- **İlke 3 — Önce siluet, sonra detay.** [Jam/trailer hedefi]
  - Her karakter, silah ve tutulabilir nesne 1/4 çözünürlükte ve gri tonda tanınmalı.
  - **Test:** Detay mı siluet mi kararsızsan siluete yatırım yap (kask, omuz, silah ucu). Yüzey detayı (desen, yazı) en son ve yalnızca kamera 3 m'den yakınken.
- **İlke 4 — Bozkır yataydır, kutsal ve tehlikeli olan dikeydir.** [Pitch: tanrılar]
  - Arazi, otağlar, ufuk yatay. Balballar, ağaçlar, Gök'ün kutsal yapıları, düşman telegraphları dikey.
  - **Test:** Bir level öğesi dikkat çekmemeliyse yatay ve alçak yap; çekmeliyse dikeyleştir.

## 2. Mood & Atmosphere

Her durum ışık sıcaklığı ve kontrastla ayrışır; iki durum aynı LUT'u paylaşmaz.

- **Ana menü (`L_Main3DMenu`, `LS_MainMenu_01/02`)**
  - Hedef: efsane, saygı, "bir destan açılıyor".
  - Işık: alacakaranlık, 2500–3500 K altın arka ışık + soğuk mavi dolgu; yüksek kontrast, siluet ağırlıklı.
  - Tanımlar: ağır, sisli, törensel, uzak, sessiz.
  - Enerji: düşük; kamera yavaş.
- **Keşif / puzzle (`Oba_L`, arena aralıkları)**
  - Hedef: merak, ölçek, bozkırın genişliği.
  - Işık: öğleden sonra güneşi, 5000–5500 K, orta kontrast, uzun yumuşak gölgeler; atmosferik sis ile derinlik.
  - Tanımlar: rüzgârlı, geniş, yaşanmış, toprak kokulu.
  - Enerji: orta-düşük. Tutulabilir nesneler çevreden ayrılır (bkz. §6).
- **Savaş (`Stand_Arena` dalgaları)**
  - Hedef: güç, hakimiyet, tehdit.
  - Işık: keşifle aynı güneş, ama post-process kontrastı +, doygunluk −%15 (dünya), böylece Kut Altını ve Kan Kızılı öne çıkar.
  - Tanımlar: tozlu, sert, metalik, kızgın.
  - Enerji: yüksek. Toz, kıvılcım, kamera sarsıntısı (`CS_Crush`) izinli.
- **Kut anı (tutma / ölçek / ezme)**
  - Hedef: "fizik yasası bükülüyor".
  - Işık: tutulan nesneye küçük sıcak point light (Kut Altını); ezme anında 2–3 kare beyaza yakın flaş + vinyet.
  - Tanımlar: gergin, basınçlı, titreşen.
  - Enerji: ani tepe, sonra hızlı düşüş.
- **Kılıç sörfü**
  - Hedef: özgürlük, hız, gökyüzüne meydan okuma.
  - Işık: gökyüzü baskın, soğuk Gök Mavisi ortam + altın iz. Hız çizgileri, hafif FOV artışı.
  - Tanımlar: rüzgârlı, uçuşan, cesur.
  - Enerji: yüksek, sürekli.
- **Mağara açılış sineması (`Stand_Arena`)**
  - Hedef: kutsal/ilahi olanla yüzleşme.
  - Işık: dışarıda sıcak gün, içeride karanlık (Is Karası) + mağaradan sızan soğuk Gök Mavisi. Açılış anında hacimsel ışık huzmeleri.
  - Tanımlar: kadim, ürkütücü, büyük, toz zerrecikli.
  - Enerji: yavaş yükselen.
- **Yenilgi (`WBP_Restart`)**
  - Hedef: kısa yas, hemen "tekrar" isteği.
  - Işık: doygunluk 0'a, Kut Altını söner; yalnızca Kan Kızılı UI kalır.
  - Tanımlar: soğuk, sessiz, ağır. Enerji: çok düşük, 1 sn'den kısa geçiş.
- **Zafer / dalga sonu**
  - Hedef: rahatlama, onur.
  - Işık: doygunluk normale döner, güneş sıcaklığı +300 K; ruhlar (Ruh Turkuazı) yükselir.
  - Tanımlar: aydınlık, dingin, ritüel. Enerji: orta, iniş.
- **Duraklatma (`WBP_PauseMenu`)**: dünya dim overlay ile Is Karası'na çekilir; yalnızca UI altını okunur.

## 3. Shape Language

- **Temel gramer: Orhun açısı.** Kut ile ilgili her şey (oyuncu silüeti, VFX, UI) Orhun yazısı ve tamgalardan gelen keskin açılar, ok uçları, çentikler kullanır. Yuvarlak köşe yok.
- **Şekil–anlam tablosu**
  - Üçgen / ok ucu / çentik → oyuncu, Kut, hareket. (Kahraman şekli)
  - Daire / kubbe → Gök, tanrılar, otağ; dinginlik veya ilahi tehdit.
  - Dikdörtgen / dik blok → balbal, taş, ağırlık, engel.
  - Düzensiz, kırık → hasar, ezilmiş nesne, yıkım.
- **Karakter siluetleri**
  - Her arketipin **bir** ayırt edici siluet özelliği vardır (bkz. §5). İkinci bir özellik eklemeden önce ilkinin gri tonlu küçük resimde okunduğunu kanıtla.
  - Oyuncu: yukarı/ileri yönlü üçgen (geniş omuz, daralan bel, uçuşan saç örgüleri ve kaftan eteği).
  - Düşmanlar: kafa/kask şekli fraksiyonu söyler; gövde kütlesi rütbeyi söyler.
- **Çevre geometrisi**
  - Yatay hakim: alçak tepeler, yatay kaya katmanları, otağların basık kubbeleri.
  - Dikeyler seyrek ve anlamlı: balbal sıraları, tek ağaçlar, mağara ağzı, totem. Bir kompozisyonda en fazla 1 baskın dikey.
  - Tutulabilir nesneler kapalı, kompakt hacimlerdir (sandık, taş blok, balbal, kütük). İnce/delikli formlar (çit, dal) tutulamaz → böylece şekil "tutulabilir mi" sorusunu cevaplar.
- **UI şekil grameri**
  - Pahlı (chamfer) köşeler, Orhun harflerinden türetilmiş çentik/ok ayraçlar.
  - Paneller ince çerçeveli, dolgu yarı saydam Is Karası. Yuvarlak buton yok.
- **Kahraman vs destek şekilleri**
  - Kahraman (oyuncu, tutulan nesne, aktif düşman, telegraph): yüksek kenar kontrastı, sade iç yüzey.
  - Destek (çevre, uzak kalabalık): düşük kontrast, iç detay serbest ama değer aralığı dar.
  - **Test:** Bir nesne hem detaylı hem dikkat çekici olmak istiyorsa, kahraman mı? Değilse kenar kontrastını düşür.

## 4. Color System

### Ana palet (7 renk)

| # | Ad | Hex (sRGB) | Anlamı |
|---|----|-----------|--------|
| 1 | **Kut Altını** | `#E8B04A` (dünya/VFX) · `#EADAB8` (UI, bkz. altta) | Oyuncunun gücü ve kontrolü. Yalnızca oyuncuya aittir. |
| 2 | **Kan Kızılı** | `#B23A22` | Tehlike, düşman saldırı telegraphı, hasar, UI hover. |
| 3 | **Gök Mavisi** | `#3E6FA3` | Tengri/Gök, tanrılar, ilahi mekânlar, gökyüzü. Soğuk ve uzak. |
| 4 | **Ruh Turkuazı** | `#5FC4B8` | Ruhlar (`BP_Soul`), ödül, iyileşme. Türk çini turkuazından. |
| 5 | **Bozkır Okru** | `#A88B5C` | Toprak, kuru ot, keçe, ahşap. Dünyanın taban rengi. |
| 6 | **Balbal Grisi** | `#6E6A63` | Taş, balbal, kaya, metal zırh. Nötr kütle. |
| 7 | **Is Karası** | `#1E1A17` | Gölge, mağara, UI zemin/overlay. Saf siyah (`#000`) yerine. |

### Semantik kurallar

- Ekran alanının ~%70'i Bozkır Okru + Balbal Grisi + Is Karası; ~%20 Gök Mavisi (gökyüzü/uzak); vurgu renkleri (Altın, Kızıl, Turkuaz) toplamda ≤%10.
- **Kut Altını** ve **Kan Kızılı** aynı nesnede aynı anda bulunmaz. Tutulan bir düşman silahı kızıldan altına *geçer*, ikisini birden göstermez.
- Emissive yalnızca Kut Altını, Ruh Turkuazı ve Kan Kızılı (telegraph) için. Gök Mavisi emissive ancak ilahi/sinematik anlarda.
- Albedo değer aralığı: sRGB 30–240. Kar beyazı ve saf siyah albedo yasak (Lumen'de patlar/çöker).
- Kararsızsan: vurgu rengi koymak yerine değer (açık/koyu) kontrastı kullan.

### Bölge sıcaklık kuralları

- `Oba_L`: sıcak (Okru baskın, kilim/keçe vurguları serbest ama doygunluk ≤%60).
- `Stand_Arena` açık alan: nötr-sıcak; mağara içi: soğuk (Gök Mavisi dolgu, Is Karası).
- İlahi/Gök mekânları: soğuk; Kut Altını burada en yüksek kontrastı verir — bilinçli olarak.
- Kural: bir bölgenin ortam ışığı sıcaksa, tehlike göstergesi değerle (parlaklık) ayrılır, tonla değil.

### Fraksiyon aksanları (palet dışı, düşük doygunluk ≤%45)

- **Moğol**: koyu çivit `#2F3F5C` + kürk kahvesi.
- **Bizans**: imparatorluk moru `#5B2A4E` + bronz.
- **Çin**: siyah lake + yeşim yeşili `#4F6B4A`. (Kırmızı lake yasak: Kan Kızılı ile çakışır.)
- Hiçbir fraksiyon aksanı Altın, Kızıl veya Turkuaz olamaz.

### UI paleti (mevcut uygulamadan)

- UI Altını: linear `(0.823, 0.701, 0.479)` → sRGB `#EADAB8`. Boşta metin, HUD eksen harfleri (X/Y/Z).
- UI Kızılı: linear `(0.445, 0.042, 0.016)` → sRGB `#B23A22` = Kan Kızılı. Hover. UI'da kızılın "tehlike" anlamından sapması kabul edilmiştir: hover = "bu eylem bir şeyi bitirir" (silah çekme metaforu).
- Zemin: Is Karası %60–75 opaklık (pause dim overlay).
- Devre dışı / kapalı eksen: aynı renk, render opacity 0.25.
- **Açık karar — UI altınının hex'i:** UMG renkleri linear okunur, bu yüzden değerler soluk bir krem `#EADAB8` verir. Değerler sRGB sanılarak girildiyse niyet edilen ton daha doygun `#D2B37A` idi. Ekranda bakıp karar ver: krem kalırsa Kut Altını (`#E8B04A`) ile UI arasında ayrım kalır; `#D2B37A`'ya çekilirse UI ile dünya altını birleşir.

### Renk körlüğü yedekleri

- **Telekinezi vurgusu (`M_Highlight`)**: renk + Fresnel kenar çizgisi + hafif nabız (0.8 sn) + tutma sesi. Kenar çizgisi tek başına okunmalı.
- **Düşman fraksiyonu**: renk değil siluet (kask şekli, §5) birincil ayırıcıdır. Renk yalnızca destek.
- **Tehlike telegraphı**: Kan Kızılı + şekil (genişleyen halka / ok ucu, zemin decal) + ses cue'su. Kızıl/yeşil ayrımına hiçbir yerde güvenme.
- **X/Y/Z eksen HUD**: harf zaten metin (renk değil); açık/kapalı opaklıkla (1.0 / 0.25) ayrılır. Ek öneri: açık eksenin altına 2 px alt çizgi.
- **Ruh / ödül (Turkuaz) vs Gök Mavisi**: Turkuaz her zaman hareketli parçacık + yukarı akış; Gök Mavisi durağan. Hareket ayırıcıdır.

## 5. Character Design Direction

- **Oyuncu — Kut taşıyıcısı Göktürk savaşçısı**
  - Arketip: kahraman intikamcı; soylu ama yıpranmış.
  - Ayırt edici özellik: **Kut ile ışıyan eller/önkollar** (güçlerin fiili eldedir). Saç örgüleri ve kaftan eteği ikincil hareket verir.
  - Değer: sahnedeki **en açık değerli insan figürü** (kemik beyazı/açık keçe kaftan, Okru deri, altın kemer tokaları). Düşmanlar daha koyu.
  - Silah: kılıç (ve balta) silueti oyuncu silüetinden taşar; fırlatıldığında altın iz bırakır.
- **Düşmanlar (`BP_Enemy` tabanı)** — fraksiyon = kask/baş silueti:
  - **Moğol**: kürk kenarlı konik/yuvarlak börk, geniş omuz, yay veya eğri kılıç. Kütle alçak ve geniş.
  - **Bizans**: yüksek tepelikli miğfer, büyük kalkan (dikdörtgen/badem), dik duruş. Kütle uzun ve kapalı.
  - **Çin**: geniş kenarlı ya da kanatlı kask, katmanlı lamel zırh, mızrak/glaive (uzun dikey çizgi).
  - Rütbe: sıradan asker ince; elit/komutan omuz kütlesi +%20 ve tek fraksiyon aksanı bayrak/sorguç.
  - **Test:** Üç fraksiyon gri tonlu siluet olarak yan yana konduğunda 32 px yükseklikte ayrılmıyorsa, kafayı değiştir, rengi değil.
- **Balballar (`BP_Balbal`)**: insan yüzlü dik taş. Düşman olarak aktifken çatlaklarından Kan Kızılı sızar; pasif prop iken hiç ışımaz. Aynı mesh, iki durum = ışık farkı.
- **Ruhlar (`BP_Soul`)**: insan formunun yarı saydam, Turkuaz, alttan dağılan versiyonu. Sert kenar yok.
- **Uldız (Could Have) / NPC'ler / at**: NPC'ler `Oba_L`'de silahsız, Okru/keçe tonlarında; tehlike veya Kut rengi taşımaz. Uldız tasarlanınca Gök Mavisi ile ilişkilendirilmesi önerilir (ilahi bağ) — karar anlatıma bağlı.
- **Poz ve ifade**
  - Oyuncu: Kut kullanırken açık avuç, ağırlık arka ayakta, gövde nesneye dönük (çekme/itme fiziği okunsun).
  - Düşmanlar: saldırı öncesi en az 0.4 sn belirgin anticipation pozu (telegraph ile eş zamanlı).
  - Yüz ifadesi oyun kamerasında okunmaz; duygu bedenle verilir. Yüz detayı yalnızca sinematikte.
- **Kamera mesafesi / LOD felsefesi**
  - Oyun kamerası (3. şahıs, 3–6 m): siluet, malzeme ayrımı (metal/deri/kumaş), aksan rengi okunur; nakış ve yüz okunmaz.
  - Nakış/desen normal map'te değil, albedo'da geniş bloklar halinde; LOD1'de kaybolması sorun değil.
  - Kararsızsan: detayı silah ve başa koy, gövdeye değil.

## 6. Environment Design Language

- **Mimari ve kültür**
  - Göktürk/bozkır: otağ (keçe çadır), ahşap kafes (kerege), kurgan, balbal sıraları, tamgalı kaya, taş höyük. Kalıcı yapı az; dünya göçebe.
  - İlahi mekânlar (mağara, Gök yapıları): insan ölçeğinin 3x+ ölçeği, daire/kubbe, tek doğal malzeme (kaya) + Gök Mavisi ışık.
  - Düşman fraksiyon yapıları (gelecekte): yalnızca fraksiyonun kask diliyle uyumlu bir sancak/çadır; tam mimari üretme (kapsam).
- **Doku felsefesi: zemine bağlı PBR, stilizasyon şekil ve renkte.**
  - Megascans (Fab) zemin, kaya, foliage için kullanılır; renk MI ile palete çekilir (doygunluk −, ton Okru/Gri'ye).
  - Meshy propları aynı PBR kurallarıyla yeniden dokulanır (bkz. Meshy kuralları).
  - Neden: solo geliştirici için Megascans hız sağlar; elle boyanmış stilize dünya kapsam dışı.
  - **Açık karar — gerçekçilik düzeyi:** Megascans gerçekçiliği ile Meshy'nin yumuşak, AI-stilize formları yan yana sırıtabilir. (a) Megascans'ı baz al, Meshy proplarını sertleştir (daha az iş, daha gerçekçi); (b) her şeyi hafif stilize et (tek tip görünüm, ama Megascans'ı da MI ile yumuşatmak gerekir). Öneri (a), jam sonrası yeniden değerlendir.
- **Meshy prop kuralları (zorunlu)**
  - Ölçek cm, pivot tabanda ortada, +X ileri.
  - Albedo'dan baked ışık/gölge/AO temizlenir; AO ayrı kanala.
  - AI kaynaklı anlamsız yazı, sahte tamga ve erimiş detaylar silinir veya düzleştirilir. Tamga/Orhun harfi gerekiyorsa elle, gerçek kaynaktan çizilir.
  - Normaller kontrol edilir; ters/kırık yüzey kabul edilmez.
  - Renk palete MI ile değil kaynakta düzeltilir, MI yalnızca ince ayar.
  - Texel density diğer proplarla eşit (§8).
  - Kaynak `.fbx`/`.png` dosyaları eski klasörlerde kalır; silinmez (CLAUDE.md).
- **Prop yoğunluğu**
  - Arena (`Stand_Arena`): seyrek. Zemin okunur, her 10x10 m'de 2–4 tutulabilir nesne, dekor propu ≤ tutulabilir sayısının 2 katı.
  - Oba (`Oba_L`): orta-yoğun; yaşam izi (kazan, keçe, eğer), ama yürüme yolları boş.
  - Mağara/ilahi: çok seyrek; boşluk kutsallığı taşır.
  - Ufuk: pine imposter ve uzak kaya; ufuk çizgisi asla tamamen kapanmaz.
- **Tutulabilir nesne okunurluğu**
  - Tutulabilir nesneler kompakt şekilli (§3), çevreden bir değer adımı açık veya koyu ve zemine gömülü değil (gölgeli temas).
  - Nişan alındığında `M_Highlight` kenar çizgisi; bundan önce özel renk yok (dünya doğal kalsın).
  - **Test:** Bir prop tutulabilir mi tartışmalıysa, oyuncu nişan almadan önce şekilden anlayabilmeli; anlayamıyorsa şekli değiştir veya tutulamaz yap.
- **Çevresel anlatım**
  - Kut ve tanrılar: Gök'e dönük kırık balballar, yıkılmış otağlar, yanık izleri = intikam bağlamı.
  - Düşman işgali: fraksiyon sancakları Oba'nın içine saplanmış.
  - Tamga ve Orhun yazıtları yalnızca anlamı bilinen yerlerde ve az sayıda (her bölgede ≤3 odak).
  - Kural: anlatı propu oyun alanını kapatmaz; kenarlarda veya yükseltide durur.

## 7. UI/HUD Visual Direction

- **Diegetik vs ekran HUD**
  - Ekran HUD minimal: grab el ikonu + X/Y/Z eksen harfleri (`WBP_HudGrab`), sağlık, tutorial istemi (`WBP_TutorialPrompt`).
  - Diegetik destek: Kut gücü ellerde ve tutulan nesnede görünür (vurgu, nabız); hasar ekran kenarında kızıl vinyet.
  - HUD öğesi yalnızca diegetik karşılığı oyun kamerasında okunmuyorsa eklenir.
  - **Açık karar — diegetik eksen göstergesi:** X/Y/Z maskesini nesnenin üzerinde altın eksen okları olarak göstermek daha sinematik ve trailer'a uygun, ama küçük/uzak nesnelerde okunmaz ve ek VFX işi demek. Mevcut ekran HUD'ı jam için yeterli; diegetik oklar jam sonrası değerlendirilsin.
- **Tipografi**
  - Başlık/menü: `Font_GelioFasolada`, UI Altını, hover'da UI Kızılı + 1.15x render scale (`WBP_MainMenu`, `WBP_PauseMenu` ile aynı).
  - HUD/sayı: Roboto Bold 18, 1 px outline (Is Karası), UI Altını.
  - Gövde metni (tutorial): satır 800 px'te kırılır; en az 22 px (1080p).
  - Minimum okunabilir boyut: 1080p'de 16 px; altı yasak.
  - Hiyerarşi: başlık 48–72 px > menü öğesi 32–40 px > HUD 18–24 px > ipucu 16–20 px.
  - **Açık karar — ikinci font:** Roboto okunaklı ama kimliksiz. Gövde/HUD için Türkçe karakter (ğ, ş, ı, İ) desteği tam, hafif açılı bir humanist sans aranabilir; aksi halde Roboto kalır. Gelio Fasolada küçük boyutta kullanılmaz.
- **İkonografi**
  - Tek renk (UI Altını) düz siluet, Orhun/tamga açılarında; gradyan ve 3D ikon yok.
  - Her ikon 24 px'te okunmalı; ikonla metin birlikte kullanılabiliyorsa birlikte kullan.
- **UI animasyon hissi**
  - Hızlı ve ağırlıklı: giriş 0.15–0.25 sn ease-out, çıkış daha hızlı (≤0.15 sn).
  - Hover: renk + ölçek + `SW_Sword_SwingAndFly` sesi; üçü birlikte (renk tek başına değil).
  - Sallanma/zıplama (bounce) yok; Kut hissi "çekilme", oyuncak hissi değil.
- **UX okunabilirlik kontrolü (her yeni ekran/HUD için)**
  - Savaşta, ekranın merkez %40'ında HUD öğesi yok; HUD köşelerde.
  - Telegraph, tutulan nesne ve oyuncu her zaman HUD'ın önünde okunur (HUD opaklık ≤%85).
  - HUD olmadan (screenshot modu) savaş durumu anlaşılmalı: tutulan nesne vurgulu, düşman telegraphları görünür.
  - Pause/restart ekranları oyun dünyasını dim ile korur; tam siyah ekran yok.
  - Renk dışı ayırıcı kontrolü: §4 renk körlüğü listesi her UI değişikliğinde tekrar denetlenir.

## 8. Asset Standards

- **İsimlendirme**: projenin mevcut kuralı geçerlidir (CLAUDE.md): tip öneki + PascalCase — `BP_`, `WBP_`, `ABP_`, `BPI_`, `E_`, `SG_`, `SM_`, `SK_`, `SKEL_`, `PHYS_`, `M_`, `MI_`, `T_<Asset>_<Role>`, `NS_`, `SW_`, `ATT_`, `LS_`, `L_`. Retarget animasyon adları (`MF_Unarmed_*`, `MM_*`) olduğu gibi kalır. Yeni kural icat edilmez.
  - Doku rolleri: `_BaseColor`, `_Normal`, `_ORM` (R=AO, G=Roughness, B=Metallic), `_Emissive`, `_Mask`. Meshy'den türetilemeyen roller orijinal indeksi korur (`Image0`, `Tex1`).
  - Klasör: her prop kendi klasöründe `Content/Kutun/Environment/Props/<Prop>/`; UI dokuları `Kutun/UI/Textures/T_UI_*`.
- **Dosya formatları**
  - Mesh kaynak: `.fbx` (LFS). Doku kaynak: `.png` 8 bit (normal map 16 bit izinli), LFS.
  - Ses kaynak `.wav` (sanat alanı dışı, yalnızca not).
  - Sıkıştırma: BaseColor BC7/Default (sRGB açık), Normal BC5 (sRGB kapalı), ORM/Mask Masks (sRGB kapalı), UI `UserInterface2D`.
- **Export ayarları**: cm birim, Z-up, +X ileri, pivot tabanda, transform uygulanmış, smoothing groups açık, tek UV kanalı + lightmap gerekirse UV1.
- **Texel density** (öneri): karakterler 1024 px/m, kahraman proplar 512 px/m, çevre/arazi 256–512 px/m. Yan yana duran iki prop arasında 2x'ten fazla fark olmaz.
- **Doku çözünürlük katmanları** (öneri, onay bekliyor)

| Kategori | Varsayılan | Maks. |
|----------|-----------|-------|
| Oyuncu (gövde/kafa) | 2048 | 4096 (yalnız sinematik yakın plan) |
| Düşman / NPC | 2048 | 2048 |
| Silah (kılıç, balta, mızrak) | 1024 | 2048 |
| Tutulabilir / kahraman prop | 1024 | 2048 |
| Küçük dekor prop | 512 | 1024 |
| UI doku / ikon | 256–512 | 1024 |
| Megascans | 2048 indir, oyunda LOD bias ile 1024 hedef | 4096 yalnız zemin |

- **Poligon bütçeleri** (öneri, onay bekliyor — `project.yaml`'da performans bütçesi yok)

| Kategori | LOD0 üçgen | LOD sayısı / Nanite |
|----------|-----------|---------------------|
| Oyuncu `SK_` | 60–80k | 3 LOD (−50% her adımda) |
| Düşman `SK_` | 25–40k | 3–4 LOD; arenada aynı anda 10+ düşman varsayımı |
| Ruh / at `SK_` | 15–30k | 3 LOD |
| Silah `SM_` | 3–8k | 2 LOD; fırlatılan silahlarda Nanite kullanma (hareketli, küçük) |
| Tutulabilir prop `SM_` | 5–20k | Nanite açık, ama ölçeklendirme sırasında 10x büyütmeye dayanmalı (silüet kırılmamalı) |
| Statik çevre propu `SM_` | 20–200k (Meshy önce ≤100k'ya indirilir) | Nanite açık |
| Foliage | imposter (`PineImposter`), yakın plan Nanite foliage | — |

- **Malzeme slotları**: karakter ≤3, silah 1, prop ≤2, modüler çevre 1. Her `MI_` bir proje master `M_`'inden türer; prop başına yeni master material yasak.
- **Motor kısıtları (sanatı etkileyen)**
  - Lumen: emissive yüzeyler güvenilir ışık kaynağı değildir; Kut parıltısı için küçük dinamik point light ekle, emissive'i büyütme.
  - Lumen: büyük düz siyah albedo GI'yi öldürür; albedo alt sınırı sRGB 30 (§4).
  - Substrate: projede açık değilse legacy master materyallerle kal; iki sistemi karıştırma. Açmak ayrı bir teknik karardır (technical-artist).
  - `M_Highlight` overlay/Fresnel tek materyalde kalır; `MATERIALCHANGE` graph'ı refactor edilmeden ikinci bir vurgu materyali eklenmez.
  - Ölçeklendirme: nesneler 10x'e kadar büyür; doku tekrarı ve texel düşüşü kabul, ama UV dikişleri büyük ölçekte görünür olmamalı (dikişleri alt/arka yüze koy).
- **Açık karar — Nanite vs Meshy temizliği:** Nanite, Meshy'nin yüksek poligonlu çıktısını olduğu gibi kullanmaya izin verir (zaman kazancı), ama disk boyutu, AI artefaktları ve tutarsız yüzey kalitesi kalır. Öneri: statik dekor için Nanite + hafif decimate; tutulabilir ve kahraman proplar için tam temizlik (§6). Bütçe rakamları ilk profil (`/perf-profile`) sonrası onaylanmalı.

## 9. Reference Direction

- **Orhun Yazıtları ve Göktürk tamgaları (gerçek arkeolojik kaynak)**
  - Al: açılı, çentikli harf formları → UI ayraçları, Kut VFX şekilleri, ikon dili.
  - Kaçın: gerçek harfleri anlamsız dizilerle "süs" olarak kullanmak. Yazı gerekiyorsa gerçek metinden ve doğru anlamla.
- **Balbal taşları, kurganlar ve Altay/Moğolistan bozkır fotoğrafçılığı**
  - Al: yatay ufuk, alçak güneş, rüzgârla eğilen ot, aşınmış taş yüzeyi, insan yüzlü balbal siluetleri.
  - Kaçın: kartpostal doygunluğu; renk §4 paletine çekilir.
- **Keçe ve kilim desenleri (koçboynuzu, eli belinde, muska, su yolu)**
  - Al: üçgen ve basamaklı geometrik motifler → kaftan kenarları, otağ kapıları, sancaklar, UI çerçeve süsleri.
  - Kaçın: desenle yüzey kaplamak; yalnızca kenar ve şeritlerde, gövde düz kalır (§5 LOD felsefesi).
- **"Mongol" (Sergei Bodrov, 2007) ve benzeri bozkır destan filmleri**
  - Al: manzara ölçeği ile insan küçüklüğü kontrastı, sınırlı toprak paleti, tozlu atmosfer, gökyüzünün kompozisyondaki ağırlığı.
  - Kaçın: kostümleri birebir kopyalamak; oyuncu Göktürk'tür, Moğol fraksiyonu düşmandır — iki görünüm karışmamalı.
- **Fiziksel güç okunurluğu (Control, God of War 2018 gibi telekinezi/fırlat-çağır oyunları)**
  - Al: yalnızca *mekanik okunurluk* — fırlatılan nesnenin ağırlık hissi, çarpma anındaki enkaz/toz, çağrılan silahın dönüş izi, kısa hit-stop.
  - Kaçın: bu oyunların mimari, renk veya karakter stilini almak. Toygard'ın görünümü bozkır/Göktürk kaynaklarından gelir; bu referanslar yalnızca "hareket nasıl hissettirir" içindir.

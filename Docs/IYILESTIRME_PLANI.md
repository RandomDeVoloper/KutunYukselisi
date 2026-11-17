# Toygard — İyileştirme Planı

Tarih: 16 Kasım 2026
Çalışma dalı: `codex/project-cleanup-plan`

## Çalışma düzeni

Her seferinde tek küçük iş ele alınır: güncel durumu doğrula, değiştir, ilgili kontrolü yap, sonucu bu dosyaya işle. Bir sonraki aşamaya önceki aşamanın kabul koşulları sağlandığında geçilir. Oynamayı engelleyen yeni bir hata sıranın önüne alınır. Eski belgelerdeki bulgular doğrulanmadan asset silinmez veya yeniden düzenlenmez.

Asset değişiklikleri öncesinde açık editörün bu checkout'u kullandığı ve mevcut çalışmaların kayıt/yedek durumu doğrulanır. `L_Trailer.umap` ilk incelemede değiştirilmiş göründü; mevcut değişiklik korunacak ve bu işin değişikliklerine dahil edilmeyecek. İki PlayerStart veya sekiz TargetPoint bulunması tek başına hata değildir.

## İş sırası

| ID | İş | Durum | Kabul koşulu |
|---|---|---|---|
| P01 | README proje adı, açılış dosyası ve harita bilgilerini düzelt | Tamamlandı | Toygard.uproject ve Config ile uyumlu; eski ISIK/Tutorial yolları yok; yerel bağlantılar geçerli |
| P02 | Güncel hata durumlarını doğrula | Sürüyor — ön inceleme tamamlandı | BUG-0006–0009 mevcut sürümde yeniden denenmiş; her kayda sonuç ve sürüm eklenmiş; yeniden üretilemeyenler test kanıtı olmadan kapatılmamış |
| P03 | Arena yerleşimini incele | Bekliyor | PlayerStart seçimi, spawner SpawnPoints referansları, NavMesh kapsamı ve ölüm bölgesi doğrulanmış; yalnızca kanıtlanan hatalar düzeltilmiş |
| P04 | Mongol animasyon uyarısını incele | Bekliyor | ABP_Mongol Head kemiği ebeveyn uyumsuzluğunun kaynağı belirlenmiş; gerekiyorsa düzeltme ve animasyon kontrolü yapılmış |
| P05 | Crush sesi bağımlılığını kontrol et | Bekliyor | VREditor sesi güncel graph'larda aranmış; kullanılıyorsa uygun runtime sesle değiştirilmiş ve iki ölçekleme/crush yolu denenmiş |
| P06 | HUD ve input sorunlarını küçük düzeltmelere ayır | Bekliyor | İlk grab, bırakma, crush, pause ve restart akışları denenmiş; BUG-0007 ve eksen HUD tekrarı ayrı değerlendirilmiş; yalnızca doğrulanan gereksiz input temizlenmiş |
| P07 | Sinematik geçişlerini düzelt ve test et | Bekliyor | BUG-0008 doğrulanmış; sinematikte HUD/hasar/AI davranışı ve bitişte kontrolün geri gelmesi denenmiş; L_Trailer'daki mevcut iş korunmuş |
| P08 | Spawner ve maç sınır durumlarını test et | Bekliyor | Canlı düşman sayımı, spawn başarısızlığı, son düşman ölümü, süre/kill hedefi ve restart koşulları güncel GameMode'a göre doğrulanmış |
| P09 | Arena zorluk eğrisini ayarla | Bekliyor | BUG-0009 için mevcut instance değerleri kaydedilmiş; küçük ayarlarla öğrenme alanı ve sonraki çatışma baskısı playtest edilmiş |
| P10 | Paketlenmiş sürümü doğrula | Bekliyor | Cook/package sonucu kaydedilmiş; menü, ekran modu, ses, Türkçe metinler, sinematik, savaş ve restart editör dışında denenmiş |
| P11 | Blueprint bağımlılıklarını azalt | Bekliyor | Güncel oyuncu–düşman bağımlılık haritası çıkarılmış; uygun interface değişiklikleri tek tek yapılıp derleme ve savaş testinden geçmiş |
| P12 | BP_Telekinezi sorumluluklarını aşamalı ayır | Bekliyor | Önce HUD/ayarlar gibi küçük parçalar, sonra telekinezi/savaş ele alınmış; her parçada derleme ve ilgili oynanış kontrolü tamamlanmış |

## P02 alt işleri

- BUG-0006: fullscreen/windowed geçişi, Options yerleşimi ve sensitivity taşması.
- BUG-0007: ilk grab'de beyaz/yeşil el görünürlüğü ve hedef rengi.
- BUG-0008: sinematikte sağlık çubuğu, düşman saldırısı ve sinematikten çıkış.
- BUG-0009: spawner yoğunluğu ve mekanik öğrenme akışı; tasarım ayarı P09'da yapılacak.
- Bu dört kayıt 14 Kasım tarihli eski bir build'e ait. Güncel HEAD `105578c` mesajı Options/fullscreen/HUD/sequence input düzeltmeleri bildiriyor; bu, testin yerine geçmez.

## Doğrulama başlangıç noktası

16 Kasım canlı MCP incelemesi: açık harita Stand_Arena, PIE kapalı, 369 aktör, 8 TargetPoint, 2 PlayerStart ve bir BP_EnemySpawner. BP_Telekinezi 55 graph ve EventGraph'ta 21 giriş noktası; BP_Enemy 13 graph. Bunlar performans ölçümü veya tüm graph'ların davranış doğrulaması değildir. Eski 1114 node sayısı yeniden ölçülmedi.

## Tamamlanan işler

- P01 tamamlandı (16 Kasım 2026): README proje adı, açılış dosyası, başlangıç haritası ve harita listesi güncellendi. Toygard.uproject motor sürümü, Config harita ayarları ve ilgili yerel dosyalarla karşılaştırıldı. README içinde ISIK/L_Tutorial_New kalmadığı ve git diff --check sonucu doğrulandı. Oyun assetleri değiştirilmedi.

## P02 ilerleme — 16 Kasım 2026

- BUG-0006–0009'a güncel statik/canlı okuma sonuçları eklendi. Hiçbiri oynanış kanıtı olmadan kapatılmadı.
- İki kısa standart PIE başlatması yapıldı; 20:16:18 ve 20:17:34 UTC'de controller uyuşmazlığı ve boş dizi uyarıları tekrarlandı. Test sonunda StopPIE çağrıldı ve IsPIERunning=false doğrulandı.
- Yeni işler: BUG-0010 (pawn/controller ve sinematik input), BUG-0011 (boş aktör dizisi). P02'nin sonraki parçası bu başlangıç hatalarının kaynağını doğrulamak; ardından eksik etkileşim testlerine dönmek.
- Ek gözlemler: PIE başlatma aracı transient REINST karakter/animasyon referansları nedeniyle isError döndürmesine rağmen PIE başladı; gerçek durum ayrıca kontrol edildi. Axe fizik/collision ve orphaned cave ambience ses uyarıları da logda var; henüz kök neden incelemesi yapılmadı.
- Fullscreen geçişi, ilk grab, L_Trailer sinematiği ve zorluk playtesti henüz tamamlanmadı. Bu yüzden P02 tamamlandı sayılmaz.
- Oyun assetleri değiştirilmedi veya kaydedilmedi. PIE başlangıcında Unreal otomatik Blueprint regeneration yaptı; bu kalıcı bir düzeltme değildir.

## P02 ilerleme — BUG-0010 düzeltmesi

- BP_Telekinezi StartCinematic/EndCinematic girişlerine IsPlayerControlled koruması eklendi; compile başarıyla tamamlandı ve yalnızca bu asset kaydedildi.
- İki ardışık başlangıçta controller uyuşmazlığı görülmedi; uzun oturumda sinematik flag'inin false'a döndüğü okundu. Hareket/kamera playtesti hâlâ bekliyor; BUG-0010 durumu buna göre güncellendi.
- Geri dönüş dosyası .scratch/BUG-0010-before/BP_Telekinezi.uasset altında.
- Sonraki küçük iş BUG-0011: önce EndCinematic'teki, ardından EventGraph başlangıcındaki boş dizi erişimini pin düzeyinde doğrulayıp düzeltmek. Genel EventGraph DSL ile yeniden yazılmayacak.

## P02 ilerleme — BUG-0011 düzeltmesi

- Taban e19de70, çalışma dalı codex/bug-0011-array-guards. Önceki planın başlığındaki dal ilk çalışma dalını gösterir; bu parça yeni daldadır.
- BP_Telekinezi EventGraph ve EndCinematic içindeki iki koşulsuz index 0 okumasına IsValidIndex kontrolü eklendi. İki başlangıç ve bir sinematik bitişinde boş dizi uyarısı görülmedi. Asset kaydedildi.
- Animasyon önizlemesinin REINST uyarısı compile_blueprint sonucunu kirletmeye devam ediyor. ABP değişikliği kalıcılaştırılmadı; temiz editör oturumunda derleme kontrolü ve önizleme referansının kök nedeni ayrı iş olarak bekliyor.
- P02 hâlâ sürüyor: fullscreen/Options, ilk grab/HUD ve L_Trailer etkileşim testleri tamamlanmadı. Dizi doluyken eski sinematik zincirinin davranışı ayrıca test edilmedi.

## 17 Kasım — Sahneye göre sinematik süreleri

Kullanıcı kararı: mağara açılışı 22 saniye, L_Trailer sinematiği 40 saniye; süreler ayrı ayarlanacak.

BP_Telekinezi değişiklikleri:
- Cinematics|Settings kategorisi altında CaveCinematicDuration=22 ve TrailerCinematicDuration=40 eklendi.
- ConfigureCinematicDuration, PIE önekini kaldırarak geçerli harita adını okur: Stand_Arena için CaveCinematicDuration, L_Trailer için TrailerCinematicDuration seçilir. Diğer haritalarda önceki CinematicDuration korunur.
- StartCinematic içinde oyuncu kontrolü doğrulandıktan sonra, timer kurulmadan önce ConfigureCinematicDuration çağrılır.
- Eski CinematicDuration, Cinematics|Runtime kategorisine taşındı; artık seçilmiş çalışma süresini tutar.
- Mağaradaki BP_CutsceneDirector instance süresi zaten 22 idi ve değiştirilmedi. İleride mağaranın toplam süresi değiştirilirse director ile oyuncu kilidi süreleri birlikte değerlendirilmelidir.

Canlı test: Stand_Arena PIE oyuncusunda cinematicDuration=22 ve başlangıçta bIsCinematicActive=true okundu; ardından false'a döndü. Aynı PIE oturumunda open /Game/Kutun/Maps/L_Trailer ile yalnızca oyun dünyasında seyahat edildi; oyuncuda cinematicDuration=40 ve başlangıçta true okundu, süre sonrasında false doğrulandı. Editör haritası Stand_Arena olarak kaldı; harita assetleri kaydedilmedi.

BP_Telekinezi save_assets=true ve is_dirty=false ile kaydedildi. Önceki animasyon önizlemesinin REINST uyarısı compile_blueprint sırasında devam etti; temiz derleme iddia edilmiyor. Runtime PIE başlangıcı başarılıydı. Önceki BUG-0011 düzeltmesi korundu. Yedek: .scratch/cinematic-durations-before-20261117/BP_Telekinezi.uasset.

## 17 Kasım — Animasyon önizleme uyarısı giderildi (BUG-0012)

- Taban a0b11da, dal codex/animation-preview-reference.
- ABP_Telekinezi InitializeAnimation ve UpdateAnimation girişlerine toplam üç IsValid kontrolü eklendi. Başlangıç yolundaki geçersiz owning actor erişimi de korundu.
- ABP_Telekinezi ve BP_Telekinezi temiz derlendi; kısa PIE testinden sonra warnings_as_errors=true ile tekrar başarıyla derlendiler. Önceki notlarda kalan temiz derleme engeli bu değişiklikle giderildi.
- Runtime animasyonun Character/MovementComponent referansları doğru oyuncuya ait olarak okundu. Animasyon state machine'leri ve 22/40 saniyelik süre ayarları değiştirilmedi.
- Yalnızca animasyon Blueprint'i ve takip belgeleri bu parçada kaydedildi. P02'nin fullscreen/Options, ilk grab ve L_Trailer etkileşim kontrolleri hâlâ bekliyor.

## 17 Kasım — BUG-0007 ön doğrulaması

Boşta beyaz HUD açık / yeşil HUD kapalı doğrulandı. İkinci pawn'ın bu iki HUD'u oluşturmadığı okundu. Gerçek ilk grab/bırakma, fare otomasyon ortamı başlatılamadığı için bekliyor; BUG-0007 açık kalır. Oyun asseti değiştirilmedi.

Ek yerleşim doğrulaması: Stand_Arena içindeki TargetPoint_7, BP_CutsceneDirector.handoffPoint olarak atanmış. Spawner'a bağlı olmayan sekizinci nokta eksik spawn bağlantısı değildir; sinematik sonrası oyuncu konumlandırması içindir. P03'ün diğer kabul koşulları henüz tamamlanmadı.

## 17 Kasım — Interface tabanlı hedef göstergesi ve cast envanteri

Kullanıcı kararı: etkileşilebilir hedef yeşile dönmeli; bunu class cast yerine interface/yetenek sorgusu yönetmeli. Bütün cast'ler belirlenecek, özellikle BP_Telekinezi bağımlılıkları küçük parçalarla dönüştürülecek.

WBP_Hud:EventGraph ve WBP_Scope:UpdateCrosshair içindeki Cast To BPI_Interactable düğümleri Does Object Implement Interface(BPI_Interactable) + Branch ile değiştirildi. İki graph'ta dynamic cast sayısı 0; green/white dalları korundu. Her iki widget warnings_as_errors=true ile derlendi ve kaydedildi.

84 Blueprint asset'i ve üç Level Blueprint üzerinden 629 graph tarandı. Kalan 51 cast'in 11'i BP_Telekinezi hedefli. Tam düğüm yolları, işlem amaçları ve dönüşüm sırası Docs/CAST_ENVANTERI.md ve Docs/CAST_ENVANTERI.json dosyalarında. Level Blueprint'lerde cast bulunmadı. Oba_L, ObjectRedirector olarak doğrulandı.

Canlı renk testi, Play öncesi genel derlemede ABP_Unarmed hatasına takıldı. Aynı şablonda envantere alınan Badcastnode var; önce bu referansın kullanımını doğrulamak gerekiyor. Widget derlemeleri temiz olmasına rağmen gerçek yeşile geçiş/ilk grab testi tamamlanmış sayılmıyor. Diğer 51 cast bu parçada değiştirilmedi.

## Güncel öncelik kararı — 17 Kasım 2026

Kullanıcı kararı: kalan cast dönüşümleri not olarak saklanacak ve bug düzeltmelerinden sonra ele alınacak. Öncelik açık bug'ların giderilmesi ve ilgili testlerin tamamlanmasıdır. CAST_ENVANTERI.md / CAST_ENVANTERI.json dosyalarındaki 51 cast (11 BP_Telekinezi hedefli) ertelenmiş mimari işlerdir; normal bug çalışması sırasında toplu cast refactor başlatılmayacak. Bir cast doğrudan doğrulanmış bir bug'ın nedeni ise yalnızca o bug için gerekli dar düzeltme yapılabilir. Hedef göstergesinde tamamlanmış interface değişikliği korunur.

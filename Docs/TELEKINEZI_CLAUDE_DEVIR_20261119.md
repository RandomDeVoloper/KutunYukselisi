# Telekinezi uygulama planı ve Claude devir notu

Tarih: 2026-11-19

Kullanıcı hedefi: Nesneleri hızlı, anlaşılır ve ağırlığı hissedilen bir telekineziyle kontrol etmek. Codex temel takip sorunlarını düzeltti; aşağıdaki kalan uygulamalar Claude'a devrediliyor. Bu belge dışarıya gönderilmedi. Mevcut kullanıcı değişikliklerini koru; git reset/checkout yapma.

## 1. Codex tarafından uygulanan P0 değişiklikleri

Asset: `/Game/Kutun/Characters/Player/BP_Telekinezi`.

| Yer | Önce | Şimdi |
|---|---|---|
| `FinalizeGrabSpeed`, fizik simülasyonlu bileşen | InterpolationSpeed doğrudan GetMass | MapRangeClamped(Mass, 1, 100, 18, 8) |
| `UpdateHandleByMass`, ilk takip hızı | 1 | 8 |
| Aynı fonksiyon, FinalizeGrabSpeed zamanlayıcısı | 0.5 sn | 0.15 sn |
| EventGraph SetActorTickInterval, CallFunction_60 ve _62 | 0.1 sn | 0 sn, her kare |
| EventGraph SetActorTickInterval, CallFunction_61 | 0 sn | 0 sn, değişmedi |

1 kg ve altı 18; 50.5 kg 13; 100 kg ve üstü 8 takip hızı alır. Bunlar başlangıç ayarıdır; maksimum taşınabilir kütle kuralı değildir. Fizik simülasyonu olmayan bileşenlerde mevcut 20 değeri korundu. Sadece hedef konumun interpolasyonu değişti; fizik handle stiffness/damping değerleri değiştirilmedi.

Doğrulama: Blueprint compile çağrısı hatasız döndü. İki fonksiyon tekrar DSL olarak okunarak eşleme ve süre doğrulandı. Üç TickInterval düğümü tekrar okunarak 0 doğrulandı. Asset save true döndü. PIE ve gerçek girişle oynanış testi yapılmadı; görsel akıcılık veya ağırlık hissi doğrulanmış sayılmamalı.

Yedek: `Backups/Telekinesis_P0_20261119/BP_Telekinezi_before.uasset`. Editör asset'i bellekte tutarken dosyayı üzerine kopyalama. Kullanıcının başka asset değişikliklerini geri alma.

Risk: Karakterin EventTick'i başlangıç/fırlatma sonrasında da her kare çalışır; o zincirdeki hedefleme/HUD sorguları daha sık çalışabilir. Gerekirse pahalı hedef aramasını ayrı, düşük frekanslı bir zamanlayıcıya ayır; tutulan nesne hedef güncellemesini tekrar 10 Hz'e düşürme. 0.15 sn sonunda hız basamaklı değişir; sonrasında gerekirse yumuşak geçiş ekle.

## 2. Claude için uygulama sırası

### Ek ilerleme — Codex, P1-C kısmi tamamlandı

- `UpdateHandleByMass`: `IsValid(GrabbedComp)` artık fonksiyonun ilk yürütme adımı. StartKutGrabFX ve StartKutHandFX bu kontrolün başarılı dalına taşındı. Boş/geçersiz nesne için efekt, ses veya FinalizeGrabSpeed zamanlayıcısı başlamaz.
- `CancelGrabTransition` fonksiyonu eklendi: self üzerindeki FinalizeGrabSpeed zamanlayıcısını ClearTimerbyFunctionName ile iptal eder.
- `M_ReleaseGrab` makrosunda ReleaseComponent sonrasına CancelGrabTransition bağlandı; mevcut materyal/diğer bırakma zinciri korunur. Diğer release/crush/ölüm yolları henüz merkezi temizliğe taşınmadı; bu görev tamamlandı sayılmamalı.
- Derleme hatasız döndü ve asset kaydedildi. Geçerlilik sırası DSL geri okumasıyla doğrulandı. Runtime giriş testi henüz yapılmadı.
- Ek yedek: `Backups/Telekinesis_P1_20261119/BP_Telekinezi_before.uasset` (P0 sonrası, bu ek düzenlemeler öncesi).
- P1-A incelemesi: PhysicsHandle SetTargetLocationAndRotation NewLocation, `Grab Location` scene component'inin GetWorldTransform Location çıkışından geliyor. Henüz boyut uyarlaması/sweep eklenmedi. Başlangıç noktası EventGraph'taki bu bağlantıdır; önce gerçek grab noktası ile component bounds merkezi arasındaki farkı izle.

### P1-A — Boyuta uygun tutma noktası ve engel kontrolü

**Codex ek ilerleme: ilk uygulama bağlı ve kaydedildi; tam hacim koruması henüz tamamlanmadı.**

`UpdateSafeHoldTarget` ve `SafeHoldTarget` Vector değişkeni eklendi. Fonksiyon, her PhysicsHandle SetTargetLocationAndRotation çağrısından önce çalışır. NewLocation artık SafeHoldTarget'tan gelir; rotasyon yolu korunur.

- Varsayılan hedef mevcut Grab Location bileşeninin dünya konumudur. Handle'da geçerli nesne yoksa bu varsayılan kalır.
- Aktif PlayerCameraManager konumu ile mevcut tutma hedefi arasındaki yön korunur.
- Mesafe = max(mevcut kamera-hedef mesafesi, 120 + 2 * component bounds SphereRadius), cm. Her çağrıda bounds okunduğundan ölçek değişikliği mesafeye yansır. Üst boyut sınırı eklenmedi; çok büyük/uzun nesnelerde uzaklık aşırı olabilir ve ayar gerekir.
- Kameradan yeni hedefe 20 cm yarıçaplı SphereTraceByChannel (TraceTypeQuery1, Visibility) yapılır. Tutulan aktör ve self yok sayılır.
- Engel varsa hedef Hit.Location + Hit.Normal * 5 cm olur. Sorgu başlangıçta iç içeyse önceki PhysicsHandle hedefi korunur. Engel yoksa hesaplanan yeni hedef kullanılır.
- Bu sorgu **tutuş noktasını** korur; nesnenin tam hacmini temsil etmez. Büyük nesne yanlarının duvara girmesini tek başına çözmez. Başlangıç overlap'ında uzun süre takılma için kontrollü bırakma henüz yok.
- Compile hatasız, save true. GetComponentBounds SphereRadius ve BreakHitResult bInitialOverlap/Location/Normal çıkışlarının doğru pinlere bağlı olduğu get_node_infos ile doğrulandı. Oynanış/PIE testi yapılmadı; bu maddeyi tam bitmiş sayma.

Sonraki iş: mevcut ilk aşamayı test et, aşağıdaki tam hacim/anchor tasarımını tamamla. Aynı isimli fonksiyonu tekrar oluşturarak ikinci bir zincir ekleme.

İlk iş olarak mevcut kamera -> tutma noktası -> PhysicsHandle bağlantısını düğüm/pin düzeyinde izle. Aktif FPS/TPS kamerasını kullan. Nesnenin gerçek component bounds'undan boyut al; büyük nesne daha uzakta tutulmalı, ölçek değişince mesafe yeniden hesaplanmalı. İnce ve uzun nesnelerde yalnız bounding sphere kullanımı aşırı mesafe doğurabilir; kutu extents veya kamera yönündeki izdüşümü değerlendir.

Önerilen ayrı fonksiyonlar: `ComputeHoldTarget`, `ResolveHoldObstruction`. İstenen hedefe nesne hacmine uygun sweep yap. Oyuncuyu ve tutulan aktörü sorgudan hariç tut; dünya geometrisini dikkate al. Duvara çarpınca hedef duvarın önünde sınırlansın. Kamera duvar arkasına dönünce nesne duvardan geçmesin. Takılı kalınca sürekli kuvvet biriktirmesin; kısa engelde tutuşu koru, uzun engelde kontrollü bırakma uygula. Süre/mesafe eşiklerini düzenlenebilir değişken yap.

Kabul: küçük taş ve büyük sandık kamerayı kapatmıyor; duvar/köşe/kapı eşiğinde nesne geçişi ve ani fizik fırlaması olmuyor; nesne ölçeklenince hedef mesafesi güncelleniyor. Bu doğrulanmadan fırlatma yönünü değiştirmeye geçme.

### P1-B — Nişangâha doğru, güvenilir fırlatma

**Codex ek ilerleme: M_ReleaseGrab yolu uygulandı, diğer yollar henüz birleştirilmedi.**

- `ComputeTelekinesisAim(ThrownComponent: PrimitiveComponent)` ve `TelekinesisAimDirection` eklendi. Kamera yönü varsayılan; geçerli component için PlayerCameraManager'dan 10000 cm Visibility line trace yapılıyor. Self ve fırlatılan aktör yok sayılıyor. Engel varsa ImpactPoint, yoksa uzak uç hedef seçiliyor. Component dünya konumundan hedefe normalize yön hesaplanıyor; hedef component'in ileri yönünde 10 cm'den yakın/gerideyse kamera ileri yönü korunuyor.
- M_ReleaseGrab içindeki AddImpulse öncesinde yeni fonksiyon çağrılıyor; aynı component fonksiyona aktarılıyor. Mevcut kuvvet çarpanının yön girdisi yeni hesaplanan yönden geliyor. Bu yolda sabit +0.15 yukarı sapması kaldırıldı. Kuvvet ve bVelChange=true korundu.
- WidgetandImpulse yolu henüz değiştirilmedi; kılıç/özel silah girişlerinin kapsamı netleştirilmeden yeni hesabı oraya yayma. Tüm fırlatmaların eşitlendiğini iddia etme.
- Bu bir başlangıç yönü düzeltmesi; yerçekimi için balistik çözüm veya nesne hacmiyle fırlatma güzergâhı sorgusu yapılmıyor. Oyuncudan ayrılana kadar collision geri yükleme hâlâ açık iş.
- Compile hatasız, save true. Yedek: Backups/Telekinesis_ThrowAim_20261119/BP_Telekinezi_before.uasset.
- Bu değişiklikten ÖNCE kısa PIE başlangıç kontrolü yapıldı ve durduruldu. Accessed None / Blueprint Runtime Error / PIE Error sorgusu önceki aynı 06:47:56 sağlık kayıtlarını döndürdü; yeni eşleşme oluşmadı. Tutuş/fırlatma girişi uygulanmadığı için bu, mekanik testi değildir. Yeni yön hesabı henüz oyunda test edilmedi.

Mevcut `WidgetandImpulse` ve `M_ReleaseGrab` içinde fırlatma mantığı tekrarlanıyor. CameraForward + (0,0,0.15), normalize, SwordThrowForce ve AddImpulse(bVelChange=true) kullanılıyor. Tüm giriş yollarını bul; sadece birini düzeltmek davranışları ayrıştırır.

Ortak `ComputeThrowDirection` ve `ThrowHeldObject` oluştur. Kameradan nişangâh hedefini bul, nesnenin gerçek konumundan hedefe yön hesapla. Nesnenin önünde engel varsa hedefi ulaşılabilir noktaya sınırla. Hedef çok yakın/nesnenin gerisinde olduğunda güvenli ileri yön kullan. Oyuncunun kapsülüyle çarpışmayı hemen açmak yerine nesne güvenli ayrılma mesafesine ulaşınca önceki tepkiyi geri yükle; bunu sürekli Pawn Ignore bırakma.

Tasarım önerisi: arcade kontrol için hafif/orta/ağır hız profilleri; ağır nesne daha yavaş fakat daha güçlü çarpışma. bVelChange tek başına hata değildir: istenen hız politikasına göre bilinçli seç. Mevcut hasar hesaplamasını incelemeden enerji/kütle hasarı ekleme. Kılıcın özel fırlatma/geri çağırma davranışlarını genel nesne yoluyla karıştırma.

Kabul: yakın/uzak hedeflerde uçuş nişangâhla tutarlı; duvar dibinde kendine çarpma yok; bırakma itki uygulamıyor; tüm fırlatma girişleri ortak davranıyor; kılıç geri çağırma çalışıyor.

### P1-C — Güvenli durum geçişleri ve temizlik

Durumlar: Idle, Acquiring, Holding, Throwing/Released, Pinned. Önce mevcut bool'ların tüketicilerini listele (tutorial/HUD dahil); hepsini bir anda silme. Geçişleri merkezi fonksiyonlarda topla. Tutuş başlangıcında geçerli component kontrolü VFX/ses çağrılarından önce gelsin. Mevcut UpdateHandleByMass efektleri geçerlilik kontrolünden önce çağırıyor; efekt fonksiyonlarının kendi korumalarını da incele.

Tek temizleme yolu handle'ı bırakmalı, timer'ları iptal etmeli, ses/VFX'i bitirmeli, referansları temizlemeli ve değiştirilmiş gravity/collision/material ayarlarını saklanan değerlerine döndürmeli. Nesne yok edilmesi, crush, ölüm, sinematik, pause ve seviye geçişini ele al. Hızlı bırak-yakala sırasında eski zamanlayıcı yeni nesnenin ayarını değiştirmemeli. Sağlık referansı/uzuv sistemi bu işin kapsamına dahil değil.

Kabul: 20 hızlı tut-bırak/nesne değiştirme döngüsü; elde nesne yok edilmesi; tutulurken crush; ölüm/sinematik. Accessed None yok, eski nesnede efekt veya uğultu kalmıyor, handle sahipsiz kalmıyor.

### P2-A — Seçim toleransı ve rotasyon

Mevcut seçim 20 yarıçaplı SphereTraceForObjects, EventGraph'ta ayrıca 30 yarıçaplı channel trace yolları içeriyor. Bunların amaçlarını ayır; hepsi seçim sorgusu varsayılmamalı. Adayları nişangâha açı, mesafe ve görüş hattıyla puanla. Mevcut hedefe küçük bir koruma payı ver; kamera hafif hareket edince hedef sürekli değişmesin. Önizlenen hedef ve gerçekten tutulan hedef aynı olsun. Duvar arkası, çok ağır veya uygun olmayan hedefleri anlaşılır göster.

Mevcut GrabComponentAtLocation rotasyonu kilitlemez, buna rağmen SetTargetLocationAndRotation çağrısı var. İstenen davranışı nesne profiline göre belirle: serbest sallanan enkaz veya kontrollü yönlenen uzun nesne. Kontrollü profil için rotasyon kısıtlı grab ve angular damping/stiffness ayarlarını birlikte ele al.

Kabul: yan yana küçük nesnelerde seçim stabil; duvar arkasından seçim yok; uzun nesne döndürülürken titreme/ani eksen sıçraması yok.

### P2-B — Ölçeklendirme ve fizik dengesi

UpdateObjectScale eksen maskesi, DeltaSeconds ve crush eşiği kullanıyor; üst sınır eksen başına 10. Ölçeği uygulayan UpdateCrush akışını da incele. Büyütmeden önce yer var mı kontrol et; zemin/duvar içine büyüme engellensin. Kütle ve boyut değişince tutuş profili tekrar hesaplansın. Şu an FinalizeGrabSpeed yalnız gecikmeli yakalama sonrasında çalışıyor; sürekli ölçek değişimine tepki tamamlanmadı.

Kütleyi hacimle sınırsız kübik büyütme; oyun için sınırlandırılmış etkin kütle eğrisi tasarla. Eksen ölçeklendirme ve crush'ın mevcut tutorial bağımlılıklarını koru.

Kabul: duvar dibinde büyütme güvenli, küçültme/crush çalışıyor, büyük nesne kamerayı kapatmıyor, başlangıç ölçeği farklı nesnelerde tutarlılık var.

### P3 — Ağırlığa bağlı geri bildirim ve ayar profilleri

Hafif/orta/ağır profillerini DataAsset veya düzenlenebilir yapı altında topla. Takip hızı, maksimum mesafe, atış hızı, kuvvet/sönümleme ve VFX yoğunluğu ayrı alanlar olsun. Mevcut Kut el/nesne efektleri, uğultu ve FOV değişimini tekrar oluşturma; ağırlık/gerilimle ölçekle. Tutuş boyunca kamera sarsıntısı ekleme. Hedef kilitleme, koparma ve fırlatma anlarında kısa vurgular yeterli.

## 3. İlk oynanış kontrolü

P1'e başlamadan Codex P0 ayarlarını 1, 10, 50, 100 ve 200 kg nesnelerde dene. Küçük nesnenin takibi canlı, ağırınki gecikmeli fakat kontrol edilebilir olmalı. 30/60/120 FPS, hızlı 180 derece dönüş, uzak nesneyi çekme ve art arda tut-bırak dene. Spawn haritasına kalıcı test aktörü koyma. Testte ölçülen takip hatası ve görülen jitter'ı not et; sadece compile başarısını oynanış başarısı sayma.

## 4. Editör çalışma notları

Blueprint-only proje; .uasset dosyalarını metinle değiştirme. Unreal MCP kullan. Kaydet/yedekle, mevcut grafikte küçük pin değişikliklerini tercih et. `write_graph_dsl` eski düğümleri temizlemeyebilir. EventGraph DSL export döngü hatası, collapsed graph export ise K2Node_Composite cast hatası verebilir; `find_nodes` + `get_node_infos` ile incele. Düğüm yollarını yeniden keşfet; bu belgedeki numaralar kalıcı kimlik garantisi değildir.

MCP aynı isimli materyal fonksiyonlarında yanlış sınıf seçebilir; gerektiğinde declaring_class belirt. PIE sırasında Blueprint düzenleme yapma. REINST hatasını otomatik başarı kabul etme; asset durumunu ve logları ayrı doğrula. Çalışma ağacında önceki uzuv/sağlık/harita ve kullanıcı değişiklikleri bulunuyor; sadece kendi kapsamındaki asset'leri kaydet, commit etme.

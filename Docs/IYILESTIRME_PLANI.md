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

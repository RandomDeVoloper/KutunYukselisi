# Stand Modu — İlerleme Kaydı

Son güncelleme: 2026-10-14
Karar: **C++ YOK, iptal edildi.** Proje Blueprint-only kalır (`Source/` boş, `.uproject`'te `Modules` yok).
Tüm Stand Modu mantığı mevcut Blueprint'lerde düzeltildi (Seçenek a).

## Durum özeti

| Adım | Durum | Nerede |
|---|---|---|
| S0 Level hazırlığı | [x] / [manuel doğrulama] | `/Game/Kutun/Maps/Stand_Arena` |
| S1 Match Manager | [x] | `BP_StandGameMode` (Actor değil, GameMode) |
| S2 Blueprint Library | [atlandı] | gereksiz: `BP_Enemy:Die` içindeki `Cast To BP_StandGameMode` zaten güvenli durma sağlıyor |
| S3 Fırlatma hasarı | [atlandı] | gereksiz: hasar `BP_Telekinezi` → `UC_HealthComponent.TakeDamage` ile zaten veriliyor |
| S4 Spawner | [x] | `BP_EnemySpawner` — 4 hata düzeltildi, ramp + preplaced sayımı eklendi |
| S5 HUD / sonuç | [x] | `WBP_StandHUD`, `WBP_Result` |
| S6 Stand ayarları | [ ] | Config'e DOKUNULMADI, kullanıcı onayı bekliyor |
| S7 Test | [ ] | editörde oynanarak test edilecek |

## Mimari (denetimle doğrulandı)

- Oyuncu: `/Game/Kutun/Characters/Player/BP_Telekinezi` (Character)
- Düşman: `/Game/Kutun/Characters/Enemies/Base/BP_Enemy` (Character), `AutoPossessAI = PlacedInWorldOrSpawned` (doğru)
- Sağlık: `/Game/Kutun/Core/Components/UC_HealthComponent` — **AnyDamage değil**, kendi `TakeDamage` fonksiyonu + `OnDepleted` delegate'i
- Düşman AI: **Behavior Tree YOK.** PawnSensing → `OnSeePawn`/`OnHearNoise` → `AI MoveTo`. Projede hiç `BT_*`/`BB_*`/AIController sınıfı yok → Blackboard hedef anahtarı karşılıksız, spawner'ın hedef ataması gerekmiyor
- Öldürme bildirimi: `BP_Enemy:Die` (`bIsDead` guard) → `Cast To BP_StandGameMode` → `AddKill`; ayrıca `GetAllActorsOfClass(BP_EnemySpawner)[0]` → `EnemyDied`
- Mükerrer sayım koruması: `BP_Enemy.bIsDead` guard'ı (TSet gerekmedi)
- Stand_Arena içeriği: `BP_StandGameMode` override, 1 `BP_EnemySpawner`, 34 `BP_Throwable`, `PlayerStart`, `NavMeshBoundsVolume` + `RecastNavMesh`, 7 `TargetPoint`

## Değiştirilen dosyalar

| Dosya | Değişiklik |
|---|---|
| `Content/Kutun/Characters/Enemies/Spawners/BP_EnemySpawner.uasset` | `SpawnOne` tek düşman doğuruyor (Break bağlandı) + `AliveCount < MaxAlive` kontrolü + noktalar shuffle; `EnemyDied` timer'ı düzeltildi (Object=self, Looping=false, AliveCount 0'ın altına düşmez); `BeginPlay` preplaced düşmanları sayar + `RampUp` timer'ı kurar; yeni `RampUp` fonksiyonu (MaxAlive += RampAmount, MaxAliveCap'e kadar); ölü kod `NotifyEnemyDied` ve boş `Tick` silindi; yeni değişkenler `RampEvery=30`, `RampAmount=2`, `MaxAliveCap=14`, `bCountPreplacedEnemies=true` (instance-editable) |
| `Content/Kutun/Core/GameMode/BP_StandGameMode.uasset` | `MatchDuration` 100 → **120**; yeni `RestartMatch` (pause kapat, imleci gizle, **mevcut level**'i aç); yeni `FormatTime(Seconds) → Text` (`1:45` biçimi); `GetRemainingTime` artık timer handle yerine `MatchDuration - geçen süre` (clamp 0); `BeginPlay`'e `EnableInput` eklendi; **F8** (Execute When Paused, Consume Input) → `RestartMatch`; HUD/sonuç widget'ları ZOrder 50 |
| `Content/Kutun/UI/Widgets/WBP_StandHUD.uasset` | Süre `1:45` biçiminde, son 10 saniyede kırmızı; skor `ÖLDÜRME: X` |
| `Content/Kutun/UI/Widgets/WBP_Result.uasset` | `{Kills} DÜŞMAN`, `Son öldürme: 1:52`; **R** artık sabit `Stand_Arena` değil **mevcut level**'i açıyor (`GetCurrentLevelName` exec zincirine bağlandı — ilk denemede "pruned" uyarısı alınmıştı) |
| `Content/Kutun/UI/Widgets/WBP_Restart.uasset` | **Orijinal oyun düzeltmesi:** Restart butonu sabit `Stand_Arena` yerine mevcut level'i açıyor. Construct'ta Stand GameMode varsa widget gizlenip `EndMatch` çağrılıyor → arenada ölünce sonuç ekranı gelir; diğer level'larda eski davranış korunur |
| `STAND_MODE_PROGRESS.md` | bu dosya |

Tüm Blueprint'ler derlendi ve kaydedildi. Derleme logunda bu beşine ait hata/uyarı kalmadı.

## Düzeltilen hatalar (Faz 0 denetimi)

1. `SpawnOne` Break'e hiç gitmiyordu → her uygun noktaya düşman doğuyordu (6 × 7 = ~42 düşman). ✔
2. `EnemyDied` timer'ının Target pini boş, `Looping = true` idi → yeniden doğma çalışmıyor/kontrolsüzdü. ✔
3. Spawner `AliveCount`'u `MaxAlive` ile karşılaştırmıyordu. ✔
4. `NotifyEnemyDied` ölü koddu. ✔ (silindi)
5. `WBP_Restart` sabit `OpenLevel("Stand_Arena")` → tutorial'da ölen oyuncu arenaya düşüyordu. ✔
6. Oyuncu ölümü `EndMatch` çağırmıyordu. ✔
7. F8 yoktu. ✔ (R zaten sonuç ekranında vardı)
8. `MatchDuration = 100`. ✔ → 120
9. HUD süreyi ham float basıyordu. ✔

## Bilinen kalanlar / kararlar

- `RespawnDelay = 1.5` bırakıldı (spec 2.5 diyordu, 1.5 kullanıcının seçimi). Değiştirmek istenirse level'daki spawner instance'ında ayarlanır.
- `EnemyClass` değişkeni **kullanılmıyor**: CDO'ya yazılamadı (TSubclassOf, MCP set_properties reddetti), `SpawnOne` düşman sınıfını sabit `BP_Enemy` olarak kullanıyor. Tek düşman tipi olduğu için sorun değil.
- `SpawnOne`'ın mesafe filtresinde **fallback yok**: `SpawnPoints`'teki hiçbir nokta oyuncudan `MinDistanceToPlayer` (800) kadar uzak değilse o çağrıda düşman doğmaz. 7 nokta ve 40x40 m arenada pratikte oluşmaz.
- `IA_Restart` hâlâ `IMC_Default`'ta duruyor ama **hiçbir yerde dinlenmiyor** (F8 doğrudan GameMode'da Input Key event'i ile çözüldü). Kullanılmayacaksa `IMC_Default`'tan kaldırılabilir.
- F8'in oyun duraklatılmışken de çalışması için node'da `bExecuteWhenPaused = true` ayarlandı; gerçek testi PIE'de yapılacak.

## Bekleyen manuel adımlar (editörde)

1. Stand_Arena'daki `BP_EnemySpawner` instance'ında `SpawnPoints` dizisinin 7 TargetPoint ile dolu olduğunu doğrula (level yüklü olmadığı için denetlenemedi).
2. NavMesh'in arenayı kapladığını P tuşuyla kontrol et.
3. S6 kararları: Config `GameDefaultMap`, tam ekran, Esc/pause.
4. Test listesini (11 madde) oyna.

## 2026-10-14 — "akın akın" ayarı

Şikayet: düşmanlar en fazla 2 noktadan çıkıyor ve yeniden doğma çok yavaş.

**Sebep:** Blueprint varsayılanları değil, **level'daki spawner instance'ı** belirleyicidir ve orada
`MaxAlive = 3`, `RespawnDelay = 3`, `SpawnPoints` dizisinde 7 noktadan 6'sı vardı. Aynı anda 3 düşman
canlı olabildiği için en fazla 3 nokta kullanılıyordu.

`Stand_Arena` → `BP_EnemySpawner_C_0` instance değerleri:

| Alan | Eski | Yeni |
|---|---|---|
| MaxAlive | 3 | **12** |
| MaxAliveCap | 14 | **24** |
| RespawnDelay | 3.0 | **0.4** |
| RampEvery | 30 | **15** |
| RampAmount | 2 | **4** |
| SpawnPoints | 6 nokta | **7 nokta** (TargetPoint_6 eklendi) |
| MinDistanceToPlayer | 450 | 450 (değişmedi) |

Baskı eğrisi: 12 canlı → 15 sn'de 16 → 30 sn'de 20 → 45 sn'de 24 (tavan).

**`BP_Enemy` (stand-only kovalama):** `BeginPlay`'de `Cast To BP_StandGameMode` başarılıysa
`Set Timer by Event(ChasePlayer, 2 sn, looping)` + ilk `AI MoveTo(oyuncu, 150)`. Yeni `ChasePlayer`
custom event'i her 2 saniyede `AI MoveTo` yeniliyor. Cast başarısızsa (tutorial vb.) hiçbir şey
olmaz — düşman eski PawnSensing davranışında kalır. Böylece arenada doğan düşman oyuncuyu
görmeyi beklemeden üstüne geliyor.

**Dikkat — bu adımda bir hata yapıldı ve düzeltildi:** `write_graph_dsl` ile `BP_Enemy:EventGraph`
yazıldığında `Bind Event to OnDepleted`'in delegate pini koptu (DSL mevcut `Die` custom event'ine
bağlanmak yerine yeni bir event düğümü yaratmaya çalıştı) ve derleme
"Event Dispatcher pin is not connected" hatası verdi — o halde **düşmanlar hiç ölmezdi**. Pin
seviyesinde onarıldı: BeginPlay → eski `Bind Event` düğümü → cast; DSL'in ürettiği fazladan
`Bind Event` ve boş `CustomEvent` düğümleri silindi. Ders: **`BP_Enemy:EventGraph`'ı DSL ile
yeniden yazma**, düğüm/pin düzenlemesi kullan.

## 2026-10-14 — Düşmanlar oyuncuyu öldürebiliyor

Şikayet/istek: "biraz zorluk olsun diye karakterimizi öldürebilsin düşmanlar".

**Tespit:** Ölüm zinciri aslında hazırdı — `BP_Telekinezi` `BPI_CombatTarget.ApplyDamage`'ı
uyguluyor, o da `health (UC_HealthComponent).TakeDamage` çağırıyor; sağlık 0'a inince
`UC_HealthComponent:Die` oyuncuysa `WBP_Restart`'ı ekrana koyuyor (Stand modunda bu widget
`EndMatch` çağırıp sonuç ekranını açıyor). Eksik olan tek halka: **düşman saldırısı hiç hasar
vermiyordu.** `BP_Enemy:LoopAttacking` sadece `AM_Attack` montajını oynatıyordu.

Ayrıca iki saldırı hatası vardı:
- Sphere BeginOverlap'teki `Set Timer by Event(LoopAttacking, 1.2)` **looping = false** idi →
  düşman oyuncunun yanında tek bir kez saldırıyordu.
- EndOverlap timer'ı temizlemek yerine `Set Timer by Event(LoopAttacking, 0.0)` çağırıyordu →
  oyuncu uzaklaşınca saldırı bir kez daha tetikleniyordu.

### `BP_Enemy` değişiklikleri

| Alan | Değer |
|---|---|
| Yeni değişken `AttackDamage` (instance-editable) | 12 |
| Yeni değişken `AttackRange` (instance-editable) | 250 |
| Yeni değişken `AttackInterval` (instance-editable) | 1.5 sn |
| Yeni değişken `AttackTimer` (TimerHandle) | — |

- `OnComponentBeginOverlap(Sphere)`: timer artık **looping = true**, süre `AttackInterval`'dan
  geliyor ve dönen handle `AttackTimer`'a yazılıyor.
- `OnComponentEndOverlap(Sphere)`: `Set Timer` düğümü silindi, yerine
  `Clear and Invalidate Timer by Handle(AttackTimer)` geldi.
- `LoopAttacking` yeni akış: `Branch(NOT bIsDead)` → `PlayAnimMontage(AM_Attack)` →
  `Delay 0.35` (vuruş zamanlaması) → `Branch(GetDistanceTo(oyuncu) <= AttackRange)` →
  `ApplyDamage (BPI_CombatTarget mesajı)` Amount = `AttackDamage`, Instigator = self.
  Gecikme + mesafe kontrolü sayesinde oyuncu savrulup kaçarsa vuruş ıskalıyor.

Arayüz mesajı kullanıldığı için hasar `BPI_CombatTarget` uygulayan her hedefe gider; `BP_Enemy`
hâlâ oyuncu sınıfını tanımıyor (cast yok).

### `BP_Telekinezi` değişiklikleri (dokunulmazlık penceresi)

12–24 düşmanlık sürüde her düşman 12 hasar vurursa oyuncu ~1 saniyede ölüyordu. Bunun için
oyuncuya kısa bir vuruş bağışıklığı eklendi:

- Yeni değişkenler: `bHitImmune` (bool), `HitImmunityTime` (float, **1.0**, instance-editable).
- `ApplyDamage` yeni akış: `Branch(NOT bHitImmune)` → `Set bHitImmune = true` →
  `health.TakeDamage(Amount)` → `Set Timer by Function Name("ClearHitImmunity", HitImmunityTime)`
  → `return true`. Bağışıklık açıkken çağrı hasar vermeden `return true` ile dönüyor.
- Yeni fonksiyon `ClearHitImmunity`: `bHitImmune = false`.
- Etkin tempo: en fazla 12 hasar/saniye → 100 canla sürekli temasta ~8 saniye.

Bağışıklık **oyuncu tarafında** (`BP_Telekinezi.ApplyDamage`) duruyor, `UC_HealthComponent`
içinde değil — yoksa oyuncunun kılıç/fırlatma vuruşlarından sonra düşmanlar da 1 saniye
dokunulmaz olurdu.

İki Blueprint derlendi ve kaydedildi; derleme logunda bunlara ait hata yok.

### Test edilecekler (PIE)

1. Düşmanın yanında dur: montaj → ~0.35 sn sonra can azalmalı, saniyede en fazla bir kez.
2. Vuruş anında savrul/uzaklaş: hasar gelmemeli (mesafe kontrolü).
3. Uzaklaş: saldırı timer'ı durmalı (artık montaj oynamamalı).
4. Can 0: `WBP_Restart` → Stand arenasında sonuç ekranı + `EndMatch`.
5. Zorluk dengesi: ölüm çok hızlıysa `AttackDamage`'ı düşür veya `HitImmunityTime`'ı artır
   (ikisi de instance-editable; level'daki düşman/oyuncu instance'ından ayarlanabilir).
6. **Doğrulanamadı:** düşmanın `Sphere` bileşeninin yarıçapı/çarpışma ayarı MCP'den okunamadı.
   Saldırı tetikleyicisi bu overlap'e bağlı; montaj hiç oynamıyorsa yarıçapı editörde kontrol et.

## 2026-10-14 — Can barı (WBP_HealthBar)

Şikayet: "can barı ekle karakterimize canımızın olup olmadığı anlaşılmıyor".

**Yeni asset:** `/Game/Kutun/UI/Widgets/WBP_HealthBar` (UserWidget)
- `RootCanvas` → `PB_Health` (ProgressBar) + `HealthText` (TextBlock), ikisi de widget değişkeni.
- Yerleşim: sol-alt köşeye sabit (anchor 0,1 / alignment 0,1). Bar 420x28, sol 60 / alt 40;
  sayı barın hemen üstünde (Roboto Bold 20, beyaz, gölgeli — `WBP_StandHUD` ile aynı stil).
  Dolgu rengi koyu kırmızı (0.65, 0.06, 0.06).
- Değişken `HealthComp` (UC_HealthComponent referansı).
- Fonksiyon `RefreshHealth`: `PB_Health.SetPercent(CurrentHealth / MaxHealth)` +
  `HealthText.SetText(Round(CurrentHealth))`.
- `Event Tick` → `IsValid(HealthComp)` → `RefreshHealth`.

**`UC_HealthComponent:EventGraph` (BeginPlay):** `SetCurrentHealth(MaxHealth)` zincirinin ardına
`if (GetOwner == GetPlayerPawn(0))` → `CreateWidget(WBP_HealthBar, PlayerController 0)` →
`SetHealthComp(widget, self)` → `AddToViewport` eklendi. `Die` içindeki `WBP_Restart` mantığı da
aynı "sahibi oyuncu mu" kalıbını kullanıyor, böylece bar **her level'da** otomatik çıkıyor ve
düşmanların sağlık bileşeni bar yaratmıyor.

**Neden Tick, neden delegate değil:** `OnHealthChanged` parametresiz ve `Die` canı 0'a çekerken
onu yayınlamıyor; ayrıca tek widget'ın tick'i ihmal edilebilir. Tick, hangi yoldan hasar gelirse
gelsin barın doğru kalmasını garantiliyor.

Not: `write_graph_dsl` iki yerde yanlış düğüm üretti ve elle onarıldı — (a) `(if ...)` içinde
`IsValid` exec makrosunu kullanıp fazladan bağlanmamış bir `Branch` bıraktı (Branch silindi,
makronun "Is Valid" çıkışı doğrudan `RefreshHealth`'e bağlandı); (b) bir başka sınıfın
`SetHealthComp` setter'ına denk gelip tip uyuşmazlığı verdi — düğüm `declaring_class` ile elle
kuruldu (setter'da pin sırası: değer önce, **hedef (`self`) sonra**).

### Test edilecekler (PIE)

1. Oyun başında sol-altta bar + sayı görünüyor mu (hem tutorial hem arena).
2. Düşman vurdukça bar azalıyor mu, sayı yuvarlanmış canı gösteriyor mu.
3. Ölümde bar 0'da kalıp `WBP_Restart`/sonuç ekranı üstte açılıyor mu.
4. Arena HUD'u (ZOrder 50) ile çakışma var mı — bar sol-altta, skor/süre üstte.

## 2026-10-14 — R ile yeniden başlatma + Game Only input

Şikayet: "ölünce R'ye basınca tekrar başlamıyor ve önceden de UI and Game olduğu için mouse ile
yönü kontrol edemiyorduk; oyun tekrar başlayınca Game Only olsun."

**Sebep (R çalışmıyor):** R yalnızca `WBP_Result:OnKeyDown` içinde dinleniyordu. `EndMatch`
`SetInputModeGameAndUI` + `SetGamePaused(true)` yapıyor; bu modda klavye odağı viewport'ta
kalabildiği için widget'ın `OnKeyDown`'ı hiç tetiklenmiyor (widget `bIsFocusable = true` ve
`Construct`'ta `SetKeyboardFocus` çağrılıyor olmasına rağmen). Yani tuş kaybolup gidiyordu.

**Çözüm:** F8 için zaten çalışan kalıbın aynısı — tuş, widget değil **GameMode** üzerinden
dinleniyor. `BP_StandGameMode:EventGraph`'a `R` Input Key event'i eklendi
(`bExecuteWhenPaused = true`, `bConsumeInput = true`, `bOverrideParentBinding = true`) →
`Branch(bMatchOver)` → `RestartMatch`. `bMatchOver` guard'ı sayesinde maç sürerken R'ye basmak
level'ı sıfırlamıyor; sadece sonuç ekranında çalışıyor. `WBP_Result:OnKeyDown` olduğu gibi
bırakıldı — odak gerçekten widget'a geçtiğinde o da çalışır, iki yol da aynı yere varıyor.

**Game Only:** `BP_StandGameMode:BeginPlay` sonuna (`EnableInput`'tan sonra)
`SetInputMode_GameOnly(PlayerController 0)` + `bShowMouseCursor = false` eklendi. Böylece arena
her başlayışta — ilk açılışta, R ile yeniden başlatmada, Restart butonunda — Game Only moda
dönüyor ve mouse yine yönü kontrol ediyor. Sonuç ekranındaki `SetInputModeGameAndUI` bilinçli
olarak korundu: oyuncu actor'ı o anda duraklatılmış durumda ve GameMode'un R event'inin tuşu
alabilmesi için input'un actor'lara ulaşması gerekiyor (UI Only'ye çevirmek bu yolu kapatırdı).

Derlendi ve kaydedildi, hata yok.

### Test edilecekler (PIE)

1. Arena başlar: imleç yok, mouse ile yön kontrolü çalışıyor.
2. Öl veya süre bitsin → sonuç ekranı. R → level yeniden yükleniyor, yine Game Only.
3. Maç sürerken R'ye bas → hiçbir şey olmamalı (`bMatchOver` guard'ı).
4. F8 hâlâ çalışıyor mu (aynı mekanizma, değişmedi).

# Uzuv Kesme Sistemi — Devir Notu (2026-11-18)

Bu doküman başka bir AI ajanının (Codex vb.) devralması için yazıldı.
Önceki oturum Claude Code + `unreal-mcp` ile çalıştı.

---

## 0. ÖNCE BUNU OKU — Bu repoda kod düzenleyemezsin

**Toygard Blueprint-only bir Unreal Engine 5.8 projesi.** `Source/` dizini ve C++
modülü **yok**. Tüm oyun mantığı `Content/` altındaki `.uasset` / `.umap` **binary**
dosyalarında.

Bunun pratik sonuçları:

- `.uasset`/`.umap` dosyalarını metin olarak **okuyamaz ve düzenleyemezsin**. Diff de alamazsın.
- `grep`/`sed` ile Blueprint mantığı değiştirmeye **çalışma**. Hook'lar `Edit(**/*.uasset)` ve `Edit(**/*.umap)` işlemlerini zaten reddediyor.
- Blueprint değiştirmenin tek yolu: **Unreal Editor açıkken** `.mcp.json`'daki `unreal-mcp` sunucusu (`http://127.0.0.1:8000/mcp`). Editör kapalıysa `ECONNREFUSED` alırsın.
- Git LFS zorunlu (`.gitattributes`). Binary asset'ler merge edilemez — branch başına tek değişiklik seti tut.
- **Editör açıkken branch değiştirme.** Gerekirse kısa yollu (`C:\wt`) bir `git worktree` kullan.

Metin olarak düzenleyebileceğin şeyler: `Config/*.ini`, `Docs/*.md`, `.claude/`,
`project.yaml`. Oyun mantığı değil.

Detaylı MCP tuzakları için repo kökündeki `CLAUDE.md` dosyasını oku — orada
"Workflow notes (learned the hard way)" başlığı altında uzun bir liste var.

---

## 1. Bu oturumda kaldırılan test objesi

### Belirti
Stand_Arena'da oyun başlar başlamaz NPC'ler ölüyordu. Kullanıcı önce baltanın
(`BP_Axe`) suçlu olduğunu düşündü; throwable aktörlerini silmek sorunu çözmedi.

### Kök neden
`BP_DismembermentRegression` adlı bir **test harness aktörü** ana oyun haritasına
yerleştirilmişti. BeginPlay'de düşman spawn edip uzuvlarını kesiyor ve öldürüyordu.

```
Asset          : /Game/Developers/Tests/BP_DismembermentRegression
Yerlesim       : /Game/Kutun/Maps/Stand_Arena -> BP_DismembermentRegression_C_0
Geldigi commit : 6682844 "sword kesme hissiyati eksik o halledilecek."
```

### Nasıl kanıtlandı
**Simulate modunda** (oyuncu pawn'ı yok, kimse input vermiyor) çalıştırıldı ve log
yine testi bastı — bu, baltayı/kılıcı/throwable'ları tek hamlede eledi:

```
[BP_DismembermentRegression_C_0] DISMEMBER_TEST PASS Mongol_RightForeArm
[BP_DismembermentRegression_C_0] DISMEMBER_TEST PASS Mongol_Head
[BP_DismembermentRegression_C_0] DISMEMBER_TEST END
```

### Yapılan
`BP_DismembermentRegression_C_0` **sadece Stand_Arena'dan silindi**, harita
kaydedildi. Asset `/Game/Developers/Tests/` altında **duruyor** — ileride ayrı bir
test haritasında kullanılabilir.

Doğrulama: `get_referencers` artık boş dönüyor; tekrar Simulate çalıştırıldı,
`LogBlueprintUserMessages`'a tek `DISMEMBER_TEST` satırı bile düşmedi.

> **Dikkat:** Bu testi tekrar kullanacaksan **ana oyun haritalarına koyma.**
> Ayrı bir test map'i aç.

---

## 2. Kurulan sistem

Kılıç bir düşmana değdiğinde isabet eden kemiğe göre farklı tepki verir.

```
BP_Sword: OnComponentBeginOverlap(DetectRange)
  -> Branch(bCanKillable AND bIsPlayerControlled)
  -> Sequence
       then_0 -> SeverLimb (Interface Message)        <-- ONCE calismali
                   self           = OtherActor         (cast YOK)
                   ImpactLocation = GetActorLocation() (kilicin konumu)
       then_1 -> Cast to BP_Enemy -> ApplyDamage(25) -> DestroyActor
                            |
BP_Enemy: Event SeverLimb(ImpactLocation)             [EventGraph]
  -> SeverWithSword(ImpactLocation)                   [fonksiyon]
       FindClosestBone(Mesh, ImpactLocation) -> kemik adi
       -> SetLastHitBone -> OnLimbSevered
```

### Kemik grupları (`OnLimbSevered`, 4 dal)

| Grup | Kemikler | Sonuç |
|---|---|---|
| Bacak (6) | LeftUpLeg, LeftLeg, LeftFoot + sağ karşılıkları | `DoLegSever`: ragdoll + 3 sn kan kaybı ölümü |
| Sol kol (4) | LeftShoulder, LeftArm, LeftForeArm, LeftHand | `bLeftArmDisabled = true` |
| Sağ kol (4) | RightShoulder, RightArm, RightForeArm, RightHand | `bRightArmDisabled = true` |
| Hayati (4) | Head, neck, head_end, headfront | `TakeDamage(99999)` |
| Gövde (4) | Hips, Spine, Spine01, Spine02 | **Kasıtlı olarak eşleşmez** — normal 25 hasara düşer |

### Kol kesilince saldırı zayıflaması (`LoopAttacking`)
- `CanAttack()` -> `NOT (bLeftArmDisabled AND bRightArmDisabled)` — iki kol giderse saldırı yok
- `GetAttackDamageScaled()` -> `AttackDamage * SelectFloat(0.5, 1.0, solKol OR sagKol)` — bir kol giderse hasar yarım

---

## 3. Değiştirilen asset'ler

| Asset | Değişiklik |
|---|---|
| `/Game/Kutun/Core/Interfaces/BPI_Dismemberable` | **YENİ.** Tek fonksiyon: `SeverLimb(ImpactLocation: Vector)`, dönüş değeri yok -> implement edende event olur |
| `/Game/Kutun/Characters/Enemies/Base/BP_Enemy` | `BPI_Dismemberable` implement ediyor. Yeni değişkenler: `bLeftArmDisabled`, `bRightArmDisabled`, `bLegSevered` (bool), `LastHitBone` (Name). Yeni fonksiyonlar: `SeverWithSword`, `OnLimbSevered`, `DoLegSever`, `BleedOutDie`, `CanAttack`, `GetAttackDamageScaled`. `C_Dismemberment` bileşeni eklendi |
| `/Game/Kutun/Weapons/Sword/BP_Sword` | EventGraph'a Sequence eklendi; `SeverLimb (Message)` cast olmadan `OtherActor`'a yollanıyor |
| `/Game/Kutun/Maps/Stand_Arena` | `BP_DismembermentRegression_C_0` silindi |
| `C_Dismemberment` bileşen şablonu | Kemik adları manken -> Mixamo eşlendi (aşağıda) |

### C_Dismemberment kemik eşlemesi
Kit varsayılan olarak **UE mankeni** adlarıyla geliyordu (`thigh_l`, `upperarm_l`,
`head`...). Bu iskelette o adların hiçbiri yok, bu yüzden **görsel uzuv kopması hiç
çalışmıyordu.** Şablon yolu:

```
/Game/Kutun/Characters/Enemies/Base/BP_Enemy.BP_Enemy_C:C_Dismemberment_GEN_VARIABLE
```

```
headBone      = Head
thighLBone    = LeftUpLeg       thighRBone    = RightUpLeg
calfLBone     = LeftLeg         calfRBone     = RightLeg
upperArmLBone = LeftShoulder    upperArmRBone = RightShoulder
lowerArmLBone = LeftForeArm     lowerArmRBone = RightForeArm

breakableBones = [RightShoulder, LeftShoulder, RightForeArm, LeftForeArm,
                  RightUpLeg, LeftUpLeg, RightLeg, LeftLeg, head]
boneHealth     = [10, 10, 6, 6, 11, 11, 12, 12, 6]   <-- DEGISTIRILMEDI
```

`boneHealth` ile `breakableBones` **index eşleşmeli** — sırayı bozma.

---

## 4. Tasarım kararları ve gerekçeleri

Bunları değiştirmeden önce gerekçeyi oku; hepsi bir hatadan sonra alındı.

1. **Dispatcher değil interface.** Dispatcher nesneden dışarı yayın yapar; burada kılıcın düşmanın içine çağrı yapması gerekiyor.
2. **`BPI_CombatTarget`'a değil, ayrı `BPI_Dismemberable`'a eklendi.** `BP_Enemy` `BPI_CombatTarget`'ı **implement etmiyor** (sadece çağırıyor) ve eklemek mevcut `ReceiveHitFeedback` fonksiyonuyla isim çakışması yapardı.
3. **Payload kemik adı değil, konum.** `OnComponentBeginOverlap`'in `SweepResult`'ı yalnızca `bFromSweep=true` iken dolu ve küre düşmanın **kapsülüne** değiyor — kapsülün kemik adı yok. Bu yüzden kemik adı her zaman `None` geliyordu. Artık düşman kendi mesh'inde `FindClosestBone` ile çözüyor; çarpışma kanalından bağımsız.
4. **`SeverLimb` hasar zincirinden ÖNCE (`then_0`).** Aksi halde `DestroyActor` önce çalışıp mesaj çöp referansa gidiyordu (`pending kill` runtime hatası).
5. **Gövde kemikleri hayati listede DEĞİL.** `FindClosestBone` en sık gövdeyi döndürüyor; dahil edilseydi neredeyse her isabet anında ölüm olurdu ve uzuv kesme hiç görünmezdi.
6. **Üst kol kiti `LeftShoulder`'a bağlı, `LeftArm`'a değil.** `PHYS_Chinese`'de `LeftArm`'ın fizik gövdesi yok; `LeftShoulder` kapsülü (yarıçap 13.6, ~47 birim) üst kolu zaten kapsıyor. `LeftArm`'a gövde eklemek iç içe geçip ragdoll'u bozardı.
7. **Ayak parmakları bacak grubunda değil.** `LeftToeBase`/`RightToeBase`'in fizik gövdesi yok, `SetAllBodiesBelowSimulatePhysics` hata verirdi.

---

## 5. Doğrulanmış ÇALIŞAN şeyler

Kaldırdığımız regresyon testinin son koşusu runtime kanıtı bıraktı:

```
PASS Mongol_RightForeArm / LeftUpLeg / Head   (+ _hidden varyantlari)
PASS Chinese_LeftArm / RightForeArm / LeftUpLeg / Head
PASS 12_visual_limbs          <- gorsel uzuvlar spawn oluyor
PASS no_duplicate_limbs
PASS Mongol_bleedout / Bizans_bleedout / Chinese_bleedout
```

Yani kemik çözümü, uzuv kesme, görsel uzuv spawn'ı ve 3 saniyelik kan kaybı ölümü
**çalışıyor**.

Başarısız olan üçü beklenen durumlar:
- `Chinese_Spine`, `Bizans_Spine` FAIL -> gövdeyi hayati listeden kasıtlı çıkardık (karar 5)
- `Bizans_*_hidden` FAIL -> `SK_Bizans`'ın iskeleti yok (aşağı bak)

---

## 6. Açık sorunlar

### 6.1 "15 öldürme" sayacı — ÇÖZÜLDÜ
Aynı test aktöründen geliyormuş. Test, 3 düşman tipini (Mongol, Bizans, Çinli)
birkaç kemikten kesiyor ve **uzuv kesilince düşman ölüyor**; üstüne 3 bleedout
testi ekleniyor. Toplam 13-16 ölüm — rapor edilen "15" tam oraya düşüyor.

Yani bölüm 1'deki test aktörünün kaldırılması bu belirtiyi de çözdü.

**Geriye kalan küçük soru:** `get_referencers` L_Trailer'ın test aktörüne referans
vermediğini gösterdi. Sayaç L_Trailer'da görüldüyse ya ölçüm Stand_Arena'da
yapılmıştır ya da **öldürme sayacı seviyeler arasında sıfırlanmıyordur**. İkincisi
ayrı ve küçük bir hata olur; L_Trailer açılıp sayacın 0'dan başladığı teyit
edilmeli. Doğrulanmadı.

### 6.2 `SK_Bizans` riglenmemiş
```
SK_Bizans kemikleri: RootNode, Mesh_0    <- gercek iskelet yok
```
Bizans'ta uzuv kesme de ragdoll da çalışamaz. `BP_EnemySpawner`'ın
`enemyClasses` dizisinde **hâlâ var** — spawn ediliyor.

### 6.3 Fizik varlıklarında eksik gövdeler
```
PHYS_Chinese  : LeftArm, RightArm, LeftHand, RightHand govdesi YOK
PHYS_Mongol   : Spine, neck govdesi YOK (LeftArm/RightArm VAR)
Her ikisi     : LeftToeBase, RightToeBase, head_end, headfront YOK
```
Şu anki eşleme bunlardan kaçınıyor, ama kiti `LeftArm`'dan kesmeye yönlendirirsen
"Invalid Bodies" hatası alırsın.

### 6.4 Kit `boneHealth` ile gameplay senkron değil
Kit uzvu kopartmak için kemik başına **6–12 birikmiş hasar** istiyor; `OnLimbSevered`
ise **ilk isabette** tepki veriyor. Yani bacak hemen ragdoll olurken görsel kopma
daha sonra gelir. **Hizalanması gerekiyor.**

### 6.5 Debug çıktısı hâlâ açık
`BP_Enemy:SeverWithSword` içinde kemik adını 4 saniye ekrana basan bir
`PrintString` var. Kaldırılmalı.

### 6.6 BP_Sword'de gereksiz interface
`BP_Sword`'e `BPI_Dismemberable` eklenmiş. Gönderenin interface'i implement
etmesine gerek yok — Class Settings'ten çıkarılabilir.

### 6.7 Kılıç hasarı / can dengesi
Kılıç 25 hasar, `UC_HealthComponent` varsayılanı 100 can = 4 vuruş. Kullanıcı
düşmanların tek vuruşta öldüğünü bildirmişti; `BP_Enemy`'nin bileşenindeki gerçek
`MaxHealth` okunamadı (SCS şablonunda). Doğrulanmalı.

---

## 7. MCP ile çalışırken bilinmesi gerekenler

Bu oturumda acı çekilerek öğrenildi:

- `write_graph_dsl` grafiği **temizlemez**. Üzerine yazarsan eski node'lar bağlantısız ada olarak kalır. Temiz sonuç için fonksiyonu `remove_function_graph` + `compile_blueprint` + `add_function_graph` ile sıfırdan kur (araya compile şart, yoksa ad `X_0` olur).
- `write_graph_dsl` **return node oluşturamaz** (`|AddReturnNode... does not exist`). Çıkışı olan fonksiyonları `create_node` + `connect_pins` ile elle kur.
- MCP **interface override grafiği oluşturamaz** ve bir Blueprint'e **interface ekleyemez**. Bunlar editörde elle yapılır.
- `BP_Enemy` üzerinde `compile_blueprint` sürekli `REINST_BP_Enemy_C_0` hatası verir ama **yazma başarılı olur** — `read_graph_dsl` ile doğrula, hataya güvenme.
- DSL'de `and`/`or`/`not`/`*` ve `(select cond a b)` yerleşik operatörler; ayrı node tipi aramaya gerek yok.
- Bileşen şablonu yolu: `<BP>.<BP>_C:<BilesenAdi>_GEN_VARIABLE`
- Mevcut DSL grameri için `get_graph_dsl_docs` çağır.

---

## 8. Sıradaki iş

1. **Kit `boneHealth` ile gameplay'i hizala** (6.4) — en büyük tasarım açığı
2. `PrintString`'i kaldır (6.5)
3. Kılıç hasarı / can dengesini doğrula (6.7)
4. `BP_Sword`'den gereksiz interface'i çıkar (6.6)
5. Bizans'ı ya rigle ya spawner listesinden çıkar (6.2)
6. L_Trailer'da öldürme sayacının 0'dan başladığını teyit et (6.1)

Oyun içi tam test (kılıcı fırlatıp bacağa/kola/kafaya isabet) **hiç yapılmadı**;
elimizdeki tek runtime kanıtı silinen regresyon testinin logları.

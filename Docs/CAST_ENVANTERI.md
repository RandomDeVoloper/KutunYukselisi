# Cast Envanteri ve Dönüşüm Sırası

**Durum: Bug düzeltmelerinden sonraya ertelendi.** Kullanıcının 17 Kasım 2026 kararıdır. Aşağıdaki sıralama, cast işlerine dönüldüğünde kullanılacak; şu an açık bug'lar önceliklidir.

Tarih: 17 Kasım 2026. Taban: a0b11da. Çalışma dalı: codex/animation-preview-reference.

## Kapsam ve sonuç

- /Game altında bulunan 84 Blueprint türevi asset: normal, widget, animasyon, interface ve Control Rig Blueprint'leri dahil.
- Bu asset'lerde 625 graph; ayrıca Stand_Arena, L_Trailer ve L_Main3DMenu içindeki 4 Level Blueprint graph'ı: toplam 629 graph. Üç Level Blueprint'te cast bulunmadı.
- /Game/FogArea/Maps/Overview yüklendi; bellekte LevelScriptBlueprint'i bulunmadı. Oba_L bir World değil, ObjectRedirector olarak doğrulandı.
- K2Node_DynamicCast ve alt sınıfları tarandı. K2Node_ClassDynamicCast bu sınıftan türediği için sınıf cast'leri de kapsama girer. Sayısal tür dönüşümleri bu listenin konusu değildir. Engine ve eklenti içerikleri /Game taramasına dahil değildir.
- HUD ve scope'taki iki Cast To BPI_Interactable kaldırıldı. Güncel kalan: **51 cast**, bunların **11'i Cast To BP_Telekinezi**.
- Graph listeleri çökmüş/kollapslı alt graph'ları ve animasyon geçişlerini de içerir. Kalan satırların tümü düğüm düzeyinde listelenmiştir; bağlı pin bulunması runtime erişilebilirlik kanıtı sayılmaz. Ölü kod veya asset silinmedi.

## Bu parçada yapılan düzeltme

WBP_Hud:EventGraph ve WBP_Scope:UpdateCrosshair içinde vurulan aktör, Does Object Implement Interface(BPI_Interactable) ile kontrol edilir. True dalı yeşil (0,1,0,1), false ve hit olmayan dal beyaz (1,1,1,1). İki graph'ta da dynamic cast sayısı sıfır. İki widget warnings_as_errors=true ile derlendi ve kaydedildi.

Son canlı test çağrısı Play öncesi genel Blueprint derlemesinde ABP_Unarmed hatasına takıldı; görsel yeşile geçiş testi tamamlandı sayılmıyor. Widget derlemeleri temiz. Bu global hata rapordaki BROKEN grubunda ayrıca izlenir.

## Cast hedeflerine göre sayı

| Hedef | Adet |
|---|---:|
| BP_Telekinezi | 11 |
| Character | 9 |
| BP_StandGameMode | 7 |
| UC_HealthComponent | 7 |
| SG_Settings | 4 |
| BP_Enemy | 2 |
| LevelSequenceActor | 2 |
| BP_ProjectileBase | 2 |
| PlayerController | 2 |
| Badcastnode | 1 |
| MaterialInterface | 1 |
| BP_Sword | 1 |
| Actor | 1 |
| BP_SwordMount | 1 |

## Öncelikli: Cast To BP_Telekinezi

| Kimlik | Kaynak ve graph | Kullanılan bilgi/işlem | Dönüşüm grubu |
|---|---|---|---|
| CAST-009 | `Kutun/Characters/Enemies/Base/BP_Enemy:IsPlayerInCinematic` | |GetbIsCinematicActive | CIN |
| CAST-015 | `Kutun/Characters/Player/Animations/ABP_Telekinezi:EventGraph` | |GetbIsTelekinesis | ANIM |
| CAST-027 | `Kutun/Core/Components/UC_HealthComponent:ShowHealthBarIfMatchRunning` | |GetbIsCinematicActive | CIN |
| CAST-031 | `Kutun/UI/Widgets/WBP_Options:SaveMouseSens` | |SetMouseSensitivity, |SetbMouseSensLoaded | SET |
| CAST-033 | `Kutun/UI/Widgets/WBP_PauseMenu:EventGraph` | MouseSens|SaveMouseSensitivity | SET |
| CAST-034 | `Kutun/UI/Widgets/WBP_PauseMenu:EventGraph` | MouseSens|SaveMouseSensitivity | SET |
| CAST-035 | `Kutun/UI/Widgets/WBP_PauseMenu:InitMouseSens` | |GetbMouseSensLoaded, MouseSens|LoadMouseSensitivity, |GetMouseSensitivity | SET |
| CAST-039 | `Kutun/UI/Widgets/WBP_Timer:EventGraph` | |GetSouls | STATS |
| CAST-045 | `Kutun/Weapons/Sword/BP_Sword:EventGraph` | |GetMesh | SWORD |
| CAST-046 | `Kutun/Weapons/Sword/BP_Sword:EventGraph` | |GetMesh | SWORD |
| CAST-047 | `Kutun/Weapons/Sword/BP_Sword:EventGraph` | |SetbReturning?, |SetbSwordOnHand | SWORD |

## Küçük parçalara ayrılmış uygulama sırası

1. Tamamlandı: HUD/scope hedef kontrolündeki iki interface cast'i kaldırıldı.
2. Önce BROKEN şablon derleme hatasının kapsamını doğrula; genel Play testini engelliyorsa ayrı küçük düzeltmeyle gider.
3. CIN: sağlık ve düşmandaki iki BP_Telekinezi cast'ini ortak sinematik sözleşmesine taşı.
4. SET: PauseMenu/Options içindeki dört BP_Telekinezi cast'ini ayar sözleşmesine taşı.
5. STATS: Timer içindeki tek BP_Telekinezi cast'ini BPI_Stats/dispatcher'a taşı.
6. SWORD: kılıçtaki üç BP_Telekinezi cast'ini soket/durum sözleşmesine taşı.
7. ANIM: animasyondaki tek BP_Telekinezi cast'ini durum sözleşmesine taşı; geçerli referans ve animasyon testlerini tekrar çalıştır.
8. Kalan proje ve motor cast'lerini aşağıdaki gruplarla tek tek ele al. Her parçada önce endpoint'leri ekle/derle, sonra tüketicileri geçir/derle; ilgili oynanış testinden sonra ilerle.

## Dönüşüm sözleşmeleri

- **CIN:** BPI_CinematicState üzerinden IsCinematicActive sorgusu; değişim bildirimi gerekiyorsa OnCinematicStateChanged dispatcher. Sağlık ve AI aynı sözleşmeyi kullanmalı.
- **SET:** BPI_PlayerSettings veya ayar bileşeninden hassasiyet sorgula/güncelle/kaydet; doğrudan pawn alanı yazma. Başlangıç yüklemesi ve iki menünün aynı değeri göstermesi test edilmeli.
- **SWORD:** Önce mevcut BPI_SwordHolder/BPI_SwordOwner ve SetSwordState imzalarını doğrula. Soket/attachment transformunu interface ile sorgula; kılıç durumunu interface mesajı veya dispatcher ile bildir.
- **STATS:** Mevcut BPI_Stats sözleşmesini doğrula; Souls değerini interface üzerinden sorgula veya OnSoulsChanged dispatcher ile HUD'u güncelle.
- **ANIM:** Telekinezi durumunu interface sorgusu ya da oyuncu durum bileşeni/dispatcher üzerinden animasyon instance'ına aktar. Initialize/Update geçerlilik kontrollerini koru; koşma, zıplama ve surfing regresyon testi yap.
- **BROKEN:** ABP_Unarmed içindeki kayıp BP Third Person Character hedefini ve referanslarını doğrula. Taramada bozuk cast bulundu; Play öncesi genel derleme de ABP_Unarmed hatası bildirdi. Şablonu otomatik silme veya rastgele sınıfa bağlama.
- **MATCH:** Maç sorgularını match interface/bileşenine, kill ve başlangıç/bitiş bildirimlerini dispatcher veya interface mesajına taşı.
- **HEALTH:** GetComponentByClass sonrası typed bileşen referansını koru veya ortak sağlık interface'i kullan; hasar/ölüm bildirimleri mevcut health dispatcher'larından gelmeli.
- **SAVE:** SaveGame erişimini tek ayar/kayıt katmanında topla; tüketici widget'lar SaveGame sınıfını cast etmesin. Kayıt okuma ve yeniden açma davranışını test et.
- **COMBAT:** Mevcut BPI_CombatTarget/BPI_Interactable sözleşmelerini doğrula; sınıf kontrolü yerine yetenek sorgusu ve interface mesajı kullan.
- **PROJECTILE:** Çarpılan nesnenin yeteneğini interface ile sorgula; etki/hasar olaylarını ortak sözleşmeden bildir.
- **SURF:** Mevcut BPI_Surfing/BPI_SwordOwner imzalarını doğrula; mount durumunu interface/dispatcher ile yönet.
- **SEQ:** Sequence actor/player referansını sahne director'ından typed olarak al; ilk aktörü bul/cast et modelini kaldır. 22/40 saniye ve boş sonuç korumaları korunmalı.
- **NATIVE:** Character/PlayerController/Actor/MaterialInterface cast'lerini ayrı değerlendir. Typed API/ref ile gereksiz cast'i kaldır; yetenek sorgusu gerekiyorsa interface kullan. Bir cast'i aynı somut sınıf bağımlılığını başka node'a taşıyarak kapatılmış sayma.

## Tüm kalan düğümler

Düğüm yolu tam ve kopyalanabilirdir. Planlar adaydır; imzalar ve runtime kullanım her değişiklikten önce doğrulanmalıdır.

| Kimlik | Öncelik | Grup | Hedef | Düğüm yolu |
|---|---|---|---|---|
| CAST-001 | P3 | NATIVE | Character | `/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed.ABP_Unarmed:EventGraph.K2Node_DynamicCast_0` |
| CAST-002 | P0 | BROKEN | Badcastnode | `/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed.ABP_Unarmed:EventGraph.K2Node_DynamicCast_1` |
| CAST-003 | P3 | NATIVE | Character | `/Game/CombatMagicAnims/Demo/Mannequins/Anims/Unarmed/ABP_Retarget.ABP_Retarget:EventGraph.K2Node_DynamicCast_0` |
| CAST-004 | P3 | NATIVE | MaterialInterface | `/Game/FogArea/Blueprints/BP_FogArea.BP_FogArea:CreateMID.K2Node_DynamicCast_0` |
| CAST-005 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Enemies/Base/ABP_Enemy.ABP_Enemy:EventGraph.K2Node_DynamicCast_0` |
| CAST-006 | P2 | COMBAT | BP_Enemy | `/Game/Kutun/Characters/Enemies/Base/ABP_Enemy.ABP_Enemy:EventGraph.K2Node_DynamicCast_3` |
| CAST-007 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/Characters/Enemies/Base/BP_Enemy.BP_Enemy:EventGraph.K2Node_DynamicCast_0` |
| CAST-008 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/Characters/Enemies/Base/BP_Enemy.BP_Enemy:EventGraph.K2Node_DynamicCast_2` |
| CAST-009 | P1 | CIN | BP_Telekinezi | `/Game/Kutun/Characters/Enemies/Base/BP_Enemy.BP_Enemy:IsPlayerInCinematic.K2Node_DynamicCast_0` |
| CAST-010 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Enemies/Bizans/Animations/ABP_Bizans.ABP_Bizans:EventGraph.K2Node_DynamicCast_0` |
| CAST-011 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Enemies/Chinese/Animations/ABP_Chinese.ABP_Chinese:EventGraph.K2Node_DynamicCast_0` |
| CAST-012 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Enemies/Chinese/Animations/ABP_Chineses.ABP_Chineses:EventGraph.K2Node_DynamicCast_0` |
| CAST-013 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Enemies/Mongol/Animations/ABP_Mongol.ABP_Mongol:EventGraph.K2Node_DynamicCast_0` |
| CAST-014 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Player/Animations/ABP_Telekinezi.ABP_Telekinezi:EventGraph.K2Node_DynamicCast_0` |
| CAST-015 | P1 | ANIM | BP_Telekinezi | `/Game/Kutun/Characters/Player/Animations/ABP_Telekinezi.ABP_Telekinezi:EventGraph.K2Node_DynamicCast_2` |
| CAST-016 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EmergencyRespawn.K2Node_DynamicCast_2` |
| CAST-017 | P2 | SEQ | LevelSequenceActor | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EndCinematic.K2Node_DynamicCast_0` |
| CAST-018 | P2 | SWORD | BP_Sword | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EventGraph.K2Node_DynamicCast_0` |
| CAST-019 | P2 | SEQ | LevelSequenceActor | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EventGraph.K2Node_DynamicCast_1` |
| CAST-020 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EventGraph.K2Node_DynamicCast_3` |
| CAST-021 | P2 | PROJECTILE | BP_ProjectileBase | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:EventGraph.K2Node_Composite_12.Sets.K2Node_DynamicCast_0` |
| CAST-022 | P2 | SAVE | SG_Settings | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:LoadMouseSensitivity.K2Node_DynamicCast_0` |
| CAST-023 | P2 | SAVE | SG_Settings | `/Game/Kutun/Characters/Player/BP_Telekinezi.BP_Telekinezi:SaveMouseSensitivity.K2Node_DynamicCast_0` |
| CAST-024 | P3 | NATIVE | Character | `/Game/Kutun/Characters/Uldiz/Animations/ABP_ULDIZ.ABP_ULDIZ:EventGraph.K2Node_DynamicCast_0` |
| CAST-025 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/Cinematics/CaveOpening/BP_CutsceneDirector.BP_CutsceneDirector:FinishHandoff.K2Node_DynamicCast_0` |
| CAST-026 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/Core/Components/UC_HealthComponent.UC_HealthComponent:ShowHealthBarIfMatchRunning.K2Node_DynamicCast_5` |
| CAST-027 | P1 | CIN | BP_Telekinezi | `/Game/Kutun/Core/Components/UC_HealthComponent.UC_HealthComponent:ShowHealthBarIfMatchRunning.K2Node_DynamicCast_6` |
| CAST-028 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Core/GameMode/BP_StandGameMode.BP_StandGameMode:BeginStandMatch.K2Node_DynamicCast_0` |
| CAST-029 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Gameplay/BP_DeathZone.BP_DeathZone:EventGraph.K2Node_DynamicCast_3` |
| CAST-030 | P2 | SAVE | SG_Settings | `/Game/Kutun/UI/Widgets/WBP_Options.WBP_Options:InitMouseSens.K2Node_DynamicCast_2` |
| CAST-031 | P1 | SET | BP_Telekinezi | `/Game/Kutun/UI/Widgets/WBP_Options.WBP_Options:SaveMouseSens.K2Node_DynamicCast_1` |
| CAST-032 | P2 | SAVE | SG_Settings | `/Game/Kutun/UI/Widgets/WBP_Options.WBP_Options:SaveMouseSens.K2Node_DynamicCast_2` |
| CAST-033 | P1 | SET | BP_Telekinezi | `/Game/Kutun/UI/Widgets/WBP_PauseMenu.WBP_PauseMenu:EventGraph.K2Node_DynamicCast_0` |
| CAST-034 | P1 | SET | BP_Telekinezi | `/Game/Kutun/UI/Widgets/WBP_PauseMenu.WBP_PauseMenu:EventGraph.K2Node_DynamicCast_1` |
| CAST-035 | P1 | SET | BP_Telekinezi | `/Game/Kutun/UI/Widgets/WBP_PauseMenu.WBP_PauseMenu:InitMouseSens.K2Node_DynamicCast_1` |
| CAST-036 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/UI/Widgets/WBP_Restart.WBP_Restart:EventGraph.K2Node_DynamicCast_1` |
| CAST-037 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/UI/Widgets/WBP_Result.WBP_Result:EventGraph.K2Node_DynamicCast_2` |
| CAST-038 | P2 | MATCH | BP_StandGameMode | `/Game/Kutun/UI/Widgets/WBP_StandHUD.WBP_StandHUD:EventGraph.K2Node_DynamicCast_4` |
| CAST-039 | P1 | STATS | BP_Telekinezi | `/Game/Kutun/UI/Widgets/WBP_Timer.WBP_Timer:EventGraph.K2Node_DynamicCast_4` |
| CAST-040 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Weapons/Axe/BP_Axe.BP_Axe:ApplyAxeDamage.K2Node_DynamicCast_1` |
| CAST-041 | P2 | PROJECTILE | BP_ProjectileBase | `/Game/Kutun/Weapons/Balbal/BP_ProjectileBase.BP_ProjectileBase:EventGraph.K2Node_DynamicCast_0` |
| CAST-042 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Weapons/BP_Throwable.BP_Throwable:TryDealDamage.K2Node_DynamicCast_2` |
| CAST-043 | P3 | NATIVE | Actor | `/Game/Kutun/Weapons/Sword/BP_Sword.BP_Sword:EventGraph.K2Node_DynamicCast_0` |
| CAST-044 | P2 | COMBAT | BP_Enemy | `/Game/Kutun/Weapons/Sword/BP_Sword.BP_Sword:EventGraph.t2_DynamicCast_1` |
| CAST-045 | P1 | SWORD | BP_Telekinezi | `/Game/Kutun/Weapons/Sword/BP_Sword.BP_Sword:EventGraph.t5_DynamicCast_1` |
| CAST-046 | P1 | SWORD | BP_Telekinezi | `/Game/Kutun/Weapons/Sword/BP_Sword.BP_Sword:EventGraph.t9_DynamicCast_1` |
| CAST-047 | P1 | SWORD | BP_Telekinezi | `/Game/Kutun/Weapons/Sword/BP_Sword.BP_Sword:EventGraph.t9_DynamicCast_2` |
| CAST-048 | P3 | NATIVE | PlayerController | `/Game/Kutun/Weapons/SwordMount/BP_SwordMount.BP_SwordMount:EventGraph.K2Node_DynamicCast_1` |
| CAST-049 | P3 | NATIVE | PlayerController | `/Game/Kutun/Weapons/SwordMount/BP_SwordMount.BP_SwordMount:EventGraph.K2Node_DynamicCast_2` |
| CAST-050 | P2 | HEALTH | UC_HealthComponent | `/Game/Kutun/Weapons/SwordMount/BP_SwordMount.BP_SwordMount:MountTryDealDamage.K2Node_DynamicCast_2` |
| CAST-051 | P2 | SURF | BP_SwordMount | `/Game/ThirdPerson/Blueprints/BP_ThirdPersonPlayerController.BP_ThirdPersonPlayerController:EventGraph.K2Node_DynamicCast_0` |

Makineyle işlenebilir eş dosya: [CAST_ENVANTERI.json](CAST_ENVANTERI.json).


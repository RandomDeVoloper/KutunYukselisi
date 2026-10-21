# Blueprint Denetimi — Bulgular

**Tarih:** 21 Ekim 2026
**Yöntem:** Unreal MCP (`BlueprintTools`, `AssetTools`) — editör açık, canlı proje üzerinde ölçüldü
**Durum:** Faz 1–3 tamam. Faz 4 (düzeltmeler) bekliyor.

---

## Özet Tablo

| Blueprint | Graph | Toplam Node | Ölü Node | Değerlendirme |
|-----------|-------|-------------|----------|---------------|
| BP_Telekinezi | 48 | **1114** | 21 (EventGraph) | Çok büyük — bölünmeli |
| BP_Axe | 10 | 217 | 1 | Temiz |
| BP_Enemy | 11 | 166 | 0 | Temiz ama 3 ölü üye var |
| UC_HealthComponent | 8 | 50 | 0 | Temiz |
| BP_EnemySpawner | 6 | 72 | — | Temiz |
| BP_EnemySpawn_Konsta | 3 | 20 | — | Eski, kullanılmıyor |
| BP_EnemySpawn_Mongol | 3 | 20 | — | Eski, kullanılmıyor |

---

## Faz 2 — Blueprint Taraması

### BP_Telekinezi — 1114 node, 48 graph

**EventGraph: 320 node, 29 giriş noktası.** Tek bir graph'ta 29 ayrı event var; asıl karmaşıklık kaynağı bu.

En büyük graph'lar:

| Graph | Node | Tip |
|-------|------|-----|
| EventGraph | 320 | event |
| PUSHSWORD | 84 | kollapslı |
| UpdateObjectScale | 84 | fonksiyon |
| S_ScaleUP/Down | 77 | kollapslı |
| MATERIALCHANGE | 60 | kollapslı |
| UpdateCrush | 50 | fonksiyon |

**Ölü node: 21 adet** (EventGraph içinde, hiçbir event'ten erişilemiyor):

```
CreateWidget_1, CreateWidget_7, CreateWidget_8, CreateWidget_10
CallFunction_33, _35, _58, _67, _148, _149, _152, _153
VariableGet_10, _16, _39, _43
VariableSet_2, _36, _37
MacroInstance_11, Knot_10
```

Dört adet `CreateWidget` + onları saklayan `VariableSet`'ler — **eski HUD oluşturma zinciri**. Her birinin yerini alan canlı yol doğrulandı:

| Ölü node | Oluşturduğu widget | Yerini alan |
|----------|-------------------|-------------|
| `CreateWidget_1` | WBP_Hud | `EnsureAimHud` fonksiyonu |
| `CreateWidget_7` | WBP_Hud | `EnsureAimHud` fonksiyonu |
| `CreateWidget_8` | WBP_HudGrab | `EnsureGrabHud` fonksiyonu |
| `CreateWidget_10` | WBP_Restart | `UC_HealthComponent.Die` |

`WBP_Restart` özellikle kontrol edildi: ölüm ekranı artık `UC_HealthComponent.Die` içindeki `CreateWidget_4`'ten geliyor ve `UC_HealthComponent`'in bağımlılık listesinde `WBP_Restart` var. Yani BP_Telekinezi'deki kopya gerçekten gereksiz.

Ada yapısı da doğrulandı — örnek zincir: `CallFunction_152 → CreateWidget_7 → VariableSet_36`, hiçbir event'e bağlı değil.

> **Ölçüm notu:** Kollapslı (composite) graph'ların giriş düğümü `K2Node_Tunnel`, ve `find_nodes(entry_points_only=true)` bunu giriş olarak döndürmüyor. Bu yüzden kollapslı graph'ların içindeki ölü node sayısı **ölçülemedi** — oradaki sayılar yanlış pozitif olduğu için tabloya alınmadı.

---

### BP_Enemy — 166 node, 11 graph, 0 ölü node

Graph yapısı temiz, kollapslı graph yok. Sorun node'larda değil, **ölü üyelerde**:

| Üye | Tip | BP_Enemy içi kullanım | Dışarıdan kullanım | Karar |
|-----|-----|----------------------|-------------------|-------|
| `CameraBoom` | SpringArmComponent | 0 | 0 | **SİL** |
| `MaxEnemies` | number | 0 | 0 | **SİL** |
| `CurrentSpawns` | number | 0 | 0 | **SİL** |
| `Spawner` | Object | 0 | Konsta + Mongol spawner yazıyor | **BIRAK** |

`CameraBoom` oyuncudan kopyalanmış bir SpringArm — AI düşmanda hiçbir işi yok, hiçbir graph'ta referansı da yok. Güvenle silinebilir.

`Spawner` BP_Enemy içinde **hiç okunmuyor** ama `BP_EnemySpawn_Konsta` ve `BP_EnemySpawn_Mongol` ona yazıyor. Yani write-only bir değişken: veri akışı ölü, ama silmek o iki spawner'ın derlemesini bozar. İkisi de kullanılmayan eski spawner'lar — önce onlar temizlenirse `Spawner` da gidebilir.

Ayrıca `Spawner` tipi generic `Object`, `BP_EnemySpawner` değil. Her kullanımda cast gerekir.

**Yöntem doğrulaması:** aynı tarama bilinen-kullanılan üyelerde beklendiği gibi sonuç verdi (`bIsDead`=3, `AttackDamage`=1, `Health`=2, `Sphere`=2), yani 0 sonuçlar gerçek.

---

### BP_Axe — 217 node, 1 ölü node

**CLAUDE.md'deki "323 ölü node" notu güncel değil.** Ölçüm: toplam 217 node, tek bir kopuk `K2Node_Self_0` (`Equip` fonksiyonunda). Temizlik görünüşe göre zaten yapılmış. CLAUDE.md düzeltilmeli.

---

### UC_HealthComponent — 50 node, 0 ölü node

8 graph: `TakeDamage`, `Heal`, `Die`, `EventGraph` + 4 dispatcher (`OnHealthChanged`, `OnDepleted`, `OnDeath`, `OnDamaged`). Bağımsız ve temiz. Bileşen mimarisi doğru kurulmuş.

---

## Faz 3 — Hard Referans Haritası

`BP_Telekinezi` 38 adet `/Game` asset'ine **hard** referans veriyor. Yani oyuncu belleğe girdiğinde hepsi beraberinde yükleniyor.

### Kritik bulgular

**1. Oyuncu ↔ Düşman döngüsel bağımlılığı**

```
BP_Telekinezi  ──hard──>  BP_Enemy
BP_Enemy       ──hard──>  BP_Telekinezi
```

Oyuncuyu yüklemek düşmanı, mesh'ini ve anim blueprint'ini de yüklüyor; tersi de geçerli. Proje `BPI_CombatTarget` arayüzüne zaten sahip — `Cast To BP_Enemy` yerine arayüz mesajı kullanmak bu bağı koparır. Bu en yüksek getirili tek düzeltme.

**2. Engine editör içeriği oyun yolunda — iki yerde**

```
/Engine/VREditor/Sounds/UI/Camera_Shutter.Camera_Shutter
```

| Graph | Node | Pin |
|-------|------|-----|
| `CrushHeldObject` (fonksiyon) | `K2Node_CallFunction_21` | `Sound` |
| `S_ScaleUP/Down` (kollapslı) | `K2Node_CallFunction_7` | `Sound` |

Crush sesi Engine'in **VREditor eklentisinden** geliyor. VREditor editör eklentisi — paketlenmiş build'de cook edilmeme riski var.

**Ancak yerine koyacak bir asset yok.** `Kutun/Audio/SFX` tamamı kılıç sesi (`SW_Sword_*`, `SW_Woosh`), `Kutun/Audio/UI` ise menü sesi. Crush/çarpma/kırılma sesi hiç yok. Yani bu bir **sanat ajanı görevi**: önce ses üretilmeli, sonra iki pin değiştirilmeli. `set_pin_value` kollapslı graph'ta da çalıştığı için değişiklik MCP'den yapılabilir.

**3. Editör modülü bağımlılığı**

`/Script/UMGEditor` runtime bir Blueprint'in bağımlılık listesinde. Genelde zararsız ama bir editör-only node'un graph'ta kaldığına işaret eder.

**4. `WBP_ScaleAxes` — ilk şüphe yanlıştı**

`WBP_ScaleAxes` **kullanılıyor**: `UpdateScaleAxesHud` fonksiyonundaki `CreateWidget_0` onu oluşturuyor. Yani silinecek bir referans değil.

Yine de açık bir soru kalıyor: CLAUDE.md'ye göre eksen göstergesi `WBP_HudGrab` içindeki `HB_Axes`'e taşınmıştı. Şu an **iki ayrı eksen HUD'u** var gibi görünüyor — `UpdateScaleAxesHud`'un hâlâ çağrıldığı editörde kontrol edilmeli.

### Tam bağımlılık listesi (/Game)

**Input (10):** IA_Copy, IA_Jump, IA_Look, IA_Move, IA_ScaleDown, IA_ScaleUp, IA_Telekinesis, IA_SimulatePHY, IA_SwordThrow, IA_Pause, IA_MouseLook, BPI_TouchInterface
**Karakter (3):** SK_Kam, ABP_Telekinezi, BP_Enemy
**Silah (5):** BP_Throwable, BP_Sword, BP_Axe, BP_ProjectileBase
**UI (7):** WBP_Hud, WBP_HudGrab, WBP_Restart, WBP_LoadingScreen, WBP_PauseMenu, WBP_ScaleAxes, WBP_Timer
**Core (6):** UC_HealthComponent, BPI_Interactable, BPI_GameInteractions, BPI_CombatTarget, BPI_SwordHolder, SG_Settings
**Ses/VFX (4):** SW_Amb_DoorHumDrone, SW_Woosh, CS_Crush, Camera_Shutter (Engine)

---

## Faz 4 — Düzeltme Listesi

> **Engel:** Editör `main` checkout'unda açık ve orada commit edilmemiş 5 asset var
> (`BP_Telekinezi`, `BP_Axe`, `BP_Throwable`, `Stand_Arena`, `MI_Mountain`).
> MCP ile yapılan her asset değişikliği bu worktree'ye değil **main'e** yazılır ve
> o yarım işin üstüne biner. Binary asset merge edilemediği için sonradan ayrılamaz.
> **Asset düzeltmeleri başlamadan önce main'deki iş commit edilmeli.**

### Alfa öncesi

| # | İş | Nasıl | Risk |
|---|----|----|------|
| 1 | `BP_Enemy` → `MaxEnemies` + `CurrentSpawns` sil | MCP `remove_variable` | Yok — 9 Blueprint tarandı, 0 referans |
| 2 | `BP_Enemy` → `CameraBoom` sil | **Elle, editörde** | Yok — 0 referans, alt bileşeni yok |
| 3 | Crush sesi üret, sonra 2 pin değiştir | Sanat → MCP `set_pin_value` | Asset yok, önce üretilmeli |

**Neden CameraBoom elle:** bileşenler `list_variables`'ta görünmüyor (sadece `Spawner`, `MaxEnemies`, `CurrentSpawns`, `bIsDead`, `AttackDamage`, `AttackRange`, `AttackInterval`, `AttackTimer`, `HitFlashMID`, `HitFlashPrevOverlay`, `AttackAnim`, `AttackAnimRate` dönüyor). `remove_variable` bir SCS bileşenini kaldıramaz — Components panelinden silinmeli.

### Beta öncesi

| # | İş | Not |
|---|----|-----|
| 4 | `Cast To BP_Enemy` → `BPI_CombatTarget` | Döngüsel bağımlılığı koparır, en yüksek getiri |
| 5 | EventGraph'taki 21 ölü node'u sil | Yerini alan yollar doğrulandı; main temizlendikten sonra |
| 6 | EventGraph'ı böl | 29 giriş tek graph'ta fazla — input / HUD / combat |
| 7 | `UpdateScaleAxesHud` hâlâ çağrılıyor mu? | İki eksen HUD'u olabilir |

### İzle (dokunma)

8. `Spawner` değişkeni — `BP_EnemySpawn_Konsta` + `_Mongol` yazıyor, onlar temizlenince gider
9. `MATERIALCHANGE` kollapslı graph'ı — çalışıyor, refactor elle + Play testi
10. Kollapslı graph içi ölü node'lar — MCP ölçemiyor (Tunnel entry dönmüyor), editörde bak

### Ölçümün kapsamadığı yerler

- **Haritalar ve level Blueprint'leri** taranmadı (`Oba_L`, `L_Niyazi`, `Stand_Arena`) — `BP_Enemy` üyelerini oradan okuyan bir şey varsa görülmedi. Silme sonrası derleme hatası çıkarsa kaynak orasıdır.
- **`ABP_Enemy`** (Animation Blueprint) taranmadı.
- Ölçüm main'deki **commit edilmemiş** BP_Telekinezi üzerinde yapıldı — 21 ölü node'un bir kısmı yarım kalmış aktif iş olabilir.

---

## Düzeltilecek Belge Notları

- **CLAUDE.md:** "`BP_Axe` had collected 323 dead nodes" → artık geçerli değil (217 node, 1 kopuk). Güncellenmeli.
- **CLAUDE.md:** `BP_Enemy`'de `CameraBoom` olduğu notu doğrulandı. Silindikten sonra not da kaldırılmalı.

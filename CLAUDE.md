# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

"ISIK" (repo: KutunYukselisi) is an Unreal Engine 5.8 game (`EngineAssociation: 5.8` in `ISIK.uproject`). It is a **Blueprint-only project in practice**: `Source/ISIK` is empty, there is no C++ game module, and no build/lint/test commands exist. All gameplay logic lives in `.uasset`/`.umap` binaries under `Content/`, which cannot be meaningfully read or diffed as text — edit them through the Unreal Editor (or the Unreal MCP server, see below), not with file tools.

## Working with the project

- Open `ISIK.uproject` in the Unreal Editor (5.8). Editor startup map: `/Game/Levels/L_Tutorial_New`. Packaged-game default map: `/Game/Levels/L_Main3DMenu`.
- `.mcp.json` registers an `unreal-mcp` HTTP server at `http://127.0.0.1:8000/mcp`. It is served by the editor's `ModelContextProtocol` / `ToolsetRegistry` / `AllToolsets` plugins, so the **editor must be running** for it to connect (otherwise `ECONNREFUSED`). Use it to inspect/modify Blueprints and levels.
- `Binaries/`, `Intermediate/`, `DerivedDataCache/`, `Saved/` are generated; do not edit.
- Git history shows commits are made from the editor workflow (assets + level changes); `.uproject` and `.mcp.json` edits are tooling setup for the MCP plugins.

### Workflow notes (learned the hard way)

- **Git LFS is required.** `.uasset`, `.umap`, `.fbx`, `.png`, `.wav` and `.mp3` go through LFS (`.gitattributes`). `ISIK.uproject` is deliberately plain text, not LFS, so a clone without LFS can still be opened.
- **Do not switch branches or check out files while the editor is open.** It holds assets in memory and the on-disk files change underneath it. Do git work that needs another branch in a `git worktree` at a **short path** (e.g. `C:\wt`): paths under `Content/Fab/Megascans/...` exceed Windows' length limit in deep directories. Use `GIT_LFS_SKIP_SMUDGE=1` when creating one.
- **Binary assets cannot be merged.** Keep one change set per branch, commit a map/Blueprint edit as a single commit, and let the user merge PRs. For stacked PRs use merge commits (not squash) and retarget the child to `main` after the parent merges.
- **Unreal MCP object paths** are `/Game/Folder/Name.Name` (package + object); `/Game/Folder/Name` alone is rejected for `blueprint` parameters. For asset tools (`find_assets`, `get_referencers`, `delete`) the short form works.
- **MCP limits:** `read_graph_dsl` fails on `BP_Telekinezi:EventGraph` ("Cycle detected ... TACEANDBREAK"), so its graph cannot be read or rewritten that way; `compile_blueprint` on `BP_Enemy` raises `REINST_BP_Enemy_C_0` errors with the editor open and does not confirm success. Verify compiles in the editor.
- **`mcp__unreal-mcp__call_tool` performs deletes and edits** and is intentionally not allow-listed; expect a permission prompt. Only the discovery tools (`list_toolsets`, `describe_toolset`) and read-only git/gh commands are pre-allowed in `.claude/settings.json` (which is git-ignored).
- **Always check referencers before deleting an asset** (`AssetTools.get_referencers`). Deleting an asset the editor still references silently nulls the reference: removing `Developers/USER/Level/AM_Attack` left `BP_Enemy.LoopAttacking` with an empty montage until it was relinked to `/Game/Animations/AM_Attack`.

## Architecture (Content layout)

- **Game mode / input**: `GlobalDefaultGameMode` is `/Game/Telekinezi/Blueprints/GameMode/BP_TelekineziGameMode`. Input uses Enhanced Input (`Content/Input/IMC_Default`, `IMC_MouseLook`, actions in `Input/Actions`).
- **`Content/Telekinezi/`** — the main gameplay feature set (Blueprints incl. GameMode, Karakter [character], Animasyonlar, Niagara, Materials, Curves, Level). Start here for core mechanics.
- **Shared systems**: `Content/Components` (function libraries such as `BFL_StatsUtility`, component enums) with the active stat component `Content/Components/Blueprints/BP_Stats` (an `ActorComponent`, used by `BFL_StatsUtility` and `WB_FadeIn`) and the live health component `Content/Components/Blueprints/UC_HealthComponent` (an independent `ActorComponent` used by `BP_Telekinezi`, `BP_Enemy` and the tutorial level) paired with the `Content/Interfaces/BPI_Stats` Blueprint interface; `Content/Gameplay` (Souls, Spawning, Gambling, Audio); `Content/Enums`.
- **Class hierarchy** (verified through the editor's asset registry): the player is `BP_Telekinezi` (`Character`, used by the GameMode); throwables derive from `BP_Throwable` (`Actor`), with `BP_Sword` as the active sword; enemies derive from `BP_Enemy` (`Character`) in `Content/Telekinezi/Karakter`.
- **Removed (do not recreate or depend on):** `Components/Bp_StatComponent` and its copy under `Assets/Spider/...`, `Enemy/BP_EnemyAi`, `Developers/Niyazi/Ai/BP_Enemy_AI`, `BP_SwordOld`, `BP_Sword_Refactored`, `BP_ThrowableWeapon`, `BP_MainPawn`. They were unreferenced and deleted. `MyBlueprints/Components/BPC_HealthSyst` is also effectively dead (only its own interface references it).
- **Known cleanup candidates, not done yet:** `BP_Enemy` still carries player-copy members (`Move`, `Aim`, `bIsTPS`, `bIsTelekinesis`, `bIsGrabbing`, `WBP_Ref_Grab`, `WBP_Ref_Aim`, `TargetDistance`, `Damage`) that its own graphs never use — verify with *Find References* in the editor before removing, since `BP_Telekinezi`'s graph could not be read. `BP_Telekinezi` duplicates `CheckMaterial` / `CheckIfNewActor` blocks and has two near-identical rotation variables.
- **Levels** in `Content/Levels`: `L_Main3DMenu` (menu), `L_Tutorial_New` (tutorial), `Oba_L`.
- **Tutorial prompts** use placed instances of `Content/Telekinezi/Blueprints/BP_TutorialTrigger` (a box trigger with instance-editable `PromptText`, `Duration` — 0 means until the player leaves — and `bTriggerOnce`). On overlap with the player it creates `Content/Widgets/Widget/WBP_TutorialPrompt`, calls its `SetPromptText`, and shows it; the text wraps at 800px. Add a step by placing another instance and editing its text — do not add per-step events to the Level Blueprint, and do not place a trigger over `PlayerStart` (the player would spawn inside it and may miss the begin-overlap).
- **Sword-surfing / combat** (recent commits: "new states onswordsurfin"): assets under `FIRETRAILOFTHESWORD`, `SwordTrailVFX`, `CombatMagicAnims`, and character folders in `Content/Characters` (Kam, Karakter, Chinese, Mannequins).
- `Content/FirstPerson`, `Content/ThirdPerson`, `Content/Fab`, `Content/NeonGrid` are template/marketplace content; avoid modifying unless asked.
- Naming is mixed Turkish/English (e.g. `Karakter`, `Animasyonlar`, `Oba`).

## Plugins

`Plugins/Source/BlueprintArrange` is a local editor plugin (Blueprint node auto-arrange; only tests/headers present). Enabled engine plugins of note: ModelingToolsEditorMode, Water, DaySequence, FieldSystem, ModelContextProtocol, ToolsetRegistry, AllToolsets.

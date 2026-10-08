# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

"ISIK" (repo: KutunYukselisi) is an Unreal Engine 5.8 game (`EngineAssociation: 5.8` in `ISIK.uproject`). It is a **Blueprint-only project in practice**: `Source/ISIK` is empty, there is no C++ game module, and no build/lint/test commands exist. All gameplay logic lives in `.uasset`/`.umap` binaries under `Content/`, which cannot be meaningfully read or diffed as text — edit them through the Unreal Editor (or the Unreal MCP server, see below), not with file tools.

## Working with the project

- Open `ISIK.uproject` in the Unreal Editor (5.8). Editor startup map: `/Game/Levels/L_Tutorial_New`. Packaged-game default map: `/Game/Levels/L_Main3DMenu`.
- `.mcp.json` registers an `unreal-mcp` HTTP server at `http://127.0.0.1:8000/mcp`. It is served by the editor's `ModelContextProtocol` / `ToolsetRegistry` / `AllToolsets` plugins, so the **editor must be running** for it to connect (otherwise `ECONNREFUSED`). Use it to inspect/modify Blueprints and levels.
- `Binaries/`, `Intermediate/`, `DerivedDataCache/`, `Saved/` are generated; do not edit.
- Git history shows commits are made from the editor workflow (assets + level changes); `.uproject` and `.mcp.json` edits are tooling setup for the MCP plugins.

## Architecture (Content layout)

- **Game mode / input**: `GlobalDefaultGameMode` is `/Game/Telekinezi/Blueprints/GameMode/BP_TelekineziGameMode`. Input uses Enhanced Input (`Content/Input/IMC_Default`, `IMC_MouseLook`, actions in `Input/Actions`).
- **`Content/Telekinezi/`** — the main gameplay feature set (Blueprints incl. GameMode, Karakter [character], Animasyonlar, Niagara, Materials, Curves, Level). Start here for core mechanics.
- **Shared systems**: `Content/Components` (function libraries such as `BFL_StatsUtility`, component enums) with the active stat component `Content/Components/Blueprints/BP_Stats` (an `ActorComponent`) paired with the `Content/Interfaces/BPI_Stats` Blueprint interface; `Content/Gameplay` (Souls, Spawning, Gambling, Audio); `Content/Enums`.
- **Class hierarchy** (verified through the editor's asset registry): the player is `BP_Telekinezi` (`Character`, used by the GameMode); throwables derive from `BP_Throwable` (`Actor`), with `BP_Sword` as the active sword; enemies derive from `BP_Enemy` (`Character`) in `Content/Telekinezi/Karakter`.
- **Unused / legacy — do not build on these** (nothing references them): `Components/Bp_StatComponent` and its copy under `Assets/Spider/...`, `Enemy/BP_EnemyAi`, `Developers/Niyazi/Ai/BP_Enemy_AI`, `BP_SwordOld`, `BP_Sword_Refactored`, `BP_MainPawn`. Check the Reference Viewer before relying on or deleting any of them.
- **Levels** in `Content/Levels`: `L_Main3DMenu` (menu), `L_Tutorial_New` (tutorial, recent work with collision-interaction fixes and a tutorial widget `wbp_tutorial`), `Oba_L`.
- **Sword-surfing / combat** (recent commits: "new states onswordsurfin"): assets under `FIRETRAILOFTHESWORD`, `SwordTrailVFX`, `CombatMagicAnims`, and character folders in `Content/Characters` (Kam, Karakter, Chinese, Mannequins).
- `Content/FirstPerson`, `Content/ThirdPerson`, `Content/Fab`, `Content/NeonGrid` are template/marketplace content; avoid modifying unless asked.
- Naming is mixed Turkish/English (e.g. `Karakter`, `Animasyonlar`, `Oba`).

## Plugins

`Plugins/Source/BlueprintArrange` is a local editor plugin (Blueprint node auto-arrange; only tests/headers present). Enabled engine plugins of note: ModelingToolsEditorMode, Water, DaySequence, FieldSystem, ModelContextProtocol, ToolsetRegistry, AllToolsets.

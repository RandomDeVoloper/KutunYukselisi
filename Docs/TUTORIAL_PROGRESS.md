# Tutorial panel — 17 November 2026

## Current update: ordered lessons and progressive control hints

This update supersedes earlier statements that a later lesson can replace an unfinished one or that all control hints are always visible.

- `TutorialOrder` assigns the nine arena instances this explicit sequence: jump (1), grab/release (2), scale (0), pin (3), bridge piece (5), mount (4), sword (6), throw/crush practice (7), final mount (8). Parentheses identify actor instance suffixes, not lesson numbers.
- The single `WBP_TutorialControls` instance holds `NextLessonOrder`. `StartTutorial` checks `CanStartLesson` before changing lesson state or removing any existing prompt. Completion advances the sequence exactly once.
- Entering a later trigger early does not start it, interrupt the current lesson, or reveal hints. If the player remains inside the next trigger when its prerequisite finishes, it starts automatically; otherwise the player must return to that trigger. This gates tutorial activation, not physical player movement.
- The right panel starts Collapsed with empty text. Lines appear only when taught: hold on grab step 1; release on grab step 2; wheel on scale step 2; TAB on pin step 2; G on mount; right mouse on sword; left click on throw step 2. Previously taught controls remain available during the level.
- Panel/heading colors use the supplied Gece Mavisi and Kut Altını hex values converted from sRGB to Unreal linear values. Palette: `Docs/UI_PALETTE.md`.

### Validation of ordering and hint visibility

- PIE: entering flight order 5 while expected order was 0 left active/triggered flags false. All learned flags were false; right panel was Collapsed and empty.
- PIE: entering order 1 while the first lesson remained active did not interrupt the first or start the second.
- PIE sequence fixture: temporarily made the first lesson informational with a short duration in the PIE copy and bypassed cinematic waiting in the test graph. Completion advanced order 0 to 1 and the waiting second trigger started without re-entry. Only hold-to-grab was learned/displayed; release, scale, TAB, G and sword remained hidden. Order 2 was still blocked.
- Discarded the fixture and restored the production cinematic guard. Confirmed editor first lesson remains kind 1 (jump), duration 25, order 0. Blueprint/UMG compilation and runtime error-log checks passed.
- Verified real newline output after correcting escaped line separators in the generated guide.
- Graph sources: `Tools/TutorialFlow/Guide_*.dsl` and updated trigger files. Recovery binaries: `Backups/TutorialSequence_20261117/`.

## Current implementation: action completion and retry

This section supersedes the historical snapshot below.

- All nine Stand_Arena lessons now have 25–35 seconds **per step**. Unfinished action lessons restart from their first step when time expires; player position and the level are not reset.
- Two-step lessons reset their step timer on advancement. Completed lessons show confirmation for 2.5 seconds, then close. Their trigger does not repeat when configured as trigger-once.
- Only the visible lesson updates; a newer lesson replaces the previous one. Re-entering an unfinished lesson can start it again. Timers pause during player cinematics and naturally pause with the game.
- Completion checks use actual player/component state: upward airborne motion; grabbing then releasing; a cached component scale changing by >0.05; a formerly simulated held component becoming non-simulated; possession of a mounted BP_SwordMount; two sword-in-hand state changes; or a cached component being thrown at >300 units/s (or destroyed during the throwing/crushing practice).
- Bridge practice confirms **one fixed bridge piece**, not an entire completed bridge. Jump practice confirms a jump, not reaching the far side of the obstacle. Throwing practice does not claim a confirmed enemy kill.
- New `WBP_TutorialControls` provides one persistent, non-interactive right-side control guide: hold/click left mouse, wheel scaling, TAB pinning, right mouse sword control, G sword mount. Multiple tutorial triggers do not create multiple guides.
- The progress bar now shows remaining **step time**. Retry displays a short instruction explaining that the lesson restarted.
- Editable lesson content: TutorialKind, Duration, TutorialTitle, PromptText, SecondPrompt, HintText, SecondHint, SuccessText. Internal state stays non-instance-editable.

### Validation of the current implementation

- Both widgets compiled successfully. Trigger compilation and runtime logs contained no Blueprint errors, Accessed None, or infinite-loop messages.
- PIE observed an untouched lesson repeat after its timeout.
- PIE injected a second-step timeout: state returned to step 0, retry count increased to 1, elapsed time reset to 0, and the lesson remained active and unfinished.
- PIE seeded the scale lesson's second step and observed completion followed by automatic dismissal after 2.5 seconds. A full unchanged-versus-changed scale test through the grabbing pipeline remains a manual playtest item; the seeded baseline came from an actor transform rather than the exact component getter used by the lesson.
- PIE isolated the pin predicate on a test cube: simulated physics stayed unfinished; disabling physics completed the lesson.
- Visually inspected the main prompt above the health bar and the right control panel in the native Unreal window. Shortened guide wording after observing unwanted wrapping.
- Keyboard/mouse end-to-end execution of every action, all screen resolutions, and sword mounting remain manual playtest items. Predicate tests above injected cached lesson state in PIE; they do not claim to exercise the player's full grabbing/input pipeline.
- PIE-only cube/state changes were discarded. Temporary editability for predicate tests was reverted before final compilation and saving.

Graph sources for review are in `Tools/TutorialFlow/*.dsl`; lesson settings are in `Tools/TutorialFlow/lessons.json`. These files document the editor assets and are not loaded at runtime. Before bulk edits, recovery copies were saved in `Backups/TutorialFlow_20261117/`.

## Historical snapshot: timed reading panel

The following describes the earlier implementation, before action completion and retry were added.

## Completed

- Current level: `/Game/Kutun/Maps/Stand_Arena`; nine existing `BP_TutorialTrigger` instances.
- Rewrote all nine Turkish instructions; populated `TutorialTitle` and `HintText`.
- Reading duration is 8–12 seconds per instruction instead of 1.5–3 seconds.
- `RefreshTutorial` fills the title, instruction and hint through `WBP_TutorialPrompt.SetTutorialState` and shows the remaining reading time as a progress bar.
- `CompleteTutorial` stops updates and removes the prompt. Tick advances reading time only while the prompt is active. A new prompt replaces the previous prompt.
- Duration <= 0 still keeps the prompt visible until the player leaves its trigger; its progress stays full.
- Panel anchors above the health bar with automatic height and 460-unit text wrapping.
- TutorialTitle and HintText are instance-editable for future level authoring.

## Verification

- Widget Blueprint compilation returned true; trigger Blueprint compilation reported no compiler errors in the editor log.
- PIE: entering trigger 0 created the expected heading, instruction and hint; after 10 seconds its progress reached zero and the trigger became inactive/finished.
- PIE: entering trigger 2 created a new widget with its own text and a decreasing progress value.
- Graph connectivity inspection found no disconnected nodes in EventGraph, RefreshTutorial or CompleteTutorial.
- Visual HUD inspection at different screen resolutions remains unverified: editor image capture was unavailable and viewport capture showed the scene without the gameplay HUD.

## Scope / remaining work

The progress bar measures reading time, not successful gameplay actions. Existing scaffolding (`TutorialKind`, `TutorialStep`, `SecondPrompt`, `SecondHint`, `SuccessText`, observed player/component references) remains unused. Connecting completion to jumping, grabbing, scaling, pinning, sword recall and flight is a separate gameplay integration task. The panel no longer claims that performing a move unlocks a next step.

Before edits, saved the three affected packages and copied their binaries to `Backups/TutorialText_20261117/`. Backups may contain other pre-existing user changes; do not restore them without checking subsequent work.

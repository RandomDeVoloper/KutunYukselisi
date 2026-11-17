# Toygard UI palette

User-supplied palette; hex values are the source of truth. Convert sRGB to linear RGB when assigning Unreal LinearColor properties. Alpha is independent.

| Name | sRGB hex | Usage |
| --- | --- | --- |
| Kut Altını | #D2B37A | Player energy, active UI, hover waiting |
| Kut Parlağı | #FFEBB3 | Victory bursts and special effects |
| Bozkır Kızılı | #710B04 | Danger, active hover, enemies |
| Gece Mavisi | #0E152E | Panel backgrounds |

Applied to tutorial: Kut Altını headings/progress fill, low-opacity gold progress track, Gece Mavisi backgrounds (main alpha 0.9, right guide alpha 0.75). Other roles remain design guidance; combat/VFX assets were not recolored.

## Main HUD implementation — 17 November 2026

- `WBP_StandHUD`: centered timer panel with small gold KALAN SÜRE label and larger time value; right-aligned arena/kill panel. Both use Gece Mavisi backgrounds and a thin Kut Altını upper accent.
- `WBP_HealthBar`: bottom-left YAŞAM panel, right-aligned health value and thinner gold health bar.
- Existing timer, score and health update graphs remain intact, including the timer's existing last-ten-seconds warning color.
- Moved the tutorial prompt upward to keep it clear of the new health panel.
- All three widget compilations returned true. Verified the redesigned panels and live time/health/score values in a native PIE screenshot; no Blueprint runtime errors were logged. PIE stopped after inspection.
- Recovery copies: `Backups/MainHUD_20261117/`. Style properties: `Tools/HUDStyle.json`.

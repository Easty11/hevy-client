# HEVY EXERCISE TEMPLATE ID REGISTRY

*Verified template IDs for Luke's Hevy account. Resolved via `search-exercise-templates` / `get-exercise-template`.*
*Rule (per PROJECT_KNOWLEDGE §2d): `exercise_template_id` must come from real data — never fabricate. This file IS the verified source.*
*Last updated: 17 June 2026*

---

## How IDs behave

- **Standard (built-in) IDs** are short 8-char hex (e.g. `43573BB8`). Stable across the Hevy catalogue — same for everyone.
- **Custom IDs** are full UUIDs (e.g. `778c9159-7a8f-4a6a-bf64-79f0d399fcb2`). **Account-specific and not name-searchable reliably** — if a custom exercise is ever deleted/recreated the ID changes. These are the ones worth pinning here.

---

## Custom exercises (account-specific — pin these)

| Exercise | Template ID | Type | Notes |
|---|---|---|---|
| Shoulder Internal Rotation | `b4bab549-a143-4186-9615-249165e5a4a2` | weight_reps | Currently used as the "Cable Internal Rotation" rehab slot |
| Shoulder External Rotation | `f5f7ecfb-68b8-44d6-99c4-f2dc7b183072` | weight_reps | Currently used as the "Cable External Rotation" rehab slot |
| Weighted Dead Bug | `778c9159-7a8f-4a6a-bf64-79f0d399fcb2` | weight_reps | Logged at 20kg plate |
| Anti‑Rotation Pallof Press | `12b590de-078b-411d-ac22-dce2cf745ad0` | weight_reps | |
| Copenhagen Plank (Short Lever) | `a4f88801-6440-40b3-b862-728a3d2b1636` | duration | |
| Standing Cable Chest Press | `9407789b-cc0e-436d-8a00-c2c45695705f` | weight_reps | |

---

## Standard exercises (built-in catalogue)

| Exercise | Template ID | Type |
|---|---|---|
| Air Bike | `43573BB8` | duration (cardio) |
| Lat Pulldown (Machine) | `473CF5B8` | weight_reps |
| Lat Pulldown (Cable) | `6A6C31A5` | weight_reps |
| Seated Row (Machine) | `1DF4A847` | weight_reps |
| Single Arm Lat Pulldown | `2EE45F81` | weight_reps |
| Rear Delt Reverse Fly (Cable) | `C315DC2A` | weight_reps |
| Rear Delt Reverse Fly (Dumbbell) | `E5988A0A` | weight_reps |
| Rear Delt Reverse Fly (Machine) | `D8281C62` | weight_reps |
| Chest Press (Machine) | `7EB3F7C3` | weight_reps |
| Lateral Raise (Dumbbell) | `422B08F1` | weight_reps |
| Lateral Raise (Cable) | `BE289E45` | weight_reps |
| Band Pullaparts | `E8D86EE8` | reps_only |
| Cable Crunch | `23A48484` | weight_reps |
| Plank | `C6C9B8A0` | duration |
| Dead Bug | `D8911FC4` | reps_only |
| Seated Shoulder Press (Machine) | `9237BAD1` | weight_reps |
| Landmine Row | `D7D7FCCE` | weight_reps |

---

## Gaps — candidates for custom creation

*Names searched this session that returned no exact match. Review during the planned library audit before creating customs.*

| Wanted name | Current workaround | Action |
|---|---|---|
| Cable Internal Rotation | custom *Shoulder Internal Rotation* | Decide: rename/keep, or create a proper cable-specific custom |
| Cable External Rotation | custom *Shoulder External Rotation* | Same |
| Face Pull | none — not yet searched/confirmed | Check catalogue first; physio rehab candidate |

*Note: a search for `"chest press machine"` / `"seated row machine"` / `"lat pulldown machine"` etc. returns **nothing** — Hevy stores the equipment qualifier in parentheses, e.g. `Chest Press (Machine)`. Search the base name, not "name + machine".*

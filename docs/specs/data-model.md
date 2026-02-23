# Data Model — Match History

> Each completed race saves a record. All records live in `match_history.json`.

---

## Record Schema

```json
{
  "id": 1,
  "date": "2026-03-07 14:30",
  "player_name": "Player1",
  "winner": "Human",
  "human_time": 12.53,
  "bot_time": 10.21,
  "wall_count": 87,
  "grid_w": 30,
  "grid_h": 20
}
```

### Field Details

| Field | Type | Description | Example |
|---|---|---|---|
| `id` | `int` | Auto-incremented unique ID | `1`, `2`, `3`… |
| `date` | `str` | Timestamp of match | `"2026-03-07 14:30"` |
| `player_name` | `str` | Default `"Player1"`, renameable | `"SpeedKing"` |
| `winner` | `str` | One of: `"Human"`, `"Bot"`, `"Tie"` | `"Human"` |
| `human_time` | `float` | Seconds, 2 decimal places | `12.53` |
| `bot_time` | `float` | Seconds (or `999.99` if no path) | `10.21` |
| `wall_count` | `int` | Number of wall cells in the grid | `87` |
| `grid_w` | `int` | Grid width (columns) | `30` |
| `grid_h` | `int` | Grid height (rows) | `20` |

---

## File Format

The file is a **JSON array** of record objects:

```json
[
  { "id": 1, "date": "...", ... },
  { "id": 2, "date": "...", ... }
]
```

---

## CRUD Operations

| Operation | Function | What It Does |
|---|---|---|
| **C**reate | `add_record(...)` | Append new dict, save file |
| **R**ead | `load_history()` | Load JSON into list of dicts |
| **U**pdate | `rename_record(id, name)` | Find by id, change `player_name`, save |
| **D**elete | `delete_record(id)` | Remove dict by id, save |
| **S**earch | `filter_records()` / `sort_records()` | Filter by winner, sort by time/date |

---

## Edge Cases to Handle

| Situation | Behavior |
|---|---|
| File doesn't exist | `load_history()` returns `[]` |
| File is empty | `load_history()` returns `[]` |
| File has bad JSON | `load_history()` returns `[]` (catch `JSONDecodeError`) |
| No records yet | History screen shows "No matches recorded yet." |
| Bot had no path | Save `bot_time` as `999.99`, winner = `"Human"` |

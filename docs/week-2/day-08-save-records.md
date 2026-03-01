# Day 8 — Save Match Record (Create)

> **Goal:** After each race, automatically save a record to `match_history.json`.  
> **Files to create:** `history.py`  
> **Time:** ~2 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | JSON read/write | `"python json load dump file tutorial"` |
| 2 | datetime formatting | `"python datetime.now strftime"` |
| 3 | File safety | `"python FileNotFoundError try except"` |

### Quick reference:

```
import json

# Read JSON file → Python list
with open("file.json", "r") as f:
    data = json.load(f)

# Write Python list → JSON file
with open("file.json", "w") as f:
    json.dump(data, f, indent=2)

# Get current date/time as string
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M")  # "2026-03-07 14:30"
```

---

## Task 8.1 — Create `history.py` with load/save

### `load_history() → list[dict]`

```
1. Try: open "match_history.json", json.load() it, return the list
2. Except FileNotFoundError: return []
3. Except json.JSONDecodeError: return []  (corrupt/empty file)
```

### `save_history(records: list[dict])`

```
1. Open "match_history.json" in write mode ("w")
2. json.dump(records, f, indent=2)
```

### `get_next_id(records) → int`

```
1. If records is empty → return 1
2. Else → return max(r["id"] for r in records) + 1
```

**✅ Acceptance:** Call `load_history()` when no file exists → returns `[]`. Save a test list → `match_history.json` appears with formatted JSON.

---

## Task 8.2 — Write `add_record()`

### `add_record(winner, human_time, bot_time, wall_count, grid_w, grid_h)`

```
1. records = load_history()
2. new_record = {
       "id": get_next_id(records),
       "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
       "player_name": "Player1",
       "winner": winner,
       "human_time": round(human_time, 2),
       "bot_time": round(bot_time, 2),
       "wall_count": wall_count,
       "grid_w": grid_w,
       "grid_h": grid_h
   }
3. records.append(new_record)
4. save_history(records)
```

---

## Task 8.3 — Wire into result screen

In `result.py`, when the result screen is **first entered** (not every frame):

1. Add a flag: `record_saved = False`
2. When transitioning to RESULT state:
   - If `not record_saved`:
     - Call `add_record(winner, human_time, bot_time, wall_count, GRID_COLS, GRID_ROWS)`
     - Set `record_saved = True`
3. When leaving RESULT state → reset `record_saved = False`

> **Why the flag?** Without it, `add_record()` gets called 60 times per second!

**✅ Acceptance:** Play a race → go to result → check `match_history.json` → your record is there with correct data. Close and reopen the game → records persist.

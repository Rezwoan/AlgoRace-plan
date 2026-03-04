# Day 12 — Sort & Filter (Search)

> **Goal:** Add buttons to sort records by time/date and filter by winner.  
> **Files:** Update `history.py`, update `history_screen.py`  
> **Time:** ~2 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Sorting list of dicts | `"python sorted list of dicts by key lambda"` |
| 2 | List filtering | `"python list comprehension filter condition"` |

### Key patterns:

```python
# Sort by human_time, fastest first
sorted(records, key=lambda r: r["human_time"])

# Sort by date, newest first
sorted(records, key=lambda r: r["date"], reverse=True)

# Filter: only human wins
[r for r in records if r["winner"] == "Human"]
```

---

## Task 12.1 — Add sort/filter functions to `history.py`

### `sort_records(records, key, reverse=False) → list`

- `key` is a string: `"human_time"`, `"bot_time"`, or `"date"`
- Return `sorted(records, key=lambda r: r[key], reverse=reverse)`

### `filter_records(records, winner=None) → list`

- If `winner is None` → return `list(records)` (copy of all)
- Else → return `[r for r in records if r["winner"] == winner]`

---

## Task 12.2 — Add sort/filter buttons to history screen

### Button row layout (below the action buttons, at `y = 570`):

```
┌──────────────────────────────────────────────────────────────┐
│  Sort:  [Time ▲]  [Time ▼]  [Date]                          │
│  Filter: [Human Wins]  [Bot Wins]  [All]                     │
└──────────────────────────────────────────────────────────────┘
```

### Button specs:

| Button | x | y | Width | Height | Action |
|---|---|---|---|---|---|
| "Time ▲" | `120` | `520` | `110` | `35` | Sort by `human_time`, ascending |
| "Time ▼" | `240` | `520` | `110` | `35` | Sort by `human_time`, descending |
| "Date" | `360` | `520` | `110` | `35` | Sort by `date`, descending |
| "Human Wins" | `120` | `560` | `130` | `35` | Filter `winner == "Human"` |
| "Bot Wins" | `260` | `560` | `130` | `35` | Filter `winner == "Bot"` |
| "All" | `400` | `560` | `80` | `35` | Clear filter (show all) |

Draw labels "Sort:" at `(30, 528)` and "Filter:" at `(30, 568)`.

### On button click:

```
# Sort button example:
display_records = sort_records(display_records, "human_time", reverse=False)
selected_index = None

# Filter button example:
display_records = filter_records(records, "Human")  # filter from ALL records
selected_index = None

# "All" button:
display_records = records.copy()
selected_index = None
```

> **Important:** Filters work on the full `records` list, not on `display_records`. Otherwise filtering twice would lose data.

**✅ Acceptance:**
1. Have 3+ records with different winners and times
2. Click "Human Wins" → only human-win records shown
3. Click "Bot Wins" → only bot-win records shown
4. Click "All" → everything back
5. Click "Time ▲" → sorted fastest time first
6. Click "Time ▼" → sorted slowest first
7. Click "Date" → most recent first

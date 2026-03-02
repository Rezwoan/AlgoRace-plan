# Day 9 — History Screen (Read)

> **Goal:** Display all saved match records in a table format with row selection.  
> **Files to create:** `history_screen.py`  
> **Time:** ~3 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Drawing text rows | You already know this from Day 1 |
| 2 | Click → row index | See formula below |

---

## Task 9.1 — Create `history_screen.py`

### Screen layout:

```
┌──────────────────────────────────────────────────────────────────┐
│  MATCH HISTORY                                   [BACK TO MENU] │
│ ──────────────────────────────────────────────────────────────── │
│  #   │ Date             │ Player   │ Winner │ Human   │ Bot     │
│ ──────────────────────────────────────────────────────────────── │
│  1   │ 2026-03-07 14:30 │ Player1  │ Human  │ 12.53s  │ 10.21s │
│  2   │ 2026-03-07 14:35 │ Player1  │ Bot    │ 15.20s  │  9.88s │
│  3   │ 2026-03-07 15:00 │ Speed    │ Human  │  8.44s  │ 10.21s │
│  ▸   │ (selected = highlighted row)                              │
│      │                                                           │
│ ──────────────────────────────────────────────────────────────── │
│                                                                  │
│  [DELETE]  [RENAME]                                              │
│                                                                  │
│  (Analytics & sort/filter buttons come in Days 12–13)            │
└──────────────────────────────────────────────────────────────────┘
```

### State variables:

```
selected_index = None        # which row is selected (0-based)
records = []                 # all records from JSON
display_records = []         # filtered/sorted view (starts as all)
```

### Column layout:

| Column | x position | Content |
|---|---|---|
| `#` (id) | `30` | `str(r["id"])` |
| Date | `80` | `r["date"]` |
| Player | `300` | `r["player_name"]` |
| Winner | `450` | `r["winner"]` |
| Human Time | `580` | `f'{r["human_time"]:.2f}s'` |
| Bot Time | `720` | `f'{r["bot_time"]:.2f}s'` |
| Walls | `860` | `str(r["wall_count"])` |

### Row positioning:

| Element | y |
|---|---|
| Title "MATCH HISTORY" | `20` |
| Column headers | `70` |
| Header divider line | `95` |
| First record row | `100` |
| Row spacing | `30` px per row |
| Max visible rows | `12` (fits `100` → `460` px) |

### Draw function:

For each `i, record` in `enumerate(display_records[:12])`:
1. `y = 100 + i * 30`
2. If `i == selected_index` → draw a highlight rect behind the row at `(20, y, WINDOW_WIDTH - 40, 28)` with `HIGHLIGHT` color
3. Draw each column value using `draw_text()` at the corresponding x position

### Other elements:

| Element | Position | Size |
|---|---|---|
| "BACK TO MENU" button | `(980, 15)` | `200×40` |
| "DELETE" button | `(30, 520)` | `120×40` |
| "RENAME" button | `(170, 520)` | `120×40` |

### On entering HISTORY state:

```
records = load_history()
display_records = records.copy()
selected_index = None
```

---

## Task 9.2 — Row selection (click detection)

On `MOUSEBUTTONDOWN`, left button:

```
1. mx, my = event.pos
2. If 100 <= my <= 100 + len(display_records) * 30:
       index = (my - 100) // 30
       if 0 <= index < len(display_records):
           selected_index = index
   else:
       selected_index = None  (clicked outside table)
```

**✅ Acceptance:** Click a row → it highlights with `HIGHLIGHT` color. Click another → selection moves. Click outside → deselects.

---

## Task 9.3 — "No matches" state

If `records` is empty, instead of the table, draw:

```
"No matches recorded yet. Play a race first!"
```

Centered at `(WINDOW_WIDTH // 2, 300)`, color `WHITE`, size `22`.

**✅ Acceptance:** History screen shows all records, rows are clickable, "Back to Menu" works. Empty state shows a friendly message.

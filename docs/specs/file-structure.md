# File & Folder Structure

> This is the final file layout you're building toward.  
> You won't create all files on Day 1 — each day adds new files.

---

## Project Tree

```
SNAP/
├── main.py                # Entry point: event loop + state machine
├── constants.py           # ALL colors, sizes, config (from specs/constants.md)
├── ui_helpers.py          # draw_button(), draw_text(), draw_input_box()
├── grid.py                # Grid creation, reset, pixel↔cell conversion
├── editor.py              # Editor screen: wall/start/end placement
├── player.py              # Player position, movement, collision
├── pathfinding.py         # BFS and A* implementations
├── bot.py                 # Bot: follows computed path step-by-step
├── race.py                # Race screen: start race, timer, win detection
├── result.py              # Result screen: winner + stats + buttons
├── history.py             # CRUD functions: load, save, add, delete, rename
├── history_screen.py      # History display: table, selection, sort/filter
├── analytics.py           # Win %, top 3 times computation
├── match_history.json     # Auto-created data file (DO NOT create manually)
│
└── docs/                  # This plan folder (not part of the game)
    └── ...
```

---

## When Each File Gets Created

| Day | Files Created |
|---|---|
| Day 1 | `constants.py`, `main.py`, `ui_helpers.py` |
| Day 2 | `grid.py`, start `editor.py` |
| Day 3 | Finish `editor.py` |
| Day 4 | `player.py` |
| Day 5 | `pathfinding.py` |
| Day 6 | `bot.py` |
| Day 7 | `race.py`, `result.py` |
| Day 8 | `history.py` |
| Day 9 | `history_screen.py` |
| Day 11 | Update `history_screen.py` (rename logic) |
| Day 13 | `analytics.py` |

---

## Design Principle: No Classes Needed

Each file uses **plain functions** + module-level variables or dicts.  
Example: instead of a `Player` class, just use:

```
player = {"row": 0, "col": 0, "active": False}
```

This is simpler, professor-friendly, and totally fine for this project size.

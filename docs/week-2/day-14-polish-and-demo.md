# Day 14 — Polish, Edge Cases & Demo Prep

> **Goal:** Handle all edge cases, add help overlay, rehearse demo.  
> **Files:** Various small updates  
> **Time:** ~3–4 hours

---

## Task 14.1 — Edge Case Checklist

Go through each one and fix it:

| # | Edge Case | Where | Fix |
|---|---|---|---|
| 1 | No Start or End placed | `race.py` → `start_race()` | Show error: `"Place Start and End first!"` for 2 sec |
| 2 | No valid path exists | `race.py` → `start_race()` | Show error: `"No path found! Adjust walls."` |
| 3 | Bot has no path but player finishes | `race.py` | Set `bot_time = 999.99`, `winner = "Human"` |
| 4 | `match_history.json` empty/corrupt | `history.py` | Already handled — `load_history()` returns `[]` |
| 5 | Player name empty after rename | `history_screen.py` | Don't allow — keep old name if `rename_text` is empty |
| 6 | 0 records in history | `history_screen.py` | Show `"No matches recorded yet."` instead of table |
| 7 | Start placed on a wall | `editor.py` | Placing Start/End always overrides cell value |
| 8 | Player at end but race not started | `editor.py` | Only check win condition when `race["running"]` is True |

---

## Task 14.2 — Controls Help Overlay

Press `H` to toggle a help screen:

```
┌─────────────────────────────────────┐
│                                     │
│            CONTROLS                 │
│                                     │
│   Editor:                           │
│     Left Click        Toggle wall   │
│     S + Click         Place Start   │
│     E + Click         Place End     │
│     C                 Clear grid    │
│     H                 This help     │
│     ENTER             Start race    │
│                                     │
│   Race:                             │
│     Arrow Keys        Move player   │
│                                     │
│   History:                          │
│     Click row         Select        │
│     Delete btn        Remove record │
│     Rename btn        Edit name     │
│                                     │
│          Press H to close           │
│                                     │
└─────────────────────────────────────┘
```

### Implementation:

1. Add variable: `show_help = False`
2. On `KEYDOWN` → `K_h`: toggle `show_help = not show_help`
3. When `show_help` is True:
   - Draw a semi-transparent dark overlay over the whole screen:
     - Create a surface: `overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))`
     - Set alpha: `overlay.set_alpha(200)`
     - Fill: `overlay.fill((10, 10, 20))`
     - Blit: `screen.blit(overlay, (0, 0))`
   - Draw the help text on top (centered, white text, 18px)
   - Draw a box border behind it for clarity

---

## Task 14.3 — Optional: Visual Path Expansion Animation

If you have time, show BFS/A* expanding in real-time:

1. Instead of instant pathfinding, yield cells one at a time
2. Draw "explored" cells in a dim color (e.g., `(40, 40, 70)`)
3. Show the path being found before the race starts

> This is purely visual polish. Skip if short on time.

---

## Task 14.4 — Demo Rehearsal Script

Practice this exact flow for your professor:

```
Step  Action                              What to Say
────  ─────────────────────────────────   ──────────────────────────
 1    Launch game                         "This is S.N.A.P."
 2    Point out menu buttons              "Three options: Start, History, Exit"
 3    Click START                         "This opens the maze editor"
 4    Click cells to place walls          "Left click toggles walls"
 5    Hold S + click                      "S + click places the start"
 6    Hold E + click                      "E + click places the end"
 7    Point to sidebar                    "Shows wall count and controls"
 8    Press ENTER                         "Race begins — timer starts"
 9    Race with arrow keys                "I navigate, bot follows A*"
10    Result screen appears               "Shows winner, times, stats"
11    Click MAIN MENU                     "Back to menu"
12    Click HISTORY                       "All matches are saved"
13    Point to records table              "CRUD — each record is saved"
14    Click a record → Rename             "Update: rename the player"
15    Type a name → Enter                 "Name persisted to JSON"
16    Click sort buttons                  "Search: sort by time"
17    Click filter buttons                "Filter by winner type"
18    Point to analytics                  "Win rate and top 3 times"
19    Select record → Delete              "Delete: remove a record"
20    Click BACK → EXIT                   "Records persist on restart"
```

> **Pro tip:** Have 3–4 records already saved before the demo so the history screen looks populated.

---

## Task 14.5 — Final Sanity Checks

Before your demo, verify:

- [ ] Game launches without errors
- [ ] All 5 screens work (Menu, Editor, Race, Result, History)
- [ ] No crashes on edge cases (empty grid, no path, etc.)
- [ ] JSON file persists across app restarts
- [ ] History loads correctly even with 0 records
- [ ] Rename, Delete, Sort, Filter all work
- [ ] Analytics numbers are correct
- [ ] `H` key shows controls overlay

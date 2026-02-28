# Day 7 — Race Logic, Timer & Result Screen

> **Goal:** Press Enter → timer starts → player races bot → winner shown on result screen.  
> **Files to create:** `race.py`, `result.py`  
> **Time:** ~3–4 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Precise timing | `"pygame.time.get_ticks timer example"` |
| 2 | State transition | You already know this — just set `state = "RESULT"` |

---

## Task 7.1 — Create `race.py` — race state management

### Race state (dict):

```
race = {
    "running": False,
    "start_time": 0,           # ms from get_ticks()
    "human_finish_time": None, # seconds (float) or None
    "bot_finish_time": None,   # seconds (float) or None
    "winner": None             # "Human", "Bot", or "Tie"
}
```

### `start_race(grid, player, bot, race) → str or None`

Call this when ENTER is pressed or RACE! button is clicked.

1. Find `start = find_cell(grid, START)` and `end = find_cell(grid, END)`
2. If either is `None` → return `"Place Start and End first!"`
3. Compute path: `path = find_path_astar(grid, start, end)` (or BFS)
4. If `path is None` → return `"No path found! Adjust walls."`
5. Reset player to start position: `player["row"], player["col"] = start`
6. Init bot: `bot = init_bot(path)`
7. Set `race["running"] = True`
8. Set `race["start_time"] = pygame.time.get_ticks()`
9. Set `race["human_finish_time"] = None`, `race["bot_finish_time"] = None`, `race["winner"] = None`
10. Return `None` (success)

### `update_race(player, bot, race, grid)`

Called every frame when race is running:

```
If not race["running"]: return

end = find_cell(grid, END)
current_time = pygame.time.get_ticks()
elapsed = (current_time - race["start_time"]) / 1000  # seconds

# Check human finish
if race["human_finish_time"] is None:
    if (player["row"], player["col"]) == end:
        race["human_finish_time"] = round(elapsed, 2)

# Check bot finish
if race["bot_finish_time"] is None:
    if bot["finished"]:
        race["bot_finish_time"] = round(
            (current_time - race["start_time"]) / 1000, 2
        )

# Both done? Determine winner
if race["human_finish_time"] is not None and race["bot_finish_time"] is not None:
    if race["human_finish_time"] < race["bot_finish_time"]:
        race["winner"] = "Human"
    elif race["bot_finish_time"] < race["human_finish_time"]:
        race["winner"] = "Bot"
    else:
        race["winner"] = "Tie"
    race["running"] = False
```

---

## Task 7.2 — Race HUD (timer display)

During the race, draw at the top of the screen:

```
┌──────────────────────────────────────────────────────────┐
│   ⏱ 05.32s                          You: --  Bot: --    │
│  ─────────────────────────────────────────────────────── │
│  (grid below)                                            │
```

| Element | Position | Font | Color |
|---|---|---|---|
| Timer `"⏱ XX.XXs"` | `(20, 30)` | `28` | `WHITE` |
| `"You: XX.XXs"` or `"You: --"` | `(700, 30)` | `20` | `PLAYER_COLOR` |
| `"Bot: XX.XXs"` or `"Bot: --"` | `(900, 30)` | `20` | `BOT_COLOR` |

- Show `"--"` until that racer finishes, then show their time
- Timer shows current elapsed time: `f"{elapsed:.2f}s"`

---

## Task 7.3 — Error messages

If `start_race()` returns an error string (instead of `None`):
- Show the message in `END_COLOR` (red) at the top of the editor screen
- Display it for ~2 seconds, then clear it
- **Simple approach:** store `error_msg` and `error_time`, draw if `current_time - error_time < 2000`

---

## Task 7.4 — Create `result.py` — Result screen

### Target layout:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│                     🏆  RACE RESULT                          │
│                                                              │
│                  Winner:  HUMAN!                             │
│                                                              │
│            ┌───────────────────────────────┐                 │
│            │   Your Time:     12.53 s      │                 │
│            │   Bot Time:      10.21 s      │                 │
│            │   Walls:         87           │                 │
│            │   Grid:          30 × 20      │                 │
│            └───────────────────────────────┘                 │
│                                                              │
│                   ┌────────────────┐                         │
│                   │   PLAY AGAIN   │                         │
│                   └────────────────┘                         │
│                   ┌────────────────┐                         │
│                   │   MAIN MENU    │                         │
│                   └────────────────┘                         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Positions:

| Element | x | y | Size | Color |
|---|---|---|---|---|
| "RACE RESULT" | centered (`600`) | `150` | `36` | `WHITE` |
| Winner name | centered | `220` | `48` | `GOLD` |
| Stats box background | `350, 300` | `500×160` | — | `(30, 30, 50)` |
| "Your Time: Xs" | `380` | `320` | `22` | `PLAYER_COLOR` |
| "Bot Time: Xs" | `380` | `350` | `22` | `BOT_COLOR` |
| "Walls: N" | `380` | `380` | `22` | `WHITE` |
| "Grid: W × H" | `380` | `410` | `22` | `WHITE` |
| "PLAY AGAIN" button | `470, 520` | `260×50` | — | — |
| "MAIN MENU" button | `470, 590` | `260×50` | — | — |

### Button actions:
- "PLAY AGAIN" → `state = "EDITOR"` (keep the same grid)
- "MAIN MENU" → `state = "MENU"`

**✅ Acceptance:** Full race loop works:
1. Build a maze with walls, start, end
2. Press Enter → timer starts, player can move, bot starts walking
3. Both reach end → result screen shows with correct winner and times
4. Play Again / Main Menu buttons work

# Constants & Configuration

> This is the **single source of truth** for every size, color, and config value in the project.  
> Create a file called `constants.py` and put all of these in it.

---

## Window & Layout

| Constant | Value | Purpose |
|---|---|---|
| `WINDOW_WIDTH` | `1200` | Total window width in pixels |
| `WINDOW_HEIGHT` | `800` | Total window height in pixels |
| `FPS` | `60` | Frames per second |
| `CELL_SIZE` | `30` | Each grid cell is 30×30 px |
| `GRID_COLS` | `30` | 30 columns → 900 px wide |
| `GRID_ROWS` | `20` | 20 rows → 600 px tall |
| `GRID_OFFSET_X` | `20` | Grid left padding |
| `GRID_OFFSET_Y` | `100` | Grid top padding (room for header) |
| `SIDEBAR_X` | `940` | Where sidebar info panel starts |

---

## Typography

| Constant | Value | Used For |
|---|---|---|
| `FONT_NAME` | `"consolas"` | Monospace, clean, available on Windows |
| `TITLE_FONT_SIZE` | `48` | Main menu title |
| `BUTTON_FONT_SIZE` | `28` | All clickable buttons |
| `LABEL_FONT_SIZE` | `20` | Info labels, sidebar text |
| `SMALL_FONT_SIZE` | `18` | History rows, analytics |

---

## Gameplay

| Constant | Value | Purpose |
|---|---|---|
| `BOT_MOVE_DELAY` | `80` | Milliseconds between bot steps |
| `HISTORY_FILE` | `"match_history.json"` | Where records are saved |

---

## Cell Types (stored in the grid)

| Constant | Value | Meaning |
|---|---|---|
| `EMPTY` | `0` | Walkable cell |
| `WALL` | `1` | Blocked cell |
| `START` | `2` | Player/Bot spawn point |
| `END` | `3` | Finish line |

---

## Color Palette

| Name | RGB Tuple | Used For |
|---|---|---|
| `BG_DARK` | `(18, 18, 30)` | Window background |
| `GRID_BG` | `(30, 30, 50)` | Empty cells |
| `GRID_LINE` | `(50, 50, 80)` | Grid line borders |
| `WALL_COLOR` | `(80, 80, 110)` | Wall cells |
| `START_COLOR` | `(0, 200, 120)` | Start cell (green) |
| `END_COLOR` | `(220, 50, 50)` | End cell (red) |
| `PLAYER_COLOR` | `(0, 180, 255)` | Human player (cyan) |
| `BOT_COLOR` | `(255, 165, 0)` | Bot (orange) |
| `PATH_COLOR` | `(255, 255, 100)` | Bot's planned path overlay |
| `BTN_NORMAL` | `(50, 50, 90)` | Button idle background |
| `BTN_HOVER` | `(80, 80, 140)` | Button hovered background |
| `BTN_TEXT` | `(230, 230, 255)` | Button label text |
| `WHITE` | `(255, 255, 255)` | General text |
| `GOLD` | `(255, 215, 0)` | Winner highlight, titles |
| `HIGHLIGHT` | `(60, 60, 120)` | Selected row in history |

---

## Menu Button Positions

| Button | x | y | Width | Height |
|---|---|---|---|---|
| "START" | `470` | `380` | `260` | `60` |
| "HISTORY" | `470` | `460` | `260` | `60` |
| "EXIT" | `470` | `540` | `260` | `60` |

> `x = (WINDOW_WIDTH - 260) // 2 = 470` to center horizontally.

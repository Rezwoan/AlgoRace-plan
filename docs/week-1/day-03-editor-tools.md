# Day 3 — Editor Tools (Walls, Start, End)

> **Goal:** Click to place/remove walls, hold S/E + click to place Start/End, press C to clear.  
> **Files:** Update `editor.py`, update `grid.py`  
> **Time:** ~2–3 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Held keys | `"pygame key.get_pressed vs KEYDOWN difference"` |
| 2 | Mouse held | `"pygame detect mouse button held down"` |

> **Key difference:**  
> - `KEYDOWN` event fires **once** when a key is pressed  
> - `pygame.key.get_pressed()` returns a snapshot of **all keys** — tells you if a key is currently held down  
> Use `get_pressed()` for modifier-type behavior (hold S then click).

---

## Task 3.1 — Toggle walls on click

In `editor.py`, write `editor_handle_events(grid, events)`:

On `MOUSEBUTTONDOWN` (left button, `event.button == 1`):

1. Get mouse position: `mx, my = event.pos`
2. Convert: `cell = pixel_to_cell(mx, my)`
3. If `cell is None` → ignore (clicked outside grid)
4. Get `row, col = cell`
5. Get held keys: `keys = pygame.key.get_pressed()`
6. If `keys[pygame.K_s]` is True → **place Start** (Task 3.2)
7. Elif `keys[pygame.K_e]` is True → **place End** (Task 3.2)
8. Else → **toggle wall:**
   - If `grid[row][col] == EMPTY` → set to `WALL`
   - If `grid[row][col] == WALL` → set to `EMPTY`
   - If `grid[row][col]` is `START` or `END` → do nothing (protect them)

**✅ Acceptance:** Click empty cells → they turn `WALL_COLOR`. Click again → back to empty.

---

## Task 3.2 — Place Start and End

Add a helper to `grid.py`:

### `find_cell(grid, value) → tuple or None`
- Scan every cell, return `(row, col)` of the first cell matching `value`
- Return `None` if not found

### Start placement logic (when S is held):
1. Find existing start: `old = find_cell(grid, START)`
2. If `old` exists → `grid[old[0]][old[1]] = EMPTY` (clear old start)
3. Set `grid[row][col] = START`

### End placement logic (when E is held):
- Same pattern but with `END` instead of `START`

> **Why clear the old one?** There should only be ONE start and ONE end on the grid at any time.

**✅ Acceptance:** Hold S + click → green cell appears. Click somewhere else while holding S → green moves (old one clears). Same for E + click → red cell.

---

## Task 3.3 — Clear grid

In the event loop, on `KEYDOWN`:
- If `event.key == pygame.K_c` → call `reset_grid(grid)`

**✅ Acceptance:** Build a maze, press C → everything is cleared.

---

## Task 3.4 — Sidebar info panel

On the right side of the screen, draw an info panel:

```
                                              ┌─────────────┐
                                              │  [RACE!]    │
                                              │             │
                                              │  Legend:    │
                                              │  ■ Wall     │
                                              │  ■ Start    │
                                              │  ■ End      │
                                              │             │
                                              │  Walls: 42  │
                                              │             │
                                              │  Controls:  │
                                              │  LClick=wall│
                                              │  S+Click=st │
                                              │  E+Click=end│
                                              │  C = clear  │
                                              │  Enter=race │
                                              └─────────────┘
```

### Positions:

| Element | Position |
|---|---|
| "RACE!" button | `(SIDEBAR_X, 50)`, size `200×45` |
| "Legend:" label | `(SIDEBAR_X, 120)` |
| Color squares (15×15) | `(SIDEBAR_X, 150/175/200)` with label text offset 25px right |
| "Walls: N" | `(SIDEBAR_X, 250)` — call `count_walls(grid)` each frame |
| "Controls:" | `(SIDEBAR_X, 310)` |
| Control lines | `(SIDEBAR_X, 340)` onwards, 25px apart |

For the legend squares, draw small filled rects of the appropriate color, then text to their right.

**✅ Acceptance:** Sidebar shows, wall count updates in real time as you click.

---

## Task 3.5 — Optional: Click-and-drag wall drawing

On `MOUSEMOTION` event, check if left mouse button is currently held:

```
if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
    cell = pixel_to_cell(*event.pos)
    if cell and grid[cell[0]][cell[1]] == EMPTY:
        grid[cell[0]][cell[1]] = WALL
```

> This is "stretch" — do it only if basic click-to-toggle works perfectly.

**✅ Acceptance:** Hold left mouse and drag across empty cells → walls paint continuously.

# Day 4 — Player Spawn & Movement with Collision

> **Goal:** Player appears at the Start cell and moves with arrow keys. Walls block movement.  
> **Files to create:** `player.py`, update `editor.py` / `main.py`  
> **Time:** ~2 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | KEYDOWN for arrows | `"pygame KEYDOWN arrow keys WASD example"` |
| 2 | Collision concept | No search needed — just check `grid[new_row][new_col] != WALL` |

---

## Task 4.1 — Create `player.py`

### Player state (just a dict, no class):

```
player = {
    "row": 0,
    "col": 0,
    "active": False
}
```

### `init_player(grid) → dict`
- Find the START cell: `start = find_cell(grid, START)`
- If `start is None` → return player at `(0, 0)` with `active = False`
- Return `{"row": start[0], "col": start[1], "active": True}`

### `move_player(player, direction, grid)`

`direction` is a string: `"up"`, `"down"`, `"left"`, `"right"`

1. Compute new position:
   - `"up"` → `new_row = player["row"] - 1`, same col
   - `"down"` → `new_row = player["row"] + 1`, same col
   - `"left"` → same row, `new_col = player["col"] - 1`
   - `"right"` → same row, `new_col = player["col"] + 1`
2. **Collision checks** (move is BLOCKED if any is true):
   - `new_row < 0` (above grid)
   - `new_row >= GRID_ROWS` (below grid)
   - `new_col < 0` (left of grid)
   - `new_col >= GRID_COLS` (right of grid)
   - `grid[new_row][new_col] == WALL`
3. If all checks pass → update `player["row"]` and `player["col"]`

### `draw_player(screen, player)`
1. Get pixel: `px, py = cell_to_pixel(player["row"], player["col"])`
2. Compute center: `cx = px + CELL_SIZE // 2`, `cy = py + CELL_SIZE // 2`
3. Draw circle: `pygame.draw.circle(screen, PLAYER_COLOR, (cx, cy), CELL_SIZE // 2 - 4)`

> Circle with radius slightly smaller than cell, so it doesn't overlap grid lines.

---

## Task 4.2 — Wire movement into editor screen

In the editor's event handling, on `KEYDOWN`:

| Key | Direction |
|---|---|
| `K_UP` or `K_w` | `"up"` |
| `K_DOWN` or `K_s` (only when **not** holding S for start placement!) | `"down"` |
| `K_LEFT` or `K_a` | `"left"` |
| `K_RIGHT` or `K_d` | `"right"` |

> ⚠️ **Conflict:** `S` key is used for placing Start AND for moving down (WASD). Solution: Only treat `S` as movement if the mouse button is **not** pressed. Or simpler: just use arrow keys for movement and keep WASD out to avoid confusion.

In `main.py`, when entering EDITOR state:
- Call `player = init_player(grid)`

In the draw phase:
- After `draw_grid()`, call `draw_player(screen, player)` (so player draws on top)

**✅ Acceptance:**
- Place a Start cell (S + click)
- Player circle appears on it (cyan)
- Arrow keys move the player one cell per press
- Player cannot walk through walls or off the grid
- Player can reach any open cell

# Day 2 — Grid Data Structure & Rendering

> **Goal:** Create a 2D grid in memory and draw it on screen with colors per cell type.  
> **Files to create:** `grid.py`, start `editor.py`  
> **Time:** ~2–3 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | 2D lists in Python | `"python list of lists 2d grid"` |
| 2 | List comprehension | `"python nested list comprehension"` |
| 3 | Pixel ↔ grid math | Read the section below |

### Pixel ↔ Grid Conversion (key concept)

Your grid is drawn starting at `(GRID_OFFSET_X, GRID_OFFSET_Y)`. Each cell is `CELL_SIZE` pixels wide/tall.

**Mouse pixel → grid cell:**
```
col = (mouse_x - GRID_OFFSET_X) // CELL_SIZE
row = (mouse_y - GRID_OFFSET_Y) // CELL_SIZE
```

**Grid cell → pixel (top-left corner):**
```
px = GRID_OFFSET_X + col * CELL_SIZE
py = GRID_OFFSET_Y + row * CELL_SIZE
```

**Bounds check:** Only valid if `0 <= row < GRID_ROWS` and `0 <= col < GRID_COLS`.

---

## Task 2.1 — Create `grid.py`

Write these 5 functions:

### `create_grid(rows, cols) → list[list[int]]`
- Use nested list comprehension: `[[0 for _ in range(cols)] for _ in range(rows)]`
- Every cell starts as `0` (EMPTY)
- Call with `create_grid(GRID_ROWS, GRID_COLS)` → 20 rows × 30 cols

### `reset_grid(grid)`
- Loop through every cell and set to `0`

### `pixel_to_cell(mx, my) → tuple or None`
- Convert using the formulas above
- If result is out of bounds → return `None`
- Otherwise → return `(row, col)`

### `cell_to_pixel(row, col) → tuple`
- Returns `(px, py)` — the top-left pixel of that cell

### `count_walls(grid) → int`
- Count all cells where value == `1`
- Use: `sum(1 for row in grid for cell in row if cell == WALL)`

**✅ Acceptance:** Open a Python shell, import `grid`, call `create_grid(20, 30)` — returns 20 lists of 30 zeros.

---

## Task 2.2 — Create `editor.py` with `draw_grid()`

Write `draw_grid(screen, grid)`:

For every `row` in range `GRID_ROWS`, for every `col` in range `GRID_COLS`:

1. Get pixel position: `px, py = cell_to_pixel(row, col)`
2. Determine color based on cell value:
   - `0` (EMPTY) → `GRID_BG` → `(30, 30, 50)`
   - `1` (WALL) → `WALL_COLOR` → `(80, 80, 110)`
   - `2` (START) → `START_COLOR` → `(0, 200, 120)`
   - `3` (END) → `END_COLOR` → `(220, 50, 50)`
3. Draw **filled** rect: `pygame.draw.rect(screen, color, (px, py, CELL_SIZE, CELL_SIZE))`
4. Draw **border** rect: `pygame.draw.rect(screen, GRID_LINE, (px, py, CELL_SIZE, CELL_SIZE), 1)`

### Target layout:

```
┌────────────────────────────────────────────────────────────────┐
│  MAZE EDITOR                                       [RACE!]    │
│  ┌──────────────────────────────────────────────┐  ┌────────┐ │
│  │ ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐   │  │        │ │
│  │ │  │  │  │  │  │  │  │  │  │  │  │  │  │   │  │Sidebar │ │
│  │ ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤   │  │(Day 3) │ │
│  │ │  │  │  │  │  │  │  │  │  │  │  │  │  │   │  │        │ │
│  │ ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤   │  │        │ │
│  │ │  │  │  │  │  │  │  │  │  │  │  │  │  │   │  │        │ │
│  │ └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘   │  │        │ │
│  │           30 cols × 20 rows                  │  │        │ │
│  │           900 px × 600 px                    │  │        │ │
│  └──────────────────────────────────────────────┘  └────────┘ │
└────────────────────────────────────────────────────────────────┘
```

### Wire into `main.py`:

1. At the top of `main.py`, create the grid: `grid = create_grid(GRID_ROWS, GRID_COLS)`
2. In the main loop, when `state == "EDITOR"`:
   - `screen.fill(BG_DARK)`
   - Draw a header: `draw_text(screen, "MAZE EDITOR", 20, 20, BUTTON_FONT_SIZE, WHITE)`
   - Call `draw_grid(screen, grid)`

**✅ Acceptance:** Click START on menu → see a grid of 30×20 dark cells with visible grid lines. All cells are the same color (empty).

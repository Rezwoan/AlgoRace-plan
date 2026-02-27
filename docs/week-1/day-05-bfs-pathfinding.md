# Day 5 — BFS Pathfinding

> **Goal:** Implement BFS that finds the shortest path on the grid. Visualize it.  
> **Files to create:** `pathfinding.py`  
> **Time:** ~3–4 hours (this is the most algorithmic day)

---

## 📚 What to Learn First

| # | Topic | What to Search | Time |
|---|---|---|---|
| 1 | BFS concept | `"BFS grid pathfinding python visualization"` | 30 min |
| 2 | `collections.deque` | `"python deque popleft BFS example"` | 10 min |
| 3 | Reconstruct path | `"BFS parent dictionary reconstruct path"` | 15 min |

### BFS in Plain English

Imagine you're dropping a stone in water at the START cell. The ripple spreads outward, one ring at a time. Each ring is one "step" away. When the ripple reaches END, you know the shortest distance.

**Step-by-step:**

1. Put START in a queue
2. Mark START as visited
3. While queue is not empty:
   - Pop the **front** cell from the queue
   - If it's END → done! Trace the path backwards
   - For each neighbor (up/down/left/right):
     - Skip if: out of bounds, is a wall, already visited
     - Mark as visited
     - Record `parent[neighbor] = current_cell`
     - Add neighbor to back of queue
4. If queue empties and END never reached → no path exists

**Reconstruct path:** Start at END, follow `parent` pointers back to START, then reverse the list.

---

## Task 5.1 — Write `get_neighbors(row, col, grid)`

In `pathfinding.py`:

Returns a list of `(r, c)` tuples for valid, non-wall neighbors.

4 directions to check:
```
(row - 1, col)   # up
(row + 1, col)   # down
(row, col - 1)   # left
(row, col + 1)   # right
```

For each:
- Skip if `r < 0` or `r >= GRID_ROWS` or `c < 0` or `c >= GRID_COLS`
- Skip if `grid[r][c] == WALL`
- Otherwise add `(r, c)` to result

---

## Task 5.2 — Write `find_path_bfs(grid, start, end)`

Parameters:
- `grid`: the 2D list
- `start`: `(row, col)` tuple
- `end`: `(row, col)` tuple

Returns: `list[(row, col)]` from start to end, or `None` if no path.

Implementation:
```
from collections import deque

1. queue = deque()
2. queue.append(start)
3. visited = {start}
4. parent = {start: None}

5. while len(queue) > 0:
     current = queue.popleft()
     
     if current == end:
         # Reconstruct path
         path = []
         cell = end
         while cell is not None:
             path.append(cell)
             cell = parent[cell]
         path.reverse()
         return path
     
     for neighbor in get_neighbors(current[0], current[1], grid):
         if neighbor not in visited:
             visited.add(neighbor)
             parent[neighbor] = current
             queue.append(neighbor)

6. return None  # no path found
```

**✅ Acceptance:** Create a simple grid manually, set some walls, call `find_path_bfs()` → returns a list of cells from start to end going around walls.

---

## Task 5.3 — Draw the path as overlay

Write `draw_path(screen, path)`:

For each `(row, col)` in `path`:
1. Get pixel: `px, py = cell_to_pixel(row, col)`
2. Draw a small colored dot centered in the cell:
   - `center_x = px + CELL_SIZE // 2`
   - `center_y = py + CELL_SIZE // 2`
   - `pygame.draw.circle(screen, PATH_COLOR, (center_x, center_y), CELL_SIZE // 4)`

In the editor screen, after placing both start and end:
1. `start = find_cell(grid, START)`
2. `end = find_cell(grid, END)`
3. If both exist → `path = find_path_bfs(grid, start, end)`
4. If `path` → `draw_path(screen, path)`

> Recalculate path each frame (it's fast for 30×20 grids). Or recalculate only when grid changes.

**✅ Acceptance:** Place Start, End, and some walls. Yellow dots show the shortest path. Move a wall → path updates.

---

## Task 5.4 — Upgrade to A* (do this AFTER BFS works perfectly)

> **Only proceed here if BFS is 100% working.** A* is better but BFS gives you full marks for pathfinding.

Write `find_path_astar(grid, start, end)`:

### Differences from BFS:

| BFS | A* |
|---|---|
| Uses `deque` (FIFO queue) | Uses `heapq` (priority queue / min-heap) |
| Explores equally in all directions | Explores toward the goal first |
| Always finds shortest path | Also finds shortest path, but faster |

### Heuristic:
Manhattan distance: `h = abs(row - end[0]) + abs(col - end[1])`

### Implementation:
```
import heapq

1. counter = 0  # tiebreaker for equal f-scores
2. open_set = [(h(start), counter, start)]  # (f_score, counter, cell)
3. g_score = {start: 0}
4. parent = {start: None}
5. visited = set()

6. while open_set:
     _, _, current = heapq.heappop(open_set)
     
     if current in visited:
         continue
     visited.add(current)
     
     if current == end:
         # reconstruct (same as BFS)
     
     for neighbor in get_neighbors(current[0], current[1], grid):
         new_g = g_score[current] + 1
         if neighbor not in g_score or new_g < g_score[neighbor]:
             g_score[neighbor] = new_g
             f = new_g + h(neighbor)
             counter += 1
             heapq.heappush(open_set, (f, counter, neighbor))
             parent[neighbor] = current

7. return None
```

> **Why the counter?** When two cells have the same f-score, Python tries to compare the tuples `(row, col)`. The counter prevents that comparison.

**✅ Acceptance:** Replace BFS with A* — same path result, works correctly.

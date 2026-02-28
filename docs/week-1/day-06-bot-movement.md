# Day 6 — Bot Animated Movement

> **Goal:** Bot computes a path and visibly walks along it, one cell at a time.  
> **Files to create:** `bot.py`  
> **Time:** ~2 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Timed events | `"pygame.time.get_ticks movement delay"` |

> **Key concept:** `pygame.time.get_ticks()` returns milliseconds since `pygame.init()`.  
> To move the bot every 80ms, store the last move time and check if enough time has passed.

---

## Task 6.1 — Create `bot.py`

### Bot state (dict, no class):

```
bot = {
    "path": [],            # list of (row, col) from pathfinding
    "path_index": 0,       # which step bot is on (0 = start)
    "row": 0,              # current grid position
    "col": 0,
    "active": False,       # is the bot currently racing?
    "finished": False,     # has bot reached the end?
    "last_move_time": 0    # timestamp (ms) of last step
}
```

### `init_bot(path) → dict`
- If `path` is `None` or empty → return bot with `active = False`
- Set `row, col` to `path[0]`
- Set `path = path`, `path_index = 0`
- Set `active = True`, `finished = False`
- Set `last_move_time = pygame.time.get_ticks()`

### `update_bot(bot)`
Called every frame during the race.

```
1. If not bot["active"] or bot["finished"]:
       return

2. current_time = pygame.time.get_ticks()

3. If current_time - bot["last_move_time"] >= BOT_MOVE_DELAY:
       bot["path_index"] += 1
       
       if bot["path_index"] >= len(bot["path"]):
           bot["finished"] = True
           return
       
       next_cell = bot["path"][bot["path_index"]]
       bot["row"] = next_cell[0]
       bot["col"] = next_cell[1]
       bot["last_move_time"] = current_time
```

### `draw_bot(screen, bot)`

1. Get pixel: `px, py = cell_to_pixel(bot["row"], bot["col"])`
2. Draw a **square** (to distinguish from player's circle):
   - Inset by 4px: `pygame.draw.rect(screen, BOT_COLOR, (px + 4, py + 4, CELL_SIZE - 8, CELL_SIZE - 8))`

> Player = circle (cyan), Bot = square (orange). Easy to tell apart.

---

## Task 6.2 — Test bot movement in editor (temporary)

For testing before the race system exists:

1. In the editor, after computing the path (Task 5.3), initialize the bot: `bot = init_bot(path)`
2. Set `bot["active"] = True`
3. In the update phase: call `update_bot(bot)`
4. In the draw phase: call `draw_bot(screen, bot)`

You should see the orange square step along the path every 80ms.

> **Remove this test code** after you build the race system on Day 7. The race system will control when the bot starts.

**✅ Acceptance:** Bot starts at START, moves along the computed path cell by cell, stops at END. Movement is smooth and timed (not instant).

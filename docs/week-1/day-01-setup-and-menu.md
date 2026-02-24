# Day 1 — Setup + Pygame Basics + Main Menu

> **Goal:** Open a window, draw a Main Menu with 3 buttons that react to clicks.  
> **Files to create:** `constants.py`, `main.py`, `ui_helpers.py`  
> **Time:** ~2–4 hours

---

## 📚 What to Learn First

Before writing any code, Google/YouTube these topics:

| # | Topic | What to Search | Time |
|---|---|---|---|
| 1 | Install Pygame | `"pip install pygame tutorial"` | 5 min |
| 2 | Window + event loop | `"pygame create window event loop beginner"` | 20 min |
| 3 | Drawing shapes | `"pygame draw rect text surface"` | 20 min |
| 4 | Fonts | `"pygame.font.SysFont example"` | 10 min |
| 5 | Mouse events | `"pygame MOUSEMOTION MOUSEBUTTONDOWN"` | 10 min |

### Key Pygame concepts cheat-sheet

| Code | What it does |
|---|---|
| `pygame.init()` | Initialize all Pygame modules |
| `pygame.display.set_mode((w, h))` | Create the window (returns `screen` surface) |
| `pygame.display.set_caption("title")` | Set window title bar text |
| `pygame.time.Clock()` | Create a clock to control FPS |
| `clock.tick(60)` | Limit loop to 60 frames per second |
| `pygame.event.get()` | Get all events this frame (keyboard, mouse, quit) |
| `screen.fill((r, g, b))` | Clear entire screen with a color |
| `pygame.draw.rect(screen, color, (x,y,w,h))` | Draw a filled rectangle |
| `pygame.draw.rect(screen, color, (x,y,w,h), 1)` | Draw rectangle border only |
| `pygame.font.SysFont("name", size)` | Create a font object |
| `font.render("text", True, color)` | Create a text surface |
| `screen.blit(surface, (x, y))` | Draw a surface onto the screen |
| `pygame.display.flip()` | Show everything drawn this frame |
| `pygame.quit()` | Clean up and close |

---

## Task 1.1 — Create `constants.py`

Open the [constants spec](../specs/constants.md) and type every constant into a new file `constants.py`.

All values are plain variables at the top level — no classes, no functions:

```
# constants.py
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 60
BG_DARK = (18, 18, 30)
# ... etc, copy ALL values from the spec
```

**✅ Acceptance:** Run `python constants.py` — no errors, no output.

---

## Task 1.2 — Create `main.py` with an empty window

Create `main.py` with this structure:

1. `import pygame` and `from constants import *`
2. Call `pygame.init()`
3. Create display surface: `screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))`
4. Set caption: `pygame.display.set_caption("S.N.A.P. — Maze Race")`
5. Create clock: `clock = pygame.time.Clock()`
6. Set `running = True`
7. Game loop (`while running:`):
   - `for event in pygame.event.get():`
     - Check `event.type == pygame.QUIT` → set `running = False`
   - `screen.fill(BG_DARK)`
   - `pygame.display.flip()`
   - `clock.tick(FPS)`
8. After loop: `pygame.quit()`

**✅ Acceptance:** A 1200×800 dark purple-black window opens. It closes cleanly when you click ✕.

---

## Task 1.3 — Create `ui_helpers.py`

Write two helper functions:

### `draw_text(screen, text, x, y, size, color, center=False)`

1. Create font: `font = pygame.font.SysFont(FONT_NAME, size)`
2. Render text: `surf = font.render(text, True, color)`
3. If `center` is `True`: get rect and set `rect.center = (x, y)`
4. Else: `rect = surf.get_rect(topleft=(x, y))`
5. Blit: `screen.blit(surf, rect)`

### `draw_button(screen, text, x, y, w, h, mouse_pos) → bool`

1. Create a `pygame.Rect(x, y, w, h)`
2. Check if `mouse_pos` is inside the rect (`rect.collidepoint(mouse_pos)`)
3. If hovered → fill with `BTN_HOVER`, else → fill with `BTN_NORMAL`
4. Draw the filled rect with `pygame.draw.rect()`
5. Also draw a 1px border in a slightly lighter color
6. Render text centered inside the rect (use `get_rect(center=rect.center)`)
7. Return `True` if hovered, `False` otherwise

> **Why return hovered?** So in your click handler, you can check:  
> `if event.type == MOUSEBUTTONDOWN and start_hovered: ...`

**✅ Acceptance:** You can import these and draw a button on screen that changes color when hovered.

---

## Task 1.4 — Draw the Main Menu

### Target layout:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│                          S.N.A.P.                           │
│                Shortest-path Navigation                     │
│                 Algorithm Playground                        │
│                                                             │
│                                                             │
│                     ┌──────────────┐                        │
│                     │   ▶ START    │                        │
│                     └──────────────┘                        │
│                                                             │
│                     ┌──────────────┐                        │
│                     │  📜 HISTORY  │                        │
│                     └──────────────┘                        │
│                                                             │
│                     ┌──────────────┐                        │
│                     │   ✕ EXIT    │                         │
│                     └──────────────┘                        │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Exact positions:

| Element | x | y | Size | Color |
|---|---|---|---|---|
| Title `"S.N.A.P."` | centered (`600`) | `200` | `48` | `GOLD` |
| Subtitle line 1 `"Shortest-path Navigation"` | centered | `260` | `20` | `WHITE` |
| Subtitle line 2 `"Algorithm Playground"` | centered | `285` | `20` | `WHITE` |
| Button `"START"` | `470` | `380` | `260×60` | — |
| Button `"HISTORY"` | `470` | `460` | `260×60` | — |
| Button `"EXIT"` | `470` | `540` | `260×60` | — |

### Implementation in `main.py`:

1. Add `state = "MENU"` before the game loop
2. Inside the loop, add `mouse_pos = pygame.mouse.get_pos()`
3. When `state == "MENU"`:
   - Draw the title and subtitle using `draw_text()` with `center=True`
   - Draw 3 buttons using `draw_button()`, storing their hover state
   - In the event loop, on `MOUSEBUTTONDOWN` (left button):
     - If START is hovered → `state = "EDITOR"`
     - If HISTORY is hovered → `state = "HISTORY"`
     - If EXIT is hovered → `running = False`

**✅ Acceptance:**
- Menu renders with title in gold, subtitle in white, 3 buttons
- Buttons change color when mouse hovers over them
- Clicking EXIT closes the window
- Clicking START or HISTORY changes `state` (screen goes blank — that's expected, you'll build those screens next)

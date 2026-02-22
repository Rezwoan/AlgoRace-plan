# State Machine — Screen Flow

> Your game has 5 screens (states). The main loop checks `state` and calls the right functions.

---

## Flow Diagram

```
                    ┌──────────┐
          ┌────────►│   MENU   │◄────────────────┐
          │         └──┬───┬───┘                  │
          │            │   │                      │
          │   "Start"  │   │  "History"           │
          │            ▼   ▼                      │
          │     ┌────────┐  ┌─────────┐           │
          │     │ EDITOR │  │ HISTORY │           │
          │     └───┬────┘  └────┬────┘           │
          │         │            │                │
          │  ENTER  │       "Back" ───────────────┤
          │  key    │                             │
          │         ▼                             │
          │     ┌────────┐                        │
          │     │  RACE  │                        │
          │     └───┬────┘                        │
          │         │                             │
          │   Both  │ finish                      │
          │         ▼                             │
          │     ┌────────┐                        │
          │     │ RESULT │                        │
          │     └───┬──┬─┘                        │
          │         │  │                          │
          │ "Play   │  │  "Main                   │
          │  Again" │  │   Menu"                  │
          │         │  └──────────────────────────┘
          │         │
          │         ▼
          │     ┌────────┐
          └─────┤ EDITOR │  (grid is preserved)
                └────────┘
```

---

## How It Works in Code

In `main.py`, you have one variable:

```
state = "MENU"
```

The game loop does:

```
while running:
    events = pygame.event.get()

    if state == "MENU":
        menu_handle_events(events)
        menu_draw(screen)

    elif state == "EDITOR":
        editor_handle_events(events)
        editor_draw(screen)

    elif state == "RACE":
        race_handle_events(events)
        race_update()
        race_draw(screen)

    elif state == "RESULT":
        result_handle_events(events)
        result_draw(screen)

    elif state == "HISTORY":
        history_handle_events(events)
        history_draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
```

Each screen's `handle_events()` function can change `state` to trigger transitions.

---

## State Transitions Table

| From | Trigger | To | Notes |
|---|---|---|---|
| MENU | Click "Start" | EDITOR | Creates fresh grid |
| MENU | Click "History" | HISTORY | Loads records from JSON |
| MENU | Click "Exit" | — | `running = False` |
| EDITOR | Press ENTER or click "Race!" | RACE | Only if Start AND End are placed |
| RACE | Both player & bot finish | RESULT | Auto-saves match record |
| RESULT | Click "Play Again" | EDITOR | Keeps current grid |
| RESULT | Click "Main Menu" | MENU | — |
| HISTORY | Click "Back" | MENU | — |

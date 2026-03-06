# MVP Checklist (Minimum Viable Project)

> If you finish everything on this list, you have a passing project.  
> Check each item off as you complete it.

---

## Core Gameplay
- [ ] Window opens at 1200×800, titled "S.N.A.P."
- [ ] 60 FPS, smooth rendering
- [ ] Main Menu with 3 buttons (Start / History / Exit)
- [ ] Grid editor: 30×20 grid rendered with colored cells
- [ ] Click to toggle walls
- [ ] S + Click to place Start (one only)
- [ ] E + Click to place End (one only)
- [ ] C to clear the whole grid
- [ ] Player appears at Start cell
- [ ] Arrow keys move player one cell per press
- [ ] Player blocked by walls and grid edges

## Pathfinding
- [ ] BFS finds shortest path on the grid
- [ ] Path displayed as visual overlay
- [ ] Bot follows the computed path step-by-step
- [ ] Bot moves on a timer (not instant)

## Race
- [ ] Race starts on ENTER (timer begins)
- [ ] Player races with arrow keys, bot auto-moves
- [ ] Winner detected when both finish
- [ ] Result screen shows winner + times

## Persistence (CRUD)
- [ ] **Create:** Match auto-saved to `match_history.json`
- [ ] **Read:** History screen shows all records in table
- [ ] **Update:** Rename player name on a record
- [ ] **Delete:** Remove a record permanently

## Search & Analytics
- [ ] Sort records by time / date
- [ ] Filter by winner (Human / Bot / All)
- [ ] Show total win/loss percentage
- [ ] Show top 3 fastest human times

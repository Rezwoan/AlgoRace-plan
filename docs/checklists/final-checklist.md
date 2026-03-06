# Final Checklist (MVP + Optional Polish)

> Everything from the MVP, plus nice-to-have features.

---

## MVP Items (must have)
- [ ] Window 1200×800, 60 FPS
- [ ] Main Menu with Start / History / Exit
- [ ] Grid editor 30×20 with wall toggle
- [ ] Start/End placement (S/E + click)
- [ ] Clear grid (C key)
- [ ] Player movement + collision
- [ ] BFS pathfinding (shortest path)
- [ ] Bot animated movement along path
- [ ] Race: timer + winner detection
- [ ] Result screen with stats
- [ ] Auto-save to JSON (Create)
- [ ] History table display (Read)
- [ ] Delete record (Delete)
- [ ] Rename player (Update)
- [ ] Sort by time / date
- [ ] Filter by winner
- [ ] Win/loss % analytics
- [ ] Top 3 human times

## Edge Cases (must handle)
- [ ] No Start/End placed → show error, don't start race
- [ ] No valid path → show error message
- [ ] Bot has no path → human auto-wins
- [ ] Empty/corrupt JSON → gracefully return `[]`
- [ ] Empty rename text → keep old name
- [ ] 0 records → show "no matches" message

## Optional Polish (nice to have)
- [ ] A* pathfinding (upgrade from BFS)
- [ ] Click-and-drag wall painting
- [ ] Controls help overlay (H key)
- [ ] Visual A* expansion animation
- [ ] Disabled button styling (grayed out when nothing selected)
- [ ] Scrollable history list (if many records)
- [ ] Blinking cursor in rename input box

## Demo Prep
- [ ] Pre-populate 3–4 match records
- [ ] Rehearse the 20-step demo script (see Day 14)
- [ ] Verify JSON persists across restarts
- [ ] No crashes on any edge case

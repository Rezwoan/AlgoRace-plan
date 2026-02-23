# S.N.A.P. — Project Plan

> **S**hortest-path **N**avigation **A**lgorithm **P**layground  
> University Python Course · Pygame · 14-Day Build

---

## 📂 How This Plan is Organized

```
docs/
├── README.md                  ← You are here
│
├── specs/                     ← Read these FIRST
│   ├── constants.md           Constants, colors, sizes — the "source of truth"
│   ├── file-structure.md      What files you'll create and why
│   ├── state-machine.md       How screens connect (Menu → Editor → Race…)
│   └── data-model.md          JSON record format for match history
│
├── week-1/                    ← Core engine & gameplay
│   ├── day-01-setup-and-menu.md
│   ├── day-02-grid-rendering.md
│   ├── day-03-editor-tools.md
│   ├── day-04-player-movement.md
│   ├── day-05-bfs-pathfinding.md
│   ├── day-06-bot-movement.md
│   └── day-07-race-and-timer.md
│
├── week-2/                    ← Persistence, CRUD, polish
│   ├── day-08-save-records.md
│   ├── day-09-history-screen.md
│   ├── day-10-delete-record.md
│   ├── day-11-rename-player.md
│   ├── day-12-sort-and-filter.md
│   ├── day-13-analytics.md
│   └── day-14-polish-and-demo.md
│
└── checklists/
    ├── mvp-checklist.md       Minimum you need to pass
    └── final-checklist.md     Everything, including optional polish
```

---

## 🚀 How to Use This Plan

1. **Start by reading everything in `specs/`** — it defines sizes, colors, file layout, and the state machine you'll use throughout.
2. **Work through `week-1/` day by day.** Each file is one day's work (2–4 hours).
3. **Continue with `week-2/`.** CRUD, history, analytics, and polish.
4. **Track your progress** with the checklists in `checklists/`.

Each day file has:
- **📚 What to Learn First** — topics to Google with exact search terms
- **Tasks** — numbered, specific, with exact positions/sizes/colors
- **ASCII mockups** — so you know what the screen should look like
- **Acceptance criteria** — how to know you're done

---

## 🎯 MVP (Minimum Viable Project)

If you finish only this, you still pass:

- ✅ Main Menu (Start / History / Exit)
- ✅ Grid editor (click walls, place Start/End)
- ✅ Player movement + collision
- ✅ Bot pathfinding (BFS is fine, A* is better)
- ✅ Timer + winner detection
- ✅ Save match to JSON
- ✅ View / Delete / Rename history records
- ✅ Win/loss % and top 3 human times

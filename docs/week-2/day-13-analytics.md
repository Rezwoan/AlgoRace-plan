# Day 13 — Analytics Dashboard

> **Goal:** Show win/loss percentage and top 3 fastest human times on the history screen.  
> **Files to create:** `analytics.py`, update `history_screen.py`  
> **Time:** ~1–2 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Percentage calc | Just `count / total * 100` |
| 2 | Top N from list | `sorted(list)[:3]` |

---

## Task 13.1 — Create `analytics.py`

### `compute_analytics(records) → dict`

```
1. total = len(records)

2. If total == 0, return:
     {
       "total": 0,
       "human_wins": 0,
       "bot_wins": 0,
       "human_win_pct": 0.0,
       "bot_win_pct": 0.0,
       "top3_human_times": []
     }

3. human_wins = sum(1 for r in records if r["winner"] == "Human")
4. bot_wins = total - human_wins
5. human_win_pct = round((human_wins / total) * 100, 1)
6. bot_win_pct = round((bot_wins / total) * 100, 1)

7. all_human_times = [r["human_time"] for r in records]
8. all_human_times.sort()                # ascending = fastest first
9. top3 = all_human_times[:3]            # take up to 3

10. Return the dict with all values
```

---

## Task 13.2 — Display analytics on history screen

### Layout (bottom of history screen):

```
┌──────────────────────────────────────────────────────────────┐
│  ── Analytics ───────────────────────────────────────────── │
│  Total Matches: 15  │  Human Wins: 60.0%  │  Bot Wins: 40.0%│
│  🏆 Top 3 Human Times: 8.44s, 10.12s, 12.53s               │
└──────────────────────────────────────────────────────────────┘
```

### Positions:

| Element | x | y | Size | Color |
|---|---|---|---|---|
| Divider line | `30` to `1170` | `630` | 1px | `GRID_LINE` |
| "Analytics" title | `30` | `640` | `22` | `GOLD` |
| Stats line | `30` | `670` | `18` | `WHITE` |
| Top 3 line | `30` | `700` | `18` | `GOLD` |

### Drawing:

```
stats = compute_analytics(records)  # use ALL records, not filtered

# Divider
pygame.draw.line(screen, GRID_LINE, (30, 630), (1170, 630), 1)

# Title
draw_text(screen, "Analytics", 30, 640, 22, GOLD)

# Stats
stats_text = (
    f"Total: {stats['total']}  |  "
    f"Human Wins: {stats['human_win_pct']}%  |  "
    f"Bot Wins: {stats['bot_win_pct']}%"
)
draw_text(screen, stats_text, 30, 670, 18, WHITE)

# Top 3
if stats["top3_human_times"]:
    times = ", ".join(f"{t:.2f}s" for t in stats["top3_human_times"])
    draw_text(screen, f"Top 3 Human Times: {times}", 30, 700, 18, GOLD)
else:
    draw_text(screen, "No human times recorded yet.", 30, 700, 18, WHITE)
```

### Edge cases:
- 0 records → show "No matches yet" and skip the stats
- 1 record → top 3 shows just 1 time
- 2 records → top 3 shows 2 times

**✅ Acceptance:**
1. Play 3+ matches (mix of human/bot wins)
2. Go to History → analytics section at bottom shows correct percentages
3. Top 3 times are correct and sorted fastest-first
4. Delete all records → analytics shows zeros / "no matches" gracefully

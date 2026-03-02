# Day 10 — Delete Record (Delete)

> **Goal:** Select a record and delete it permanently.  
> **Files:** Update `history.py`, update `history_screen.py`  
> **Time:** ~1–2 hours

---

## Task 10.1 — Add `delete_record()` to `history.py`

### `delete_record(record_id)`

```
1. records = load_history()
2. records = [r for r in records if r["id"] != record_id]
3. save_history(records)
```

> Uses list comprehension to keep all records EXCEPT the one with the matching id.

---

## Task 10.2 — Wire DELETE button in history screen

On clicking the "DELETE" button `(30, 520)`:

```
1. If selected_index is None → do nothing (no record selected)
2. Get the record: record = display_records[selected_index]
3. Call delete_record(record["id"])
4. Reload: records = load_history()
5. Reapply current filter/sort to get display_records
6. Reset selected_index = None
```

### Visual feedback (optional but nice):
- Disable button (draw grayed out) when nothing is selected
- Draw disabled button in a darker color like `(35, 35, 60)` with dimmer text `(120, 120, 140)`

**✅ Acceptance:**
1. Play 2+ races so you have records
2. Go to History → select a record → click Delete → it vanishes
3. Go to Menu → come back to History → still deleted (persisted)
4. Open `match_history.json` → record is actually gone

**CRUD progress: ✅ Create, ✅ Read, ◻ Update, ✅ Delete**

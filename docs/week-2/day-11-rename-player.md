# Day 11 — Rename Player (Update)

> **Goal:** Select a record, click Rename, type a new name, press Enter to confirm.  
> **Files:** Update `history.py`, update `history_screen.py`  
> **Time:** ~2–3 hours

---

## 📚 What to Learn First

| # | Topic | What to Search |
|---|---|---|
| 1 | Text input in Pygame | `"pygame text input KEYDOWN unicode example"` |

### How Pygame text input works:

On `KEYDOWN` events:
- `event.unicode` gives the typed character (e.g., `"a"`, `"B"`, `"3"`)
- `event.key == pygame.K_RETURN` → Enter pressed (confirm)
- `event.key == pygame.K_ESCAPE` → Escape pressed (cancel)
- `event.key == pygame.K_BACKSPACE` → delete last character

Build a string character by character:
```
text = ""
# on KEYDOWN:
if event.key == K_BACKSPACE:
    text = text[:-1]
elif event.key == K_RETURN:
    # confirm
elif event.unicode.isalnum() or event.unicode == " ":
    if len(text) < 12:
        text += event.unicode
```

---

## Task 11.1 — Add `rename_record()` to `history.py`

### `rename_record(record_id, new_name)`

```
1. records = load_history()
2. for r in records:
       if r["id"] == record_id:
           r["player_name"] = new_name
           break
3. save_history(records)
```

---

## Task 11.2 — Add rename mode to history screen

### New state variables:

```
renaming = False
rename_text = ""
rename_record_id = None
```

### When "RENAME" button is clicked:

```
1. If selected_index is None → do nothing
2. record = display_records[selected_index]
3. renaming = True
4. rename_record_id = record["id"]
5. rename_text = record["player_name"]  # pre-fill with current name
```

### While `renaming == True`:

**Event handling changes:**
- `KEYDOWN` with `K_RETURN`:
  - If `rename_text` is not empty → call `rename_record(rename_record_id, rename_text)`
  - Reload records
  - Set `renaming = False`
- `KEYDOWN` with `K_ESCAPE`:
  - Set `renaming = False` (cancel, no save)
- `KEYDOWN` with `K_BACKSPACE`:
  - `rename_text = rename_text[:-1]`
- Other `KEYDOWN`:
  - If `event.unicode` is alphanumeric or space, and `len(rename_text) < 12`:
  - `rename_text += event.unicode`

**Drawing changes:**
Draw an input box over the Player column of the selected row:

```
Normal row:
│  3  │ 2026-03-07 │ Player1  │ Human  │ ...

During rename:
│  3  │ 2026-03-07 │┌──────────┐│ Human  │ ...
                    ││SpeedK_   ││
                    │└──────────┘│
```

Input box specs:
- Position: `x = 295`, `y = 100 + selected_index * 30 - 2`
- Size: `140 × 26`
- Background: `BG_DARK`
- Border: `WHITE`, 2px
- Text: `rename_text + "_"` (blinking cursor — or just always show `_`)
- Font: `SMALL_FONT_SIZE` (18)

> **Tip:** Also draw an instruction text below the table: `"Type name + Enter to confirm, Esc to cancel"` when renaming.

**✅ Acceptance:**
1. Select a record → click Rename
2. Input box appears with current name
3. Type "SpeedKing" → text updates live
4. Press Enter → name changes in the list
5. Check `match_history.json` → name is updated
6. Press Escape instead → cancels, name unchanged

**CRUD progress: ✅ Create, ✅ Read, ✅ Update, ✅ Delete — COMPLETE!**

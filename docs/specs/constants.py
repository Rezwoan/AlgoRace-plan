# =============================================================================
# constants.py — AlgoRace
# Single source of truth for all magic numbers, colours, and layout values.
# Every other module imports from here; nothing is hard-coded elsewhere.
# =============================================================================

# -----------------------------------------------------------------------------
# Window
# -----------------------------------------------------------------------------
WINDOW_TITLE   = "AlgoRace"
FPS            = 60

# -----------------------------------------------------------------------------
# Grid
# -----------------------------------------------------------------------------
COLS           = 20          # number of columns
ROWS           = 20          # number of rows
CELL_SIZE      = 36          # pixels per cell (must divide evenly into grid area)

GRID_WIDTH     = COLS * CELL_SIZE   # 720 px
GRID_HEIGHT    = ROWS * CELL_SIZE   # 720 px

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
SIDEBAR_WIDTH  = 200         # px — sits to the right of the grid

# -----------------------------------------------------------------------------
# Derived window size  (single place — change CELL_SIZE / SIDEBAR_WIDTH above)
# -----------------------------------------------------------------------------
WIN_WIDTH      = GRID_WIDTH  + SIDEBAR_WIDTH   # 920 px
WIN_HEIGHT     = GRID_HEIGHT                   # 720 px

# -----------------------------------------------------------------------------
# Cell states  (stored in grid[][])
# -----------------------------------------------------------------------------
EMPTY          = 0
WALL           = 1
START          = 2
END            = 3

# -----------------------------------------------------------------------------
# Colours  (R, G, B)
# -----------------------------------------------------------------------------

# -- Grid cells --
CLR_EMPTY      = (18,  18,  18)   # near-black background
CLR_WALL       = (60,  60,  60)   # dark grey wall
CLR_START      = (39, 174,  96)   # green
CLR_END        = (192,  57,  43)  # red
CLR_GRID_LINE  = (35,  35,  35)   # subtle grid lines

# -- Actors --
CLR_PLAYER     = (0,  210, 210)   # cyan
CLR_BOT        = (255, 165,   0)  # orange

# -- Pathfinding overlay --
CLR_VISITED    = (30,  80, 120)   # dim blue — BFS/A* explored
CLR_PATH       = (80, 180, 255)   # bright blue — final path

# -- UI / sidebar --
CLR_SIDEBAR_BG = (12,  12,  12)
CLR_TEXT       = (220, 220, 220)
CLR_TEXT_DIM   = (120, 120, 120)
CLR_BTN_NORMAL = (39, 174,  96)   # same green as START for consistency
CLR_BTN_HOVER  = (46, 204, 113)
CLR_BTN_TEXT   = (255, 255, 255)

# -- Result screen tints --
CLR_WIN        = (39, 174,  96)   # player wins → green flash
CLR_LOSE       = (192,  57,  43)  # bot wins    → red flash

# -- Misc --
CLR_WHITE      = (255, 255, 255)
CLR_BLACK      = (  0,   0,   0)

# -----------------------------------------------------------------------------
# Typography
# -----------------------------------------------------------------------------
FONT_PATH      = None        # None → Pygame default; swap for a .ttf path later

FONT_SIZE_SM   = 14          # legend / labels
FONT_SIZE_MD   = 18          # sidebar body text
FONT_SIZE_LG   = 24          # headings / result screen
FONT_SIZE_XL   = 48          # "YOU WIN!" / "BOT WINS!"

# -----------------------------------------------------------------------------
# Sidebar layout  (Y-positions measured from window top)
# -----------------------------------------------------------------------------
SIDEBAR_X      = GRID_WIDTH              # 720 — left edge of sidebar
SIDEBAR_PAD    = 16                      # internal padding
BTN_RACE_Y     = WIN_HEIGHT - 70         # RACE! button near the bottom
BTN_WIDTH      = SIDEBAR_WIDTH - SIDEBAR_PAD * 2   # 168 px
BTN_HEIGHT     = 44

# -----------------------------------------------------------------------------
# Player / movement
# -----------------------------------------------------------------------------
PLAYER_RADIUS  = CELL_SIZE // 2 - 4     # circle slightly smaller than cell
BOT_RADIUS     = CELL_SIZE // 2 - 4

# Bot step interval during animated movement (ms between steps)
BOT_STEP_MS    = 120

# -----------------------------------------------------------------------------
# Race / result screen
# -----------------------------------------------------------------------------
RESULT_DISPLAY_MS = 3000     # how long the result screen is shown (ms)

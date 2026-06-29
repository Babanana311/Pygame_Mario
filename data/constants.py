"""
游戏常量定义模块

包含：
- 屏幕尺寸与缩放
- 物理常量（重力、跳跃速度等）
- 角色/敌人/关卡状态字符串
- 道具/方块内容物类型
- 音效状态
"""

# ---- 屏幕尺寸 ----
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros 1-1"

# ---- 颜色定义 ----

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

# ---- 缩放倍率 ----
SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

# ---- 物理常量 ----
WALK_ACCEL = .15           # 行走加速度
RUN_ACCEL = 20             # 奔跑加速度
SMALL_TURNAROUND = .35     # 小马里奥转向减速

GRAVITY = 1.01             # 正常重力
JUMP_GRAVITY = .31         # 跳跃时重力（按住跳跃键时使用）
JUMP_VEL = -12             # 跳跃初速度（负值向上）
FAST_JUMP_VEL = -12.5      # 快速跳跃初速度
MAX_Y_VEL = 11             # 最大下落速度

MAX_RUN_SPEED = 800        # 最大奔跑速度
MAX_WALK_SPEED = 6         # 最大行走速度


# ---- Mario 状态 ----
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'


# ---- 敌人方向与状态 ----
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

# ---- 乌龟龟壳状态 ----
SHELL_SLIDE = 'shell slide'

# ---- 砖块状态 ----
RESTING = 'resting'
BUMPED = 'bumped'

# ---- 问号方块状态 ----
OPENED = 'opened'

# ---- 蘑菇道具状态 ----
REVEAL = 'reveal'
SLIDE = 'slide'

# ---- 金币状态 ----
SPIN = 'spin'

# ---- 星星道具状态 ----
BOUNCE = 'bounce'

# ---- 火球状态 ----
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

# ---- 砖块/问号方块内容物类型 ----
MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

# ---- 敌人类型 ----
GOOMBA = 'goomba'
KOOPA = 'koopa'

# ---- 关卡内部状态 ----
FROZEN = 'frozen'                          # 冻结（过场动画中）
NOT_FROZEN = 'not frozen'                  # 正常游戏状态
IN_CASTLE = 'in castle'                   # 进入城堡
FLAG_AND_FIREWORKS = 'flag and fireworks'  # 旗杆和烟花

# ---- 旗杆状态 ----
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

# ---- 1UP 分数标记 ----
ONEUP = '379'

# ---- 主菜单光标状态 ----
PLAYER1 = '1 player'
PLAYER2 = '2 player'

# ---- OverheadInfo 显示状态 ----
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'


# ---- game_info 字典键名 ----
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

# ---- 游戏全局状态 ----
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

# ---- 音效状态 ----
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'

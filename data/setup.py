"""
Pygame 初始化与资源加载模块

职责：
- 初始化 Pygame 窗口和显示
- 加载所有游戏资源（图形、音乐、音效、字体）
- 提供全局资源字典供其他模块使用
"""

import os
import pygame as pg
from . import tools
from .import constants as c

ORIGINAL_CAPTION = c.ORIGINAL_CAPTION

# ---- Pygame 初始化 ----
os.environ['SDL_VIDEO_CENTERED'] = '1'   # 窗口居中
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])  # 只监听必要事件
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

# ---- 加载所有游戏资源 ----
FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
MUSIC = tools.load_all_music(os.path.join("resources","music"))
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))

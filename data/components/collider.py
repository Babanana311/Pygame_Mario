"""
碰撞体模块

包含 Collider 类：不可见的碰撞矩形，用于地面、管道、台阶碰撞检测。
"""

import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    """不可见碰撞体：用于地面、管道、台阶的碰撞检测"""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None


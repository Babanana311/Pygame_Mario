"""
检查点模块

包含 Checkpoint 类：不可见触发器，用于敌人生成和事件触发。
"""

import pygame as pg
from .. import constants as c


class Checkpoint(pg.sprite.Sprite):
    """不可见触发器：到达时生成敌人或触发事件"""
    def __init__(self, x, name, y=0, width=10, height=600):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name





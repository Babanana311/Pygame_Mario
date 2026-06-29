"""
城堡旗帜模块

关卡结束时城堡顶部的旗帜动画。
"""

import pygame as pg
from .. import setup
from .. import constants as c


class Flag(pg.sprite.Sprite):
    """城堡旗帜：关卡结束时从城堡上升起"""
    def __init__(self, x, y):
        """初始化旗帜位置和上升速度"""
        super(Flag, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.image = self.get_image(129, 2, 14, 14)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = 'rising'
        self.y_vel = -2
        self.target_height = y


    def get_image(self, x, y, width, height):
        """从精灵表中提取旗帜图片"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image

    def update(self, *args):
        """根据状态更新旗帜位置"""
        if self.state == 'rising':
            self.rising()
        elif self.state == 'resting':
            self.resting()

    def rising(self):
        """上升状态：旗帜向上移动"""
        self.rect.y += self.y_vel
        if self.rect.bottom <= self.target_height:
            self.state = 'resting'

    def resting(self):
        """静止状态：旗帜已到达目标位置"""
        pass

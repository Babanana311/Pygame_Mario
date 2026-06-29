"""
旗杆模块（关卡终点）

包含 Flag、Pole、Finial 三个组件，组成关卡终点的旗杆。
"""

import pygame as pg
from .. import setup
from .. import constants as c

class Flag(pg.sprite.Sprite):
    """旗帜：随Mario滑下旗杆"""
    def __init__(self, x, y):
        super(Flag, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_images()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.state = c.TOP_OF_POLE


    def setup_images(self):
        """创建动画帧列表"""
        self.frames = []

        self.frames.append(
            self.get_image(128, 32, 16, 16))


    def get_image(self, x, y, width, height):
        """从精灵表中提取图片"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        """每帧更新行为"""
        self.handle_state()


    def handle_state(self):
        """根据状态分发旗帜行为"""
        if self.state == c.TOP_OF_POLE:
            self.image = self.frames[0]
        elif self.state == c.SLIDE_DOWN:
            self.sliding_down()
        elif self.state == c.BOTTOM_OF_POLE:
            self.image = self.frames[0]


    def sliding_down(self):
        """旗杆顶部：Mario到达旗杆时触发滑下"""
        self.y_vel = 5
        self.rect.y += self.y_vel

        if self.rect.bottom >= 485:
            self.state = c.BOTTOM_OF_POLE


class Pole(pg.sprite.Sprite):
    """旗杆：旗帜滑动的主杆"""
    def __init__(self, x, y):
        super(Pole, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def setup_frames(self):
        """创建动画帧列表"""
        self.frames = []

        self.frames.append(
            self.get_image(263, 144, 2, 16))


    def get_image(self, x, y, width, height):
        """从精灵表中提取图片"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        """更新：静态元素无需更新"""
        pass


class Finial(pg.sprite.Sprite):
    """旗杆顶部装饰球"""
    def __init__(self, x, y):
        super(Finial, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y


    def setup_frames(self):
        """创建帧列表"""
        self.frames = []

        self.frames.append(
            self.get_image(228, 120, 8, 8))


    def get_image(self, x, y, width, height):
        """从精灵表中提取图片"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        pass




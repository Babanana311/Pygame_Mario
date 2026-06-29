import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin



"""
问号方块模块

包含 Coin_box 类：可被顶出道具或金币，支持 RESTING/BUMPED/OPENED 三状态
"""

import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin



class Coin_box(pg.sprite.Sprite):
    """问号方块：从下方撞击后弹出道具或金币"""
    def __init__(self, x, y, contents='coin', group=None):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']
        self.frames = []
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.animation_timer = 0
        self.first_half = True   # First half of animation cycle
        self.state = c.RESTING
        self.rest_height = y
        self.gravity = 1.2
        self.y_vel = 0
        self.contents = contents
        self.group = group


    def get_image(self, x, y, width, height):
        """从精灵表中提取图片并缩放"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):
        """创建动画帧列表"""
        self.frames.append(
            self.get_image(384, 0, 16, 16))
        self.frames.append(
            self.get_image(400, 0, 16, 16))
        self.frames.append(
            self.get_image(416, 0, 16, 16))
        self.frames.append(
            self.get_image(432, 0, 16, 16))


    def update(self, game_info):
        """每帧更新问号方块行为"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_states()


    def handle_states(self):
        """根据状态分发方块行为"""
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()


    def resting(self):
        """静止状态：闪烁动画效果"""
        if self.first_half:
            if self.frame_index == 0:
                if (self.current_time - self.animation_timer) > 375:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index < 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index == 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.animation_timer = self.current_time
        else:
            if self.frame_index == 1:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.animation_timer = self.current_time

        self.image = self.frames[self.frame_index]


    def bumped(self):
        """被撞击状态：弹起后落回原位"""
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y > self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = c.OPENED
            if self.contents == 'mushroom':
                self.group.add(powerups.Mushroom(self.rect.centerx, self.rect.y))
            elif self.contents == 'fireflower':
                self.group.add(powerups.FireFlower(self.rect.centerx, self.rect.y))
            elif self.contents == '1up_mushroom':
                self.group.add(powerups.LifeMushroom(self.rect.centerx, self.rect.y))


        self.frame_index = 3
        self.image = self.frames[self.frame_index]


    def start_bump(self, score_group):
        """触发撞击：弹出内容物并进入 BUMPED 状态"""
        self.y_vel = -6
        self.state = c.BUMPED

        if self.contents == 'coin':
            self.group.add(coin.Coin(self.rect.centerx,
                                     self.rect.y,
                                     score_group))
            setup.SFX['coin'].play()
        else:
            setup.SFX['powerup_appears'].play()


    def opened(self):
        """已打开状态：保持空方块外观"""
        pass












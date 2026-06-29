"""
游戏控制器与工具模块

包含：
- Control 类：游戏主控制器，管理主循环和状态切换
- _State 基类：所有游戏状态的抽象基类
- 资源加载函数：图形、音乐、音效、字体
"""

import os
import pygame as pg

# ---- 按键绑定 ----
keybinding = {
    'action':pg.K_s,      # S键：动作/火球
    'jump':pg.K_a,        # A键：跳跃
    'left':pg.K_LEFT,     # 左方向键
    'right':pg.K_RIGHT,   # 右方向键
    'down':pg.K_DOWN      # 下方向键：蹲下
}

class Control(object):
    """
    游戏主控制器

    管理游戏主循环、事件处理和状态切换。
    所有游戏状态通过 state_dict 注册，由 flip_state() 切换。
    """
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):
        """初始化状态字典和起始状态"""
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):
        """
        每帧更新：
        1. 获取当前时间戳（毫秒）
        2. 检查退出/切换标志
        3. 调用当前状态的 update
        """
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        """
        切换到下一个状态：
        1. 保存上一个状态名
        2. 清理当前状态（获取 persist 数据）
        3. 启动下一个状态（传入 persist 数据）
        """
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous


    def event_loop(self):
        """处理 Pygame 事件：退出、按键按下/释放"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)


    def toggle_show_fps(self, key):
        """F5键切换FPS显示"""
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)


    def main(self):
        """主游戏循环：事件 → 更新 → 渲染，固定60FPS"""
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)


class _State(object):
    """
    游戏状态抽象基类

    所有游戏状态（Menu, LoadScreen, Level1, GameOver 等）继承此类。
    通过 Control 统一管理状态生命周期。
    """
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False        # True 时 Control 切换到 next 状态
        self.quit = False        # True 时 Control 退出游戏
        self.next = None         # 下一个状态名称
        self.previous = None     # 上一个状态名称
        self.persist = {}        # 跨状态持久化数据

    def get_event(self, event):
        """处理单个事件（子类重写）"""
        pass

    def startup(self, current_time, persistant):
        """状态启动时调用，接收上一状态传递的持久化数据"""
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        """状态结束时调用，返回持久化数据给下一状态"""
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        """每帧更新（子类重写）"""
        pass



def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    """
    加载所有图形资源

    返回 {文件名: Surface} 字典，自动处理透明通道和颜色键
    """
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    """
    加载所有音乐资源

    返回 {文件名: 文件路径} 字典，Pygame音乐播放需要完整路径
    """
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_fonts(directory, accept=('.ttf')):
    """加载所有字体资源（复用 load_all_music 逻辑）"""
    return load_all_music(directory, accept)


def load_all_sfx(directory, accept=('.wav','.mpe','.ogg','.mdi')):
    """
    加载所有音效资源

    返回 {文件名: Sound} 字典，每个音效是独立的 Sound 对象
    """
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

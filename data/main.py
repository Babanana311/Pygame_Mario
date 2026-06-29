"""
游戏入口模块

创建 Control 控制器，注册所有游戏状态，启动主循环。

游戏状态流转：
    MAIN_MENU → LOAD_SCREEN → LEVEL1 → GAME_OVER / TIME_OUT → MAIN_MENU
"""

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c


def main():
    """初始化状态机并启动游戏主循环"""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1()}

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()

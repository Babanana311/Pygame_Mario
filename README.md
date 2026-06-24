# 超级马里奥游戏 - Pygame复刻版

基于Pygame框架开发的超级马里奥第一关复刻版，作为软件项目开发与实践课程的课程设计项目。

## 项目概述

本项目复刻了经典超级马里奥游戏的第一关，包含完整的游戏机制：
- 角色控制（移动、跳跃、蹲下）
- 敌人系统（栗子怪、乌龟）
- 道具系统（蘑菇、火焰花、星星、1UP蘑菇）
- 关卡交互（砖块、问号方块、旗杆）
- 音效和背景音乐

## 环境要求

- Python 3.12+
- Pygame 2.x

## 安装与运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行游戏
python mario_level_1.py
```

## 操作说明

| 按键 | 功能 |
|------|------|
| A键 | 跳跃 |
| S键 | 动作/火球 |
| 方向键←→ | 左右移动 |
| 方向键↓ | 蹲下 |
| Enter | 确认 |

## 项目结构

```
Pygame_Mario/
├── data/                  # 源代码
│   ├── main.py           # 游戏入口
│   ├── setup.py          # 初始化和资源加载
│   ├── tools.py          # 控制器和工具函数
│   ├── constants.py      # 常量定义
│   ├── game_sound.py     # 音效管理
│   ├── components/       # 游戏组件
│   │   ├── mario.py      # 玩家角色
│   │   ├── enemies.py    # 敌人系统
│   │   ├── bricks.py     # 砖块系统
│   │   ├── powerups.py   # 道具系统
│   │   └── ...
│   └── states/           # 游戏状态
│       ├── main_menu.py  # 主菜单
│       ├── load_screen.py # 加载界面
│       └── level1.py     # 关卡1
├── resources/            # 游戏资源
│   ├── graphics/         # 图片资源
│   ├── music/            # 背景音乐
│   ├── sound/            # 音效
│   └── fonts/            # 字体
├── docs/                 # 项目文档
├── mario_level_1.py      # 入口文件
└── requirements.txt      # 依赖列表
```

## 开发进度

- [x] 基础框架搭建
- [x] 玩家系统实现
- [x] 关卡系统实现
- [x] 敌人系统实现
- [x] 道具系统实现
- [x] 音效系统实现
- [ ] 多关卡支持
- [ ] 存档功能

## 参考资料

- [Pygame官方文档](https://www.pygame.org/docs/)

## 许可证

本项目仅供学习使用。

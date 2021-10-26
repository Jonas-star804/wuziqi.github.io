'''基本设置'''

from graphics import *


class MapConfig(object):

    def __init__(self):
        # 棋盘大小
        self.maps = [[0 for i in range(16)] for j in range(16)]

        # 四个主方向变量和四个斜方向变量
        self.dx = [1, 1, 0, -1, -1, -1, 0, 1]
        self.dy = [0, 1, 1, 1, 0, -1, -1, -1]

        # 先手
        self.run_first = 1
        # 轮换
        self.run_turn = 1
        # ai下棋
        self.ai = 1
        # 玩家下棋
        self.player = 2
        # 对局结束
        self.END = False
        # 重开
        self.RESTART_FLAG = False
        # 离开
        self.QUIT_FLAG = False
        # 保存棋子
        self.pool = []


class TreeConfig(object):

    def __init__(self):
        # 设置博弈树剪枝阈值
        self.L1_max = -100000
        self.L2_min = 100000


class TextConfig(object):

    def __init__(self):
        self.ai_init()
        self.player_init()
        self.notice_board()
        self.quit_board()
        self.restart_board()

    def ai_init(self):
        # Point(x,y)-->以指定坐标的值(x, y)构造一点
        # Text(anchorPoint, string)-->以anchorPoint点的位置为中心，构建了一个内容为string的文本对象
        # AI先手
        self.ai_first = Text(Point(500, 100), '')
        # AI上一步的落子点
        self.ai_last = Text(Point(500, 330), "")

    def player_init(self):
        # 玩家先手
        self.player_first = Text(Point(500, 140), '')
        # 玩家上一步的落子点
        self.player_last = Text(Point(500, 370), '')

    def notice_board(self):
        # 提示轮到谁落子
        self.notice = Text(Point(500, 290), "")
        # 设置提示按钮的颜色
        self.notice.setFill('red')

    def quit_board(self):
        # 退出按钮
        self.QUIT = Text(Point(500, 20), "退出")
        # 退出按钮的颜色
        self.QUIT.setFill('red')

    def restart_board(self):
        # 重开按钮
        self.RESTART = Text(Point(500, 60), "重玩")
        # 设置重开按钮的颜色
        self.RESTART.setFill('red')

'''绘制棋盘'''

from graphics import *
from 六子棋博弈.config import MapConfig, TextConfig


# 画棋盘
class DrawWin(object):

    def __init__(self):
        self.mc = MapConfig()
        self.tc = TextConfig()
        # 设置棋盘背景颜色
        self.win.setBackground('pink')
        self.draw_line(451)
        self.draw_button()
        self.draw_info()
        self.init()
        # self.win.getMouse()

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, graph):
        self.__win = graph

    def init(self):
        # 数据初始化，把棋盘上的棋子和提示清空
        self.mc.END = False
        self.mc.run_turn = 1
        self.mc.run_first = 1
        self.mc.RESTART_FLAG = False
        self.mc.QUIT_FLAG = False

        # 遍历棋盘，若是某个位置不为0，就全部置零
        for i in range(16):
            for j in range(16):
                if (self.mc.maps[i][j] != 0):
                    self.mc.maps[i][j] = 0

        # 保存已画棋子
        for i in range(len(self.mc.pool)):
            # undraw()-->从窗口中删除该对象。如该对象没有在窗口中画出将会报错。
            self.mc.pool[-1].undraw()
            self.mc.pool.pop(-1)

        # AI先手
        self.tc.ai_first.setText("AI 先手")
        # 玩家先手
        self.tc.player_first.setText("玩家先手")
        # 提示按钮
        self.tc.notice.setText("")
        # AI最后棋子落点
        self.tc.ai_last.setText("")
        # 玩家最后棋子落点
        self.tc.player_last.setText("")

    def draw_line(self, length):
        '''绘制棋盘线'''
        # Line(point1, point2)-->构造一个从点point1到点point2的线段
        # 画竖线
        for i in range(0, length, 30):
            line = Line(Point(i, 0), Point(i, 450))
            line.draw(self.win)
        # 画横线
        for j in range(0, length, 30):
            line = Line(Point(0, j), Point(450, j))
            line.draw(self.win)

    def draw_button(self):
        '''绘制按钮'''
        Rectangle(Point(460, 5), Point(540, 35)).draw(self.win)
        Rectangle(Point(460, 45), Point(540, 75)).draw(self.win)
        Rectangle(Point(460, 85), Point(540, 115)).draw(self.win)
        Rectangle(Point(460, 125), Point(540, 155)).draw(self.win)
        Rectangle(Point(452, 275), Point(548, 305)).draw(self.win)
        Rectangle(Point(452, 307), Point(548, 395)).draw(self.win)

    def draw_info(self):
        '''绘制信息'''
        self.tc.ai_first.draw(self.win)
        self.tc.player_first.draw(self.win)
        self.tc.notice.draw(self.win)
        self.tc.ai_last.draw(self.win)
        self.tc.player_last.draw(self.win)
        self.tc.QUIT.draw(self.win)
        self.tc.RESTART.draw(self.win)


if __name__ == '__main__':
    dw = DrawWin()



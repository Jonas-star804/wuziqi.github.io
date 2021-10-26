'''博弈树策略'''

from graphics import *
from 六子棋博弈.rules import BasicRule
from 六子棋博弈.config import MapConfig, TextConfig
from 六子棋博弈.evaluate import Evaluate
from 六子棋博弈.draw_map import DrawWin

class Strategy(object):

    def __init__(self):
        self.mc = MapConfig()
        self.tc = TextConfig()
        self.dw = DrawWin()
        self.br = BasicRule()
        self.el = Evaluate()

    def player_play(self):
        '''玩家下棋'''
        # 获取指令
        p = self.dw.win.getMouse()
        # 重开或退出
        if self.br.Restart(p) or self.br.Quit(p):
            return
        # 返回x和y
        x = round(p.getX() / 30)
        y = round(p.getY() / 30)
        if self.br.if_can_down(x, y):
            self.go(x, y)
        else:
            self.player_play()

    def ai_layer1(self):
        '''博弈树第一层'''
        self.L1_max = -100000
        if (self.br.maps[8][8] == 0 and self.mc.run_first == self.mc.ai):
            return self.go(8, 8)
        pointi = -1
        pointj = -1

        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
                if not self.br.if_can_down(x, y):
                    continue
                # AI落子
                self.mc.maps[x][y] = self.mc.ai
                # 评估分数
                tempp = self.el.gain_score(x, y)
                if (tempp == 0):
                    self.mc.maps[x][y] = 0
                    continue
                if (tempp == 10000):
                    return self.go(x, y)

                # 获得第二层博弈树的局势分数
                tempp = self.ai_layer2()
                self.mc.maps[x][y] = 0
                if (tempp > self.L1_max):  # 取极大
                    L1_max = tempp
                    pointi = x
                    pointj = y

        self.go(pointi, pointj)


    def ai_layer2(self):
        '''博弈树第二层'''
        self.L2_min = 100000
        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
                # 如果不能落子，就继续
                if not self.br.if_can_down(x, y):
                    continue
                self.mc.maps[x][y] = self.mc.player
                # 评估分数
                tempp = self.el.gain_score(x, y)
                if tempp == 0:
                    self.mc.maps[x][y] = 0
                    continue
                if tempp == 10000:
                    self.mc.maps[x][y] = 0
                    return -10000
                # 获得第三层博弈树的局势分数
                tempp = self.ai_layer3(tempp)
                if (tempp < self.L1_max):  # L1层剪枝
                    self.mc.maps[x][y] = 0
                    return -10000
                self.mc.maps[x][y] = 0
                if (tempp < self.L2_min):  # 取极小
                    self.L2_min = tempp

    def ai_layer3(self, temp2):
        '''博弈树第三层'''
        self.pointp = -100000
        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15, 0]:
                if not self.br.if_can_down(x, y):
                    continue
                self.mc.maps[x][y] = self.mc.ai
                # 评估分数
                tempp = self.el.gain_score(x, y)
                if tempp == 0:
                    self.mc.maps[x][y] = 0
                    continue
                if tempp == 10000:
                    self.mc.maps[x][y] = 0
                    return 10000

                if (tempp - temp2 * 2 > self.L2_min):  # L2层剪枝
                    self.mc.maps[x][y] = 0
                    return 10000
                self.mc.maps[x][y] = 0
                if (tempp - temp2 * 2 > self.pointp):  # 取极大
                    self.pointp = tempp - temp2 * 2

    def go(self, x, y):
        '''落下一子并且判断游戏是否结束'''

        # Circle(centerPoint,radius)-->根据给定圆心和半径构建圆
        c = Circle(Point(x * 30, y * 30), 13)
        # AI turn
        if self.mc.run_turn == self.mc.ai:
            self.mc.maps[x][y] = self.mc.ai
            # AI上一步的落子
            self.tc.ai_last.setText("AI 落子:\n(x:y)=(" + str(x) + ":" + str(y) + ")")
            if self.mc.run_first == self.mc.ai:
                c.setFill('black')
            else:
                c.setFill('white')
        # Player turn
        else:
            self.mc.maps[x][y] = self.mc.player
            # 玩家上一步的落子
            self.tc.player_last.setText("玩家落子:\n(x:y)=(" + str(x) + ":" + str(y) + ")")
            if (self.mc.run_first == self.mc.ai):
                c.setFill('white')
            else:
                c.setFill('black')
        c.draw(self.dw.win)
        self.mc.pool.append(c)
        # 如果游戏结束
        if self.br.game_over(x, y):
            # AI turn
            if self.mc.run_turn == self.mc.ai:
                self.tc.notice.setText("AI 赢!\n点击重玩")
            # Player turn
            else:
                self.tc.notice.setText("玩家赢!\n点击重玩")








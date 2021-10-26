'''基本规则'''

from 六子棋博弈.config import MapConfig, TextConfig
from 六子棋博弈.draw_map import DrawWin
import time

class BasicRule(object):

    def __init__(self):
        self.mc = MapConfig()
        self.tc = TextConfig()
        self.dw = DrawWin()
        self.maps = self.mc.maps
        self.dx = self.mc.dx
        self.dy = self.mc.dy

    def if_inboard(self, x, y):
        '''判断该点位是否在棋盘中'''
        if (x>=0 and y>=0 and x<=15 and y<=15):
            return True
        else:
            return False

    def if_can_down(self, x, y):
        '''判断该点位是否可以落子'''
        if (self.if_inboard(x, y) and self.maps[x][y]==0):
            return True
        else:
            return False

    def if_same_role(self, x, y, val):
        '''判断某落子是否是同方'''
        if (self.if_inboard(x, y) and self.maps[x][y]==val):
            return True
        else:
            return False

    def count_inline_num(self, x, y, d):
        '''统计给定的方向d（共八个方向）上，和该点同色棋子的个数'''
        xx = x + self.dx[d]
        yy = y + self.dy[d]
        current = self.maps[x][y]
        num = 0
        if current==0:
            return 0
        while self.if_same_role(xx, yy, current):
            num += 1
            xx += self.dx[d]
            yy += self.dy[d]
        return num

    def samepoint_num(self, x, y, d, value, point, same_point):
        ''' 统计在某一方向上，是己方的点的个数'''
        # 正向
        if value == 1:
            while self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, point):
                value += 1
                same_point += 1
        # 反向
        elif value == -1:
            while self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, point):
                value -= 1
                same_point += 1

        return same_point, value

    def live_four(self, x, y):
        '''活四的个数'''
        current = self.maps[x][y]
        count = 0

        # 活4(4个方向，不区分正负)
        for d in range(4):
            same_point = 1
            # 正向
            same_point, value = self.samepoint_num(x, y, d, 1, current, same_point)
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            # 反向
            same_point, value = self.samepoint_num(x, y, d, -1, current, same_point)
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            if same_point == 4:
                count += 1

        return count

    def live_three(self, x, y):
        '''该点四个方向里活三，以及八个方向里断三的个数'''

        current = self.maps[x][y]
        count = 0
        # 活3(4个方向，不区分正负)
        for d in range(4):
            same_point = 1
            # 正向落子
            same_point, value = self.samepoint_num(x, y, d, 1, current, same_point)
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            if not self.if_can_down(x + self.dx[d] * (value + 1), y + self.dy[d] * (value + 1)):
                continue
            # 反向落子
            same_point, value = self.samepoint_num(x, y, d, -1, current, same_point)
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            if not self.if_can_down(x + self.dx[d] * (value - 1), y + self.dy[d] * (value - 1)):
                continue
            if same_point == 3:
                count += 1

        # 断3(8个方向，区分正负)
        for d in range(8):
            same_point = 0
            flag = True
            value = 1
            while (self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, current) or flag):
                if not self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, current):
                    if (flag and self.if_inboard(x + self.dx[d] * value, y + self.dy[d] * value)
                            and self.maps[x + self.dx[d] * value][y + self.dy[d] * value] != 0):
                        same_point -= 10
                    flag = False
                same_point += 1
                value += 1
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            if (self.if_inboard(x + self.dx[d] * (value - 1), y + self.dy[d] * (value - 1))
                    and self.maps[x + self.dx[d] * (value - 1)][y + self.dy[d] * (value - 1)] == 0):
                continue
            # 反向落子
            same_point, value = self.samepoint_num(x, y, d, -1, current, same_point)
            if not self.if_can_down(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            if same_point == 3:
                count += 1

        return count

    def go_four(self, x, y):
        '''该点八个方向里(v区分正负)，冲四局势的个数'''
        current = self.maps[x][y]
        count = 0
        for d in range(8):
            same_point = 0
            flag = True
            value = 1
            while self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, current) or flag:
                if not self.if_same_role(x + self.dx[d] * value, y + self.dy[d] * value, current):
                    if (flag and self.if_inboard(x + self.dx[d] * value, y + self.dy[d] * value)
                            and self.maps[x + self.dx[d] * value][y + self.dy[d] * value] != 0):
                        same_point -= 10
                    flag = False
                same_point += 1
                value += 1
            value -= 1
            if not self.if_inboard(x + self.dx[d] * value, y + self.dy[d] * value):
                continue
            # 反向
            same_point, value = self.samepoint_num(x, y, d, -1, current, same_point)
            if same_point == 4:
                count += 1

        return count - self.live_four(x, y) * 2

    def tie_line(self, x, y):
        '''该点在四个方向里，是否有四子或以上连线'''
        flag = False  # 是否连线
        for d in range(4):
            # 如果有连线且且连线大于4
            if ((self.count_inline_num(x, y, d) + self.count_inline_num(x, y, d + 4)) > 4):
                flag = True
        return flag


    def game_over(self, x, y):
        '''游戏是否结束，如果有五子连线'''
        for d in range(4):
            # 如果给定方向上有4子，就判赢
            if ((self.count_inline_num(x, y, d) +self.count_inline_num(x, y, d + 4)) >= 4):
                self.mc.END = True
                return True
        return False

    def Restart(self, p):
        '''是否重新开始游戏'''
        x = p.getX()
        y = p.getY()
        if ((abs(500 - x) < 40) and (abs(60 - y) < 15)):
            self.dw.init()
            self.RESTART_FLAG = True
            self.tc.notice.setText("重新开始")
            time.sleep(1)
            return True
        else:
            return False

    def Quit(self, p):
        '''是否退出游戏'''
        x = p.getX()
        y = p.getY()
        if ((abs(500 - x) < 40) and (abs(20 - y) < 15)):  # quit
            self.dw.init()
            self.QUIT_FLAG = True
            self.END = True
            self.tc.notice.setText("退出")
            time.sleep(1)
            return True
        else:
            return False

    def who_start(self, p):
        '''选择先后手'''
        x = p.getX()
        y = p.getY()
        # AI先手
        if ((abs(500 - float(x)) < 40) and (abs(100 - float(y)) < 15)):
            self.run_turn = 1
            self.run_first = 1
            self.tc.ai_first.setText("AI 执黑")
            self.tc.player_first.setText("玩家执白")
            return True

        # 玩家先手
        elif ((abs(500 - x) < 40) and (abs(140 - y) < 15)):
            self.run_turn = 2
            self.run_first = 2
            self.tc.ai_first.setText("AI 执白")
            self.tc.player_first.setText("玩家执黑")
            return True
        else:
            return False










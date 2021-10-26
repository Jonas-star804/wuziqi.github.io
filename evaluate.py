'''对落子的局势估分'''

from 六子棋博弈.rules import BasicRule
from 六子棋博弈.config import MapConfig

class Evaluate(object):

    def __init__(self):
        self.br = BasicRule()
        self.mc = MapConfig()


    def gain_score(self, x, y):
        # 游戏结束
        if self.br.game_over(x, y):
            self.END=False
            return 10000
        # 局势分数等于活3*1000
        score = self.br.live_three(x, y) * 1000
        # 八个方向
        for d in range(8):
            if (self.br.if_inboard(x+self.br.dx[d], y+self.br.dy[d]) and self.mc.maps[x+self.br.dx[d]][y+self.br.dy[d]]!=0):
                score += 1
        return score



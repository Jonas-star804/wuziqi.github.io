'''主程序'''

from graphics import *
from 六子棋博弈.strategy import Strategy
from 六子棋博弈.draw_map import DrawWin
from 六子棋博弈.config import MapConfig, TextConfig
from 六子棋博弈.rules import BasicRule


if __name__=='__main__':
    # 地图设置类
    mc = MapConfig()
    # 文本框设置类
    tc = TextConfig()
    # 地图绘制类
    dw = DrawWin()
    dw.win = GraphWin("五子棋",550,451)
    # 基本规则类
    br = BasicRule()
    # 策略类
    st = Strategy()

    # 初始化棋盘
    dw.init()
    # setText(string)-->设置文本对象的内容
    # 提示框
    tc.notice.setText("请选择先手")
    # 获取指令
    p=dw.win.getMouse()
    # 没选择先后手并且不退出时，重复获取玩家指令
    while not br.who_start(p) and not br.Quit(p):
        p=dw.win.getMouse()
    while not mc.END:
        mc.RESTART_FLAG=False
        # AI turn
        if mc.run_turn==mc.ai:
            tc.notice.setText("AI 正在下棋...")
            st.ai_layer1()
        # Player turn
        else:
            tc.notice.setText("请玩家下棋...")
            st.player_play()
        mc.run_turn = mc.player

        # 重开
        if mc.RESTART_FLAG:
            tc.notice.setText("请选择先手")
            p=dw.win.getMouse()
            while not br.who_start(p) and not br.Quit(p):
                p=dw.win.getMouse()
        # 结束但不退出
        elif not mc.QUIT_FLAG and mc.END:
            p=dw.win.getMouse()
            while(not br.Restart(p) and not br.Quit(p)):
                p=dw.win.getMouse()
            if mc.RESTART_FLAG:
                tc.notice.setText("请选择先手")
                p=dw.win.getMouse()
                while(not br.who_start(p) and not br.Quit(p)):
                    p=dw.win.getMouse()
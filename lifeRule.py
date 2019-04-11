#-*-coding:utf-8-*-

from lifeMap import Cell

"""
元细胞自动机
规则
    三个活细胞则生
    两个活细胞不变
    其余皆死
"""

def game_cycle(gameMap):
        """进行一次游戏循环
        gameMap: class lifeMap
        gameMap.map: list,[list]. 0,1
        """
        #依规则记录下次要更新的细胞
        shadow = []
        for i in range(len(gameMap.map)):
            for j in range(len(gameMap.map[i])):
                ngbcnt = gameMap.get_neighbor_count(i, j)
                if ngbcnt == 3:
                    shadow.append([i,j,Cell.state['live']])
                elif ngbcnt != 2:
                    shadow.append([i,j,Cell.state['dead']])
        #更新细胞状态
        for list in shadow:
            gameMap.set(list[0], list[1], list[2])
 

        
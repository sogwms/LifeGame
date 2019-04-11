# -*- coding: utf-8 -*-

import random


class Cell():
    state = {'live':1, 'dead':0}

class Map():

    map = []
    xMax = 0
    yMax = 0

    def __init__(self, xMax=60, yMax=60):
        """地图初始化"""
        Map.xMax = xMax
        Map.yMax = yMax        

        for i in range(Map.xMax):
            temp = []
            for j in range(Map.yMax):             
                temp.append(Cell.state['dead'])
            Map.map.append(temp)
    
    def reset(self):
        """重置地图为无活细胞状态"""
        for i in range(Map.xMax):
            for j in range(Map.yMax):
                Map.map[i][j] = Cell.state['dead']

    def random(self, ratio):
        """重置地图并按ratio随机填充活细胞"""
        self.reset()

        totalpixel = Map.xMax * Map.yMax        
        for i in range(int(totalpixel*ratio)):
            index = random.randint(0, totalpixel-1)
            Map.map[index//Map.xMax][index%Map.yMax] = Cell.state['live']
            

    def get_neighbor_count(self, x, y):
        """获取指定方格周围活细胞数量"""
        count = 0
        for i in range(9):        
            if (self.get(x-1+(i//3), y-1+(i%3)) == Cell.state['live']):
                count += 1
        if self.get(x, y) == Cell.state['live']:
            count -= 1
        return count

    def set(self, x, y, val):
        """设置指定方格细胞状态"""
        if (x < Map.xMax) and (y < Map.yMax):
            if (val!=Cell.state['dead']) and (val!=Cell.state['live']):
                val = Cell.state['dead']
            Map.map[x][y] = val
    
    def get(self, x, y):
        """获取指定方格细胞状态"""
        if (x < Map.xMax) and (y < Map.yMax):
            return Map.map[x][y]
        
    

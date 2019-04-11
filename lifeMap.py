# -*- coding: utf-8 -*-

import random

class Cell():
    state = {'live':1, 'dead':0}

class RangeError(Exception):
    def __init__(self, error):
        self.error = error
    def __str__(self, *args, **kwargs):
        return self.error

class Map:
    """
    地图坐标原点为左上角, 左上角->右上角 为 x 轴方向, 左上角->左下角为 y 轴方向
    """

    @staticmethod
    def check_integer(n, min=None, max=None):
        if not isinstance(n, int) or\
            (min and not isinstance(min, int)) or\
            (max and not isinstance(max, int)):
            raise TypeError("Type. error: int")
        if min and n < min:
            raise RangeError("Range error: min")
        if max and n > max:
            raise RangeError("Range error: max")

    def __init__(self, xTotal=60, yTotal=60):
        """地图初始化"""
        Map.check_integer(xTotal, 1)
        Map.check_integer(yTotal, 1)
        self.xTotal = xTotal
        self.yTotal = yTotal      

        #[note]优先使用列表解析构建列表
        #[note] _ 为了消除警告
        self.map = [[Cell.state['dead'] for _ in range(yTotal)] for _ in range(xTotal)]
    
    def reset(self):
        """重置地图为无活细胞状态"""
        for i in range(self.xTotal):
            for j in range(self.yTotal):
                self.map[i][j] = Cell.state['dead']

    def random(self, ratio):
        """重置地图并按ratio随机填充活细胞.
        possibility is float, [0,1]
        """
        self.reset()

        total = self.xTotal * self.yTotal      
        for _ in range(int(total*ratio)):
            index = random.randint(0, total-1)
            self.map[index//self.xTotal][index%self.yTotal] = Cell.state['live']
            

    def get_neighbor_count(self, x, y):
        """获取指定方格周围活细胞数量"""
        Map.check_integer(x, 0, self.xTotal)
        Map.check_integer(y, 0, self.yTotal)

        count = 0
        for i in range(9):        
            if (self.__get(x-1+(i//3), y-1+(i%3)) == Cell.state['live']):
                count += 1
        if self.__get(x, y) == Cell.state['live']:
            count -= 1
        return count

    def set(self, x, y, celstate):
        """设置指定方格细胞状态"""
        Map.check_integer(x, 0, self.xTotal)
        Map.check_integer(y, 0, self.yTotal)
        if (celstate!=Cell.state['dead']) and (celstate!=Cell.state['live']):
            raise RangeError('Range error: celstate is not valid')

        self.map[x][y] = celstate
    
    def __get(self, x, y):
        """获取指定方格细胞状态"""
        if (x < 0 or x > self.xTotal-1) or (y < 0 or y > self.yTotal-1):
            return Cell.state['dead']
        else:
            return self.map[x][y]
        
    def print_map(self, cell_mask=['0', '1'], sep=' '):
        """
        cell_mask list == 2
        sep str
        """
        if not isinstance(cell_mask, list) or not len(cell_mask) >= 2:
            raise TypeError("Type error: cell_mask")
        if not isinstance(sep, str):
            raise TypeError("Type error: sep")
        
        for x in range(self.xTotal):
            print(sep.join(map(lambda x: cell_mask[x], self.map[x])))


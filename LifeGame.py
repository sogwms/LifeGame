#!/usr/bin/python3
# -*- coding: utf-8 -*-

import lifeRule
import lifeMap
import lifeGui
import time


class LifeGame():

    def __init__(self, xWidth=60, yWidth=60, cellWidth=10):
        """
        xWidth, yWidth: 格子图宽度和长度（以格子数计）
        cellWidth: 格子像素宽
        """
        self.w = lifeGui.TkGui(cellWidth)
        self.map = lifeMap.Map(xWidth, yWidth)
        
    def run(self):
        self.animate()
        self.w.master.mainloop()

    def animate(self):
        self.w.drawboard(self.map.map)
        lifeRule.game_cycle(self.map)
        self.w.canvas.after(100, self.animate)

if __name__ == '__main__':
    game = LifeGame(80,80,10)
    game.map.random(0.1)
    game.run()
    

    
        
    
    

import tkinter
from tkinter.constants import *

class TkGui:

    color_dead = '#303030'
    color_live = '#00FFFF'
    colors=[color_dead, color_live,'orange','yellow','green','cyan','blue','pink']

    def __init__(self, cellwidth):
        self.cellwidth = cellwidth
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master, bg = TkGui.color_dead)
        self.canvas.pack()

    def drawboard(self, board, x=50, y=50):
        """
        board : 二维列表（[[],[]]）
        cellwidth: 格子大小（像素）
        x, y : 格子图距窗口边界的间隔
        """
        cvwidth = 2*x+len(board)*self.cellwidth
        cvheight = 2*y+len(board)*self.cellwidth
        self.canvas.config(width=cvwidth,height=cvheight)
        for i  in range(len(board)):
            for j in range(len(board[i])):
                index = board[i][j]
                color = TkGui.colors[index]
                cellx = x+i*self.cellwidth
                celly = y+j*self.cellwidth
                self.canvas.create_rectangle(cellx,celly,cellx+self.cellwidth,celly+self.cellwidth,
                    fill=color,outline="#505050")
        self.canvas.update()



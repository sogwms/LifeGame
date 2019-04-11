from tkinter import *
import threading
import random

class TkGui():

    color_dead = '#303030'
    color_live = '#00FFFF'
    colors=[color_dead, color_live,'orange','yellow','green','cyan','blue','pink']

    master = Tk()
    cv = None

    def __init__(self, backColor=color_dead):
        TkGui.cv = Canvas(TkGui.master, bg = backColor)
        TkGui.cv.pack()

    def drawboard(self, board, cellwidth=50, x=50, y=50, colors= colors,):
        width = 2*x+len(board)*cellwidth
        height = 2*y+len(board)*cellwidth
        TkGui.cv.config(width=width,height=height)
        for i  in range(len(board)):
            for j in range(len(board[i])):
                index = board[i][j]
                color = colors[index]
                cellx = x+i*cellwidth
                celly = y+j*cellwidth
                TkGui.cv.create_rectangle(cellx,celly,cellx+cellwidth,celly+cellwidth,
                    fill=color,outline="#505050")
        TkGui.cv.update()

def randomBoard():
    global wind
    board = []
    x = 16
    y = 16
    ratio = 0.1
    for i in range(x):
        templist = []
        for j in range(y):
            templist.append(0)
        board.append(templist)

    for i in range(int(x*y*ratio)):
        idx = random.randint(0, x*y-1)
        board[idx//x][idx%y] = 1

    wind.drawboard(board)
    tim = threading.Timer(0.1, randomBoard)
    tim.start()




if __name__ == '__main__':
   
    board=[[1,1,1,0],[0,1,1,0],[0,1,0,0],[1,0,0,0]]
    
    wind = TkGui()
    wind.drawboard(board, 50)
    randomBoard()
    wind.master.mainloop()

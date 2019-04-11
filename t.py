import tkinter
from tkinter.constants import *
import random

class TkGui():

    color_dead = '#303030'
    color_live = '#00FFFF'
    colors=[color_dead, color_live,'orange','yellow','green','cyan','blue','pink']


def drawboard( board, cellwidth=50, x=50, y=50):
        cvwidth = 2*x+len(board)*cellwidth
        cvheight = 2*y+len(board)*cellwidth
        canvas.config(width=cvwidth,height=cvheight)
        for i  in range(len(board)):
            for j in range(len(board[i])):
                index = board[i][j]
                color = TkGui.colors[index]
                cellx = x+i*cellwidth
                celly = y+j*cellwidth
                canvas.create_rectangle(cellx,celly,cellx+cellwidth,celly+cellwidth,
                    fill=color,outline="#505050")
        canvas.update()

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
    
    drawboard(board)
    canvas.after(100, randomBoard)


tk = tkinter.Tk()
canvas = tkinter.Canvas(tk)
canvas.pack()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
randomBoard()
tk.mainloop()
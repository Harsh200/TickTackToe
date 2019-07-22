from tkinter import *

def drawShape(x,y):
    global cross
    margin=20
    if cross:
        gameboard.create_line(x+margin,y+margin,x+ (width/3)-margin,y+ (height/3)-margin,fill="Blue",width=10)
        gameboard.create_line(x+margin, y + (height / 3)-margin, x + (width / 3)-margin, y+margin,fill="Blue",width=10)
        cross=False
    else:
        gameboard.create_oval(x+margin,y+margin,x+(width/3)-margin,y+(height/3)-margin,width=10,outline="Red")
        cross=True

def play(event):
    secondrow=height/3
    thirdrow=secondrow*2
    secondcolumn=width/3
    thirdcolumn=secondcolumn*2
    offsetx=thirdcolumn
    offsety=thirdrow
    if event.y<secondrow:
        offsety=0
    elif event.y<thirdrow:
        offsety=secondrow

    if event.x<secondcolumn:
        offsetx=0
    elif event.x<thirdcolumn:
        offsetx=secondcolumn

    drawShape(offsetx,offsety)



window=Tk()
cross=True
width=500
height=500
gameboard=Canvas(window,width=width,height=height)
gameboard.create_line(0,height/3,width,height/3)
gameboard.create_line(0,(height/3)*2,width,(height/3)*2)
gameboard.create_line(width/3,0,width/3,height)
gameboard.create_line((width/3)*2,0,(width/3)*2,height)
gameboard.pack()
gameboard.bind("<Button-1>",play)




window.mainloop()

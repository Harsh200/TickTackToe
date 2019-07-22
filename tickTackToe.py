from tkinter import *
window=Tk()
width=500
height=500
gameboard=Canvas(window,width=width,height=height)
gameboard.create_line(0,height/3,width,height/3)
gameboard.create_line(0,(height/3)*2,width,(height/3)*2)
gameboard.pack()




window.mainloop()
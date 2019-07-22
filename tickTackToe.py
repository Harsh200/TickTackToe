from tkinter import *
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




window.mainloop()
#//---LIBRARIES---//
import tkinter

#//---GLOBAL VARIABILES---//

#//---GUI SETUP---//
canvas = tkinter.Canvas()
canvas.pack()

#//---MAIN---//
#creating the picture from rectangles
canvas.create_rectangle( 50, 50, 150, 100, fill='blue', outline='green', width=3)
canvas.create_rectangle(50,100,150,150, fill='red', outline='green', width=3)
canvas.create_rectangle(150,50,250,100, fill='yellow', outline='green', width=3)
canvas.create_rectangle(95,65,205,120, fill='brown', outline='green', width=3)


#running the GUI in loop so it wont close after it finishes the picture
canvas.mainloop()

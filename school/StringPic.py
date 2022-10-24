
#//---LIBRARIES---//
import tkinter

#//---GLOBAL VARIABILES---//
#nothing here ._.

#//---GUI SETUP---//
canvas = tkinter.Canvas()
canvas.pack()

#//---MAIN---//
#creating the picture from random lines
canvas.create_line(-120, 10, 400, 150, fill='blue', width=4)
canvas.create_line(-120, 15, 400, 155, fill='yellow', width=4)
canvas.create_line(-120, 20, 400, 160, fill='green', width=4)
canvas.create_line(-120, 25, 400, 165,  fill='gray', width=2)
canvas.create_line(-120, 30, 400, 170,  fill='purple', width=4)
canvas.create_line(-120, 35, 400, 175, fill='gray', width=2)
canvas.create_line(-120, 40, 400, 180, fill='green', width=4)
canvas.create_line(-120, 45, 400, 185, fill='yellow', width=4)
canvas.create_line(-120, 50, 400, 190, fill='blue', width=4)

#running the GUI in loop so it wont close after it finishes the picture
canvas.mainloop()

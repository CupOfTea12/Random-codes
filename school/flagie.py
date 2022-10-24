#//---LIBRARIES---//
import tkinter

#//---GLOBAL VARIABILES---//
#...

#//---GUI SETUP---//
canvas = tkinter.Canvas()
canvas.pack()

#//---MAIN---//
#creating the flag
#base of the flag
canvas.create_rectangle( 50, 50, 150, 120, fill='white', outline='black', width=2)
canvas.create_rectangle(50, 50, 80, 80, fill='blue', outline='black', width=1)
#stripes
canvas.create_rectangle(150, 60, 80, 55, fill='blue', outline='black', width=1)
canvas.create_rectangle(150, 80, 80, 75, fill='blue', outline='black', width=1)
canvas.create_rectangle(150, 85, 50, 90, fill='blue', outline='black', width=1)
canvas.create_rectangle(150, 95, 50, 100, fill='blue', outline='black', width=1)
canvas.create_rectangle(150, 105, 50, 110, fill='blue', outline='black', width=1)


#running the GUI in loop so it wont close after it finishes the picture
canvas.mainloop()

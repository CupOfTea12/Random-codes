#//---LIBRARIES---//
import tkinter
from tkinter import *
import random

#//---GLOBAL-VARIABILES---//
gui = Tk() #object
gui.geometry('650x850') #size
gui.configure(bg='black') #bg color
canvas = Canvas(gui, width=650, height=850, bg='black')


#//---OBJECTS----//
#stars
photo_image1 =PhotoImage(file='hviezda0.png')
photo_image2 =PhotoImage(file='hviezda1.png')
photo_image3 =PhotoImage(file='hviezda2.png')

#cosmonauts
photo_image4=PhotoImage(file='kozmo0.png')
photo_image5=PhotoImage(file='kozmo1.png')
photo_image6=PhotoImage(file='kozmo2.png')

#earth
photo_image7=PhotoImage(file='Zem.png')

#//---MAIN---//
#spawning the stars
for x in range(250):
    # axis
    rangeX = random.randrange(0, 650)
    rangeY = random.randrange(0, 850)
    canvas.create_image(rangeX, rangeY, anchor=NW, image=photo_image1)
    canvas.create_image(rangeX, rangeY, anchor=NW, image=photo_image2)
    canvas.create_image(rangeX, rangeY, anchor=NW, image=photo_image3)

#spawning cosmonauts
for y in range(random.randrange(1,8)):
    rangeCosmoX=random.randrange(0,650)
    rangeCosmoY=random.randrange(0,850)
    canvas.create_image(rangeCosmoX,rangeCosmoY,  image=photo_image4)
    canvas.create_image(rangeCosmoX, rangeCosmoY, image=photo_image5)
    canvas.create_image(rangeCosmoX, rangeCosmoY, image=photo_image6)

#spawning the earth on static place
canvas.create_image(80, 800, image=photo_image7)

def move():
    canvas.move(photo_image4, 110,795)
    canvas.move(photo_image5, 110, 795)
    canvas.move(photo_image6, 110, 795)

#binding the onclick to images
canvas.tag_bind(photo_image4, '<ButtonPress-1>', move())
canvas.tag_bind(photo_image5, '<ButtonPress-1>', move())
canvas.tag_bind(photo_image6, '<ButtonPress-1>', move())



canvas.pack()


gui.mainloop()
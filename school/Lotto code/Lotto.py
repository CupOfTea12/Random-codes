"""
Code by Rebeca Martinakova
II.IT 2021
LOTO
Used libraries: import random, import time
logic: basic
"""

#//---LIBRARIES---//
from random import *
import time

#//---DEFINES---//

  #nothing to show here....

#//---GLOBAL-VARIABILES---//
#LISTS
randomlist=[]

#//---FUNCTIONS---//
#welcome messages
print("------------------")
print("WELCOME TO LOTTO")
#nice 3 second delay
time.sleep(3)
#our main function
for i in range (0,5):
    randomlist.append(randint(1,35))

#just some useless printing for style
print("------------------")
print("Generating your five lucky numbers...")
time.sleep(3)
print("------------------")
print("Printing list of 5 random lucky numbers: ")
print(randomlist)

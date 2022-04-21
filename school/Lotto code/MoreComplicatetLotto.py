"""
Code by Rebeca Martinakova
II.IT 2021
LOTO-2
Used libraries: import random, import time
logic: basic
"""

#//---LIBRARIES---//
from random import *
import time

#//---DEFINES---//

 #nothing to show here....

#//---GLOBAL-VARIABILES---//
LuckyList=[]
RandomList=[]

#//---FUNCTIONS---//
print("------------------")
print("WELCOME TO LOTTO")
print("------------------")

while True:
    try:
     print("Please enter your five lucky numbers in range 1-35:")
     print("------------------")

     num1=int(input("1. number:"))
     assert 0 < num1 < 36
     num2=int(input("2. number:"))
     assert 0 < num2 < 36
     num3=int(input("3. number:"))
     assert 0< num3 < 36
     num4=int(input("4. number:"))
     assert 0 < num4 < 36
     num5=int(input("5. number:"))
     assert 0 < num5 < 36

    #gonna check the values ofcourse :)))
    except ValueError:
        print("You must input numbers!!!")
        continue
    #also gonna check the range of input
    except AssertionError:
        print("Please enter an integer between 1 and 35")
        continue
    else:
        break

time.sleep(3)
#adding our numbers to luckylist :3333
LuckyList.extend([num1, num2, num3, num4, num5])

print("------------------")
print("Your numbers have been stored successfuly!")
print("Your numbers are: ",LuckyList)
print("------------------")
time.sleep(3)
print("Now watch carefuly...im gonna print 5 lotto numbers :3")
for i in range (0,5):
    RandomList.append(randint(0,36))
time.sleep(3)
print("Lotto numbers are: ", RandomList)
time.sleep(3)
print("---------")
print("Same numbers in two lists: ", set(LuckyList).intersection(RandomList))

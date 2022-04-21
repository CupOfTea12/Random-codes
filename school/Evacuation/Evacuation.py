"""
Code by Rebeca Martinakova
II.IT 2021
EVACUATION
Used libraries: import itertools, import time
logic: basic
"""
#//---LIBRARIES---//
import itertools
import time

#//---DEFINES---//

 #nothing to show here....

#//---GLOBAL-VARIABILES---//
carrying_Capacity= 1000
#LISTS
Planet_Alpha=[60,135,84,203,78,94,321,59,163] #weight of aliens from Planet Alpha
Planet_Beta=[151,37,278,114,69] #weight of aliens from Planet Beta
evacuation_list=[] #list for the heavy guys

#//---FUNCTIONS---//

#//---LIST-SORTING---//
#okay... i will explain what does the ,,reverse=True'' mean. It sorts the list from the largest item to the smallest one (in our case number)
Planet_Alpha.sort(reverse=True)
Planet_Beta.sort(reverse=True)
#okay...lets see how the lists looks like now
print("----EVACUATION-PLAN---")
time.sleep(2)
print("WEIGHT OF ALIENS FROM PLANET ALPHA: ", Planet_Alpha)
time.sleep(1)
print("WEIGHT OF ALIENS FROM PLANET BETA: ", Planet_Beta)
#see? now we know that lists are sorted properly and we can continue

#//---SORTING-TO-THE-EVACUATION-PLAN---//
#okay...i will do this by the simple way.. we are gonna move multiple elements from lists to the evacuation plan
evacuation_list = Planet_Alpha[4:] + evacuation_list
Planet_Alpha = Planet_Alpha[:4]

#print(evacuation_list)
#print(Planet_Alpha)

if sum(Planet_Alpha)==1000:
    print("The ship is full!!!")
elif sum(Planet_Alpha)>1000:
    print("Too much aliens!!!")
else:
    print("The ship is not full, ", 1000-sum(Planet_Alpha),"kg of space remaining.")


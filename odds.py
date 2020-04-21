import datetime
import os
import random
from time import sleep

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,
 33,35,37,39,41,43,45,47,49,51,53,55,57,59]

def my_function():
    right_this_minute = datetime.datetime.today().minute
    # print(right_this_minute)
    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print ("Not an odd minute")

for i in range(6):
    random_number = random.randrange(15)
    sleep(random_number)
    my_function()
    print(i)



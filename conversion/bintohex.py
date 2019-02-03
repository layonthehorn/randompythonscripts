#!/usr/bin/env python

import sys

# layonthehorn
# Make this program work on both Python 2.x and Python 3.x
if (sys.version_info[0] == 3): raw_input = input

import math
import string

decnumber=raw_input("Please enter a number to be changed to binary. ")
decnumber=int(decnumber)
def dectobin(num):
    finalprint = ""
    default = [0,0,0,0]
    list =[]
    if num == 0:
        list = default
    else:
        while num > 0:


            remander = num%2
            list.append(remander)
            #print(remander)
            num = num //2
        list.reverse()
        while len(list) % 4 != 0:

            list.insert(0,0)

    for i in list:
        finalprint = finalprint + str(i)
    return finalprint

message = "The binary number for {0} is {1}."
number = dectobin(decnumber)
print(message.format(decnumber,number))


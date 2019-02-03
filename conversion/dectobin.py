#-------------------------------------------------------------------------------
# Name:        module for dectohex
# Purpose:
#
# Author:      layonthehorn
#
# Created:     20/10/2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def dectobin(num):
    """This program converts from decimal to binary"""
    finalprint = ""
    num = int(num)
    list =[]
    if num == 0:
        pass
    else:
        while num > 0:

            remander = num%2
            list.append(remander)
            #print(remander)
            num = num //2
        list.reverse()
    while len(list) % 4 != 0 or list == []:

        list.insert(0,0)

    for i in list:
        finalprint = finalprint + str(i)
    return finalprint

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      layonthehorn
#
# Created:     19/10/2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import dectobin


def bintodec(num):
    loop = 0
    finalan = 0
    list =[]
    power2 = 1
    if num == "0000":
        finalan = "0"
    else:
        for i in num:
            conum= int(i)
            list.append(conum)
        list.reverse()
        print(list)
        for i in list:
            print(i,power2,loop)

            print(power2)
            if i != 0 or loop !=0:
                finalan = finalan + power2
            power2 = power2 * 2
    return finalan


print(bintodec("0000"))

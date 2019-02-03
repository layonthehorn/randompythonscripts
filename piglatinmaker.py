#-------------------------------------------------------------------------------
# Name:        puncuation remover
# Purpose:
#
# Author:      thomas p dressel
#
# Created:     17/06/2017
# Copyright:   (c) catma 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def piglat(sen):
    pigsen=""
    eagle = sen
    for i in eagle:

        start = i[0]
        basew = i[1:]
        pigs =  basew + start + "ay "
        pigsen = pigsen + pigs
        #print(eagle)
    pigsen = pigsen.capitalize()
    pigsen = pigsen[:-1]
    pigsen = pigsen + "."
    return pigsen


def stripoff(senz):
    newsen=""
    for i in senz:
        if i == "," or i == "." or i == "'" or i == "?"or i == "!" or i == ";" or i == ":" or i == "(" or i == ")" or i == '"' or i == "=" or i == "+":
            newsen= newsen + ""

        else:
            newsen = newsen + i
    newsen = newsen.lower()
    #print(newlist)
    newlist=newsen.split()
    pigwordz= piglat(newlist)
    return pigwordz


word=input("enter a sentence.")
print("the corrupted sentence is:",stripoff(word))

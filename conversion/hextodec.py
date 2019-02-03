# layonthehorn

def bintodec(num):
    """This program will convert a binary number to decimal."""
    finalan = 0
    list =[]
    power2 = 1

    for i in num:
        conum= int(i)
        list.append(conum)
    list.reverse()
    for i in list:
        if i != 0:
            finalan = finalan + power2
        power2 = power2 * 2
    return finalan






def hextodec(num):
    """This program will convert  hexidecimal to decimal"""
    hex =""
    start = 0
    count = 0
    end = 2
    list = []


    for i in num:
        sam = i.upper()
        list.append(sam)

    while len(list) > count:
        stringer=""
        chunk=list[start:end]


        for i in chunk:
            stringer= stringer + str(i)

            if stringer == "0":
                hex = hex + "0000"
            elif stringer == "1":
                hex = hex + "0001"
            elif stringer =="2":
                hex = hex + "0010"
            elif stringer == "3":
                hex = hex + "0011"
            elif stringer == "4":
                hex = hex + "0100"
            elif stringer == "5":
                hex = hex + "0101"
            elif stringer == "6":
                hex = hex +"0110"
            elif stringer == "7":
                hex = hex + "0111"
            elif stringer == "8":
                hex = hex + "1000"
            elif stringer =="9":
                hex = hex + "1001"
            elif stringer == "A":
                hex = hex + "1010"
            elif stringer == "B":
                hex = hex + "1011"
            elif stringer == "C":
                hex = hex + "1100"
            elif stringer == "D":
                hex = hex + "1101"
            elif stringer == "E":
                hex = hex +"1110"
            elif stringer == "F":
                hex = hex + "1111"

        start = start + 1
        end = end + 1
        count = count + 1

    hex = bintodec(hex)

    return hex






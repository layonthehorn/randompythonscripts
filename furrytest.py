#!/usr/bin/env python3

import time, sys

def c_test():
    while 1:
        print("ctrl-c to quit")
        testcute = input("Are you cute? y/n ")
        if testcute.lower() == "y":
            cute = True
            break
        elif testcute.lower() == "n":
            cute = False
            break
        else:
             continue
    return cute


def run_loop():
    try: 
        while 1:
            result = c_test()
            if result:
                print("Good glad to hear it.\n")
            if not result:
                print("Well that's too bad then.\n")

    except KeyboardInterrupt:
        print("\nYou're still infected by the furry.\nYou can't run forever.")
    sys.exit(0)

run_loop()

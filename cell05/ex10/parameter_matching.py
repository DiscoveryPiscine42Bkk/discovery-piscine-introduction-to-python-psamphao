#!/usr/bin/python3
import sys 

if len(sys.argv) == 2:
    parameter = sys.argv[1]
    user_input = input("what was the parameter? ")

    if user_input == parameter:
        print("Good Job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
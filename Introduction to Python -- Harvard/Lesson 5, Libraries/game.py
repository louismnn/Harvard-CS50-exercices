import random
import sys

while True:
    try:
        inpt01 = int(input("Level: "))
        if inpt01 < 1:
            raise ValueError
        else:
            break
    except ValueError:
        continue

robot = int(random.randint(1, inpt01))

def my_function(inpt):
    while int(inpt) != robot:
        if int(inpt) < robot:
            print("Too Small!")
            input02()

        elif int(inpt) > robot:
            print("Too large!")
            input02()

    else:
        sys.exit("Just right!")
        

def input02():
    while True:
        try:
            inpt02 = int(input("Guess: "))
            if inpt02 < 1:
                raise ValueError
            elif inpt02 > inpt01:
                raise ValueError
            else:
                my_function(inpt02)
        except ValueError:
            continue

input02()

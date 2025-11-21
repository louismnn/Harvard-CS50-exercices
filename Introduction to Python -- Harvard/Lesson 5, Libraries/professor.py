import random
import sys


def dfmain(number01, random_operator, number02):

    error = 1
    inpt = input(f"{number01} {random_operator} {number02} = ")
    result = eval(f"{number01} {random_operator} {number02}")

    try:
        if int(inpt) == result:
            return True
        else:
            raise ValueError

    except ValueError:
        print("EEE")
        while int(inpt) != result and error <= 2:
            error += 1          
            inpt = input(f"{number01} {random_operator} {number02} = ")
            print("EEE")
            
        return False


def get_level():
    while True:
        level = input("Level: ")

        if level == "1":
            level1, level2 = 0, 9
            return level1, level2
        elif level == "2":
            level1, level2 = 10, 99
            return level1, level2
        elif level == "3":
            level1, level2 = 100, 999
            return level1, level2
        else:
            continue  


def generate_integer(level1, level2):

    number01 = random.randint(level1, level2)
    operators = ['+', '-', '/', '*']
    random_operator = random.choice(operators)

    if random_operator == '/':
        number02 = random.randint(level1, level2)

        while number01 % number02 != 0:
            number02 = random.randint(level1, level2)

    elif random_operator == '-':
        number02 = random.randint(level1, level2)
        
        while number02 > number01:
            number02 = random.randint(level1, level2)

    else:
        number02 = random.randint(level1, level2)

    return number01, random_operator, number02


def main():
    total, score = 0, 0
    level1, level2 = get_level()

    while total < 10:
        numbers1, numbers2, numbers3 = generate_integer(level1, level2)
        result = dfmain(numbers1, numbers2, numbers3)
        if result == True:
            score += 1
        total += 1

    sys.exit(f"Your score is {score}/10")

if __name__ == "__main__":
    main()
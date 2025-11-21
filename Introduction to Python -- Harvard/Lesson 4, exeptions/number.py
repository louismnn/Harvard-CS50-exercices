try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a integer")
else:
    print(f"is is {x}")


def get_int():
    while True: # Create a infinit loop
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not a integer")
        else:
            return x

def main():
    x = get_int()
    print(f"x is {x}")

main()

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
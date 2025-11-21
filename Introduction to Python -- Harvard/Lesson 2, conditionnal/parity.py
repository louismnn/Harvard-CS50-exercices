##--------
x = int(input("What's x?"))

## % is for the euclidiean division

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

##--------
def main():
    x = int(input("What's x? "))
    if  is_even(x):
        print("Even")
    else:
        print("Odd")

## Boolean can only be TRUE or FALSE
## Creation of the function 'is_even'

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even(n):
    return True if n % 2 == 0 else False

main()
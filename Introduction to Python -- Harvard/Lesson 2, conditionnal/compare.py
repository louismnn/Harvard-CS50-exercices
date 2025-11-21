##--------
x = int(input("Whet's x?"))
y = int(input("What's y?"))

if x < y :
    print("x is less than y")
if x > y :
    print("x is greater than y")
if x == y :
    print("x is equal to y")

##--------
# elif == else + if, it's good when multiple loops
if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y")
else :
    print("x is equal to y")

##--------
if x < y or x > y :
    print("x is not equal to y")
else :
    print("x is equal to y")
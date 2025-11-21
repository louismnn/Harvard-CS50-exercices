##----------
i = 1
while i <= 3:
    print("meow")
    i += 1

##----------
# int = integrer
# bools =  boolean
# str = strings
# float = floating (number with a decimal)
# Python also have list
##----------
for i in [0, 1, 2]:
    print("meow")

# This method could be very long if the number is 999 999, 
# not a good method. The solution is :
for i in range(3) :
    print("meow")

print("meow" * 3)
# meowmeowmeow

print("meow\n" * 3, end="")
#meow
#meow
#meow

while True:
    n = int(input("What's n? "))
    if n > 0:
        break



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Wjat's n? "))
        if n > 0:
            break
    return n    
    
def meow(n):
    for _ in range(n):
        print("meow")

main()
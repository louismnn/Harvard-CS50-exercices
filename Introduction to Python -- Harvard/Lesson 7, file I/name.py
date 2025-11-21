names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

print(f"hello, {names}")

for name in sorted(names):
    print(f"hello, {name}")

# File I/O can save de names that I gave

name = input("What's your name? ")

# open function is usefull for open a file, I can take information or write 
# information to it

file = open("names.txt", "w")
# The second argument is the w of the write function
# If the file don't exit it will be create or me
file.write(f"{name}\n")
file.close()

with open("names.txt", "a") as file:
# The second argument is the a of the append function
    file.write(f"{name}\n")

with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())


names = []

with open("names.txt") as file:
    for line in sorted(file):
        names.append(line.rstrip())
# sorted() is for classify the names in the alphabetical order
# rstrip() is for delete some string characters

for name in sorted(names):
    print(f"hello, {name}")

# csv = comma, separated value
with open("sudents.csv", "a") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        # print : the first element of the list of each row, is in, the last
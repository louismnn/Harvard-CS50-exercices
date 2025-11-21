import sys
import os

def my_function(file):
    with open(file, "r") as file:

        count = 0

        for new_line in file:
            new_line = new_line.strip()

            if not new_line.startswith("#"):
                count += 1
        
        print(f"Number of lines (excluding comments): {count}")
        
if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()

line = sys.argv[1]

while True:
    name, py = line.split(".")
    if py == "py":
        break
    else:
        print("Not a python file")
        sys.exit()

my_list = list(os.listdir())

if line in my_list:
    my_function(line)
else:
    print("File does not exist")
    sys.exit()
## --- Print 3 blocs
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

## --- Print 4 question blocs
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

## --- Make a 3*3 block
def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):

        # For each row in square
        for j in range(size):
            
            print("#", end="")
        print()

## --- 
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
    
main()

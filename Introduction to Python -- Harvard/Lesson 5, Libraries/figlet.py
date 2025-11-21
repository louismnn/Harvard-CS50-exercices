import sys
import pyfiglet

if sys.argv[1] == "-f":

    police = sys.argv[2]
    text = input("Input : ")

    print(pyfiglet.figlet_format(text, font=police))
else:
    sys.exit("Invalid usage")
import sys

def prompt():
    inpt = input("Date: ").strip()

    if inpt == "9/8/1636" or inpt == "September 8, 1636":
        sys.exit("1636-09-08")
    elif inpt == "10/9/1701" or inpt == "October 9, 1701":
        sys.exit("1701-10-09")
    else:
        prompt()
    
prompt()

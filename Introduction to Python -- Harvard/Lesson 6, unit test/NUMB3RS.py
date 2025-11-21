import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^([0-2][0-9][0-9]\.)"
                 r"([0-9]{1,3}\.)"
                 r"([0-9]{1,3}\.)"
                 r"([0-9]{1,3})$", ip):
        second_validation(ip)
    else:
        return False

def second_validation(ip):
    a, b, c, d = str(ip).split(".")
    if float(a) <= 255:
        return True
    else:
        return False


main()
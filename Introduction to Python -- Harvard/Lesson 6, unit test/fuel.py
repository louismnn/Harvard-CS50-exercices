import sys

def main():
    while True:
        try:
            x, y = input("Fraction : ").split("/")
            x, y = int(x), int(y)
            if y != 0:
                z = x/y
                return z
            else:
                raise ZeroDivisionError
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(z):
    percentage = z * 100
    return percentage


def gauge(percentage):
    if percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    elif percentage > 100:
        main()
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
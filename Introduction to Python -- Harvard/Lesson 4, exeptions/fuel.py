import sys

def main():
    while True:
        try:

            x, y = input("Fraction : ").split("/")
            x, y = int(x), int(y)
            z = (x/y) * 100

            if y != 0:
                if z == 0:
                    print("E")
                    sys.exit()
                elif z == 100:
                    print("F")
                    sys.exit()
                elif z > 100:
                    pass
                else:
                    print(f"{z:.0f}%")
                    sys.exit()
            else:
                pass

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
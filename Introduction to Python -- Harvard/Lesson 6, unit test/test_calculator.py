from calculator import square

def main():
    test_square()

# assert = if you assert and it's not true, will return a boolean
def test_square():
    try:   
        assert square(2) == 4
    except AssertionError:
        assert square(3) == 9
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 9
    except AssertionError:
        print("-2 squared was not 9")

if __name__ == "__main__":
    main()

# Use pytest in the powershell than python to look at your script problem
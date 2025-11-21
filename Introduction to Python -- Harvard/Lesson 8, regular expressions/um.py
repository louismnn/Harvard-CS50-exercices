def main():
    print(count(input("Text: ")))


def count(s):

    def boucle(symbol, s):
        n = 0
        while symbol in s:
            n += 1
            s = str(s).partition(symbol)[-1]
            # .partition split the string in three parts, before the symbol, the symbol and after the symbol
        else:
            return n
    
    sum = int(boucle("Um", s)) + int(boucle("um", s))
    return sum

if __name__ == "__main__":
    main()
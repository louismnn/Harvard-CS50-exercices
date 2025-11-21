def main():
    inpt = input("Input: ")
    output = shorten(inpt)
    print(f"Output: {output}")


def shorten(word):
    letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in letters:
        if i in word:
            word = str(word).replace(i, "")

    return word


if __name__ == "__main__":
    main()
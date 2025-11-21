number = input("What is the answer to the Great Question of Life, the Universe and Everything?")

match number:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")
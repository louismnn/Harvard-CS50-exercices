
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s)>6 or len(s)<2:
        return False
    elif not s.isalnum():
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False

    first_num=len(s)-1
    for character in s:
        if character.isnumeric():
            if character=='0':
                return False
            first_num = s.index(character)
            break

    for character in s:
        if s.index(character)<= first_num:
            pass
        else:
            if character.isalpha():
                return False
    return True


if __name__ == "main":
    main()

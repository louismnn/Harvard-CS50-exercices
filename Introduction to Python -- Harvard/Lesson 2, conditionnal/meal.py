##--------
def main(number):
    if number >= 7 and number <= 8 :
        print("Breakfast time")
    elif number >= 12 and number <= 13 :
        print("Launch time")
    elif number >= 18 and number <= 19 :
        print("Dinner time")
    else:
        print("Not time to eat")


def convert(time) :
    if len(time) == 4:
        time2 = int(time[2] + time[3])
        number = int(time[0]) + time2 / 60
        return number
    else:
        time2 = int(time[0] + time[1])
        time3 = int(time[3] + time[4])
        number = time2 + time3 / 60
        return number

if __name__ == "__main__":
    inpt = input("What time is it?")
    main(convert(inpt))
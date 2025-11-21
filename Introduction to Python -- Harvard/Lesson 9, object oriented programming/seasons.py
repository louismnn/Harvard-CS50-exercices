import datetime as dt
from datetime import date
from num2words import num2words
import sys

def seperate(word):
    try:
        year, month, day = str(word).split("-")
        data = (int(year), int(month), int(day))
        return data
    except ValueError:
        sys.exit("Invalid date")

def numtowords(number):
    words = num2words(number)
    return words

def main():

    birth = input("Date of birth: ")
    birth = seperate(birth)
    time1 = dt.datetime(birth[0], birth[1], birth[2])

    today = date.today()
    today = seperate(today)
    time2 = dt.datetime(today[0], today[1], today[2])

    minutes = int((time2 - time1).total_seconds()) / 60
    end = numtowords(minutes)
    sys.exit(end)


if __name__ == "__main__":
    main()

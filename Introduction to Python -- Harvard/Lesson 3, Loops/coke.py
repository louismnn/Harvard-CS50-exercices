AmountDue = 50

while AmountDue > 0:

    print("Amount Due:", AmountDue)
    coin = int(input("Insert coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        AmountDue -= coin

if AmountDue <= 0:
    AmountDue = -AmountDue

print('Change owed: ' + str(AmountDue))

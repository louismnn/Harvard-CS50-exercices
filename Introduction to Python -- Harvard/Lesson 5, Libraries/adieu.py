data = []

while True:
    try:
        line = input("Name: ")
        if line:
            data.append(line)
        else:
            raise EOFError

    except EOFError:
        break


if len(data) == 1:
    adieu = "Adieu, adieu, to " + data[0]
    print(adieu)
elif len(data) == 2:
    adieu = "Adieu, adieu, to " + data[0] + " and " + data[1]
    print(adieu)
else:
    new_data = str()
    last_element = data.pop()

    for i in data:
        new_data = new_data + str(i) + ", "

    adieu = "Adieu, adieu, to " + new_data + "and " + last_element
    print(adieu, sep=" ")


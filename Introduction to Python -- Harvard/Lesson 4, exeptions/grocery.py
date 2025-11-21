def inpt(data):

    while True:
        line = input()
        if line:
            data.append(line.upper())
        else:
            break

    return data

def transform(data):

    grocery_count = {}

    for item in data:
        if item in grocery_count:
            grocery_count[item] += 1
        else:
            grocery_count[item] = 1
    
    grocery = []

    for item, count in grocery_count.items():
        grocery.append(f"{count} {item}")

    for entry in grocery:
        print(entry)


liste = []
transform(inpt(liste))
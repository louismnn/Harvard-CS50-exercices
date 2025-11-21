inpt = input()
new_input = list(inpt.split(" "))
final = ""
total = int(len(new_input))-1
for i in range(0, total):
    final += new_input[i] + "..."
final = final + new_input[-1]
print(final)
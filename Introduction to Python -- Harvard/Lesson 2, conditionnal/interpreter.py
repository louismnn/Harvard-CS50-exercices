computation = input('Expression: ').split()

x = float(computation[0])
y = float(computation[2])

opr = computation[1]

if opr == '+':
    print(f"{x+y:.1f}")
elif opr == '-':
    print(f"{x-y:.1f}")
elif opr == '*':
    print(f"{x*y:.1f}")
elif opr == '/':
    print(f"{x/y:.1f}")
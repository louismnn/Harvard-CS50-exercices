def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):

    d1 = d.replace("$", "")
    d2 = float(d1)
    d3 = round(d2, 1)

    return d3


def percent_to_float(p):

    p1 = float(p.replace("%", ""))
    p2 = p1 / 100

    return p2

#check50 cs50/problems/2022/python/einstein
#submit50 cs50/problems/2022/python/einstein

main()
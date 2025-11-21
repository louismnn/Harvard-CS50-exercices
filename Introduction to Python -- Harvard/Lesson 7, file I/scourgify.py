import sys, os
import pandas as pd

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

csv1 = sys.argv[1]
csv2 = sys.argv[2]

try:
    name2, end2 = csv2.split(".")
except ValueError:
    sys.exit(1)

if csv1 != "before.csv":
    sys.exit("Could not read", sys.argv[1])
if end2 != "csv":
    sys.exit("Could not read", sys.argv[2])

if csv1 in list(os.listdir()):
    csv = pd.read_csv(csv1)
    csv = csv.replace('"','')
    csv[['fisrt','last']] = csv['name'].str.split(',',expand=True)
    house = csv["house"]
    csv = csv.drop(columns=['house', 'name'])
    csv.insert(2, "house", house, True)
    csv.to_csv(csv2, index=False)
    sys.exit()
else:
    sys.exit()

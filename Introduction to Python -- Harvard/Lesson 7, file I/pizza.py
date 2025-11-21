import tabulate, sys, os, csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

line = sys.argv[1]
name, end = line.split(".")

if end != "csv":
    sys.exit("Not a CSV file")

if line in list(os.listdir()):
    df = csv.reader(open(line, encoding="utf-8"))
    sys.exit(tabulate.tabulate(df, headers="firstrow", tablefmt="grid"))
else:
    sys.exit("File does not exist")

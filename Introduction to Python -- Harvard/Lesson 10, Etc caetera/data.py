import pandas as pd

file = "tic-tac-toe.csv"
data =  pd.read_csv(file)
print(data)

newdata = data[(data['class'] == 'True') & ~(data['TL'] == 'x')]
print(newdata)
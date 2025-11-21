import tictacto_functions as tic
import tictacto as tictac
import pandas as pd


def dictionnary():

    file = "tic-tac-toe.csv"
    dadata =  pd.read_csv(file)

    blank_row = pd.DataFrame([[""] * len(dadata.columns)], columns=dadata.columns)
    data = pd.concat([blank_row, dadata], ignore_index=True)

    return data


position = []

for i in tictac.dataframe3x3().df:
    if i == "X":
        variable = tictac.df[tictac.df[i] == "X"]
        position.append(variable)

print(position)










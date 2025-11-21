import tictacto_functions as func
import pandas as pd
import tabulate, sys


df = pd.DataFrame({
            "A": ["", "", ""],
            "B": ["", "", ""],
            "C": ["", "", ""],
            })


print(tabulate.tabulate(df, headers=["A", "B", "C"], tablefmt="rounded_grid"))

while True:

    func.player1_turn(df)
    winner1 = func.main(df)
    if winner1 == True:
        if func.draw(df) == True:
            pass
    else:
        sys.exit("Player 1 won")

    func.player2_turn(df)
    winner2 = func.main(df)
    if winner2 == True:
        if func.draw(df) == True:
            pass
    else:
        sys.exit("Player 2 won")


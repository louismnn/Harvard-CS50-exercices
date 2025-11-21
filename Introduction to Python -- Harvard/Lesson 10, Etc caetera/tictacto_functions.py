import tabulate, sys

## --------- check winner ---------------
def main(df):

    for i in range(3):
        if df.iloc[i, 0] == df.iloc[i, 1] == df.iloc[i, 2] and df.iloc[i, 0] in ['X', 'O']:
            return f"Player {df.iloc[i, 0]} won"

    for i in range(3):
        if df.iloc[0, i] == df.iloc[1, i] == df.iloc[2, i] and df.iloc[0, i] in ['X', 'O']:
            return f"Player {df.iloc[0, i]} won"

    if df.iloc[0, 0] == df.iloc[1, 1] == df.iloc[2, 2] and df.iloc[0, 0] in ['X', 'O']:
        return f"Player {df.iloc[0, 0]} won"
    elif df.iloc[0, 2] == df.iloc[1, 1] == df.iloc[2, 0] and df.iloc[0, 2] in ['X', 'O']:
        return f"Player {df.iloc[0, 2]} won"

    return True

## -------------- player one turn ---------------
def player1_turn(df):

    player1 = input("Choose a cell (X): ")

    while len(player1) != 2:
        print("Error, retry")
        player1 = input("Choose a cell (X): ")

    try:
        line = int(player1[1])
        col = str(player1[0]).capitalize()

        if (line < 3) and (col in str(df.columns)) and (df.loc[line, col] == ""):
            df.at[line, col] = "X"
            print(tabulate.tabulate(df, headers=["A", "B", "C"], tablefmt="rounded_grid"))
        else:
            print("Error, retry")
            player1_turn(df)

    except ValueError:
        print("Error, retry")
        player1_turn(df)


## -------------- player two turn ---------------
def player2_turn(df):

    player2 = input("Choose a cell (O): ")

    while len(player2) != 2:
        print("Error, retry")
        player2 = input("Choose a cell (O): ")

    try:
        line = int(player2[1])
        col = str(player2[0]).capitalize()

        if (line < 3) and (col in str(df.columns)) and (df.loc[line, col] == ""):
            df.at[line, col] = "O"
            print(tabulate.tabulate(df, headers=["A", "B", "C"], tablefmt="rounded_grid"))
        else:
            print("Error, retry")
            player2_turn(df)

    except ValueError:
        print("Error, retry")
        player2_turn(df)

## ---------- check draw ---------------
def draw(df):
    total = 0

    for i in range(3):
        for j in range(3):
            if "X" in df.iloc[i, j] or "O" in df.iloc[i, j]:
                total += 1

    if total < 9:
        return True
    else:
        sys.exit("Draw")

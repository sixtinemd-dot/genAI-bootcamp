grid = [[' ',' ',' ',],[' ',' ',' ',], [' ',' ',' ',]]

def display_board(grid):
    print("TIC TAC TOE")
    print("*" *17)
    print(f"*   {grid[0][0]} | {grid[0][1]} | {grid[0][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {grid[1][0]} | {grid[1][1]} | {grid[1][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {grid[2][0]} | {grid[2][1]} | {grid[2][2]}   *")
    print("*" *17)

    pass

def player_input(player):
    print(f"Player {player}'s turn...")

    while True:
        row_player_str = input("Enter row: ")
        if not row_player_str.isdigit():
            print("You must enter a number.")
            continue 

        row_player = int(row_player_str) - 1
        if row_player not in range(3):
            print("Please enter a number between 1 and 3.")
            continue
        break 

    while True:

        column_player_str = input("Enter column: ")    
        if not column_player_str.isdigit():
            print("You must enter a number.")
            continue
        
        column_player = int(column_player_str) - 1
        if column_player not in range(3):
            print("Please enter a number between 1 and 3.")
            continue 
        break

    if grid[row_player][column_player] == ' ':
            grid[row_player][column_player] = player    
    else:
            print("This spot is already taken! You lose your turn.")
        
pass

def check_win(board, player):

    # Rows
    if grid[0][0] == player and grid[0][1] == player and grid[0][2] == player:
        return True
    elif grid[1][0] == player and grid[1][1] == player and grid[1][2] == player:
        return True
    elif grid[2][0] == player and grid[2][1] == player and grid[2][2] == player:
        return True
    
    # Columns
    elif grid[0][0] == player and grid[1][0] == player and grid[2][0] == player:
        return True
    elif grid[0][1] == player and grid[1][1] == player and grid[2][1] == player:
        return True
    elif grid[0][2] == player and grid[1][2] == player and grid[2][2] == player:
        return True
    
    # Diagonals
    elif grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    elif grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True
    
    else:
        return False
    
pass

def check_tie(board):
    for row in grid:
        for column in row:
            if column == ' ':
                return False
    return True
pass

def play(grid):
    
    while True:
        player = input("current player (X/O): ").upper()
        if player != "X" and player != "O":
            print("Please enter 'x' or 'o'")
            continue
        break

    display_board(grid)
    while True:
        player_input(player)
        display_board(grid)
        if check_win(grid, player):
            display_board(grid)
            print(f"Player {player} wins!")
            break

        if check_tie(grid):
            display_board(grid)
            print("It's a tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

play(grid)






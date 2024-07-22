# Set up the board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))


# Function to check if a player has won
def check_win(player):
    # Check for horizontal win
    for row in board:
        if row.count(player) == 3:
            return True

    # Check for vertical win
    for i in range(3):
        column = [row[i] for row in board]
        if column.count(player) == 3:
            return True

    # Check for diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


# Function to check if the game is a tie
def check_tie():
    for row in board:
        if " " in row:
            return False
    return True


# Start the game
current_player = "X"
while True:
    print_board()
    print("It's", current_player, "'s turn.")

    # Get the player's move
    while True:
        row = int(input("Enter row (1-3): ")) - 1
        column = int(input("Enter column (1-3): ")) - 1
        if board[row][column] == " ":
            board[row][column] = current_player
            break
        else:
            print("That box is already taken. Please choose another one.")

    # Check for a win
    if check_win(current_player):
        print_board()
        print(current_player, "wins!")
        break

    # Check for a tie
    if check_tie():
        print_board()
        print("It's a tie!")
        break

    # Switch to the other player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
import random

# Define the game board (visible to player)
board = [["?" for _ in range(3)] for _ in range(3)]

# Create a hidden board to store actual bomb location
hidden_board = [["?" for _ in range(3)] for _ in range(3)]

# Place a random bomb on the hidden board
bomb_row = random.randint(0, 2)
bomb_col = random.randint(0, 2)
hidden_board[bomb_row][bomb_col] = "X"

# Function to check surrounding bombs
def check_surrounding(row, col):
    bombs = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            # Check within bounds and not the current cell
            if 0 <= i < 3 and 0 <= j < 3 and not (i == row and j == col):
                if hidden_board[i][j] == "X":
                    bombs += 1
    return bombs

# Function to display the board (only shows what the player sees)
def display_board():
    for row in board:
        print(" | ".join(row) + " | ")

# Function to check if a cell is already revealed
def is_cell_revealed(row, col):
    return board[row][col] != "?"

# Game loop
while True:
    print("============================================================================================================")
    # Display the board
    display_board()

    # Get user input
    try:
        print("============================================================================================================")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
    except ValueError:
        print("Invalid input. Please enter integers between 1 and 3.")
        continue

    # Check if bomb is chosen (check hidden board)
    if hidden_board[row][col] == "X":
        # Only reveal the bomb location
        board[bomb_row][bomb_col] = "X"
        print("============================================================================================================")
        display_board()
        print("Yikes, you found the bomb. The end :(")
        print("============================================================================================================")
        break

    # Check surrounding bombs (using hidden board)
    bombs_around = check_surrounding(row, col)
    board[row][col] = str(bombs_around) if bombs_around else "O" # Display number or open space

    # Check for win condition (all non-bomb cells revealed)
    win = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == "?" and hidden_board[i][j] != "X":
                win = False
                break
        if not win:
            break

    if win:
        print("You win! Congratulations!")
        display_board()
        break

    # Check for safe reveal and display message
    if bombs_around == 0 and not is_cell_revealed(row, col):
        print("Well, There's no Bomb here, congrats!")
        board[row][col] = " "  # Set the revealed cell as empty to indicate it has been revealed

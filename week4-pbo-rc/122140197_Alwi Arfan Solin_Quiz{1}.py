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

# Game loop
while True:
  # Display the board
  display_board()

  # Get user input
  try:
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
  except ValueError:
    print("Invalid input. Please enter integers between 1 and 3.")
    continue

  # Check if bomb is chosen (check hidden board)
  if hidden_board[row][col] == "X":
    print("BOOM! You lose.")
    # Only reveal the bomb location
    board[bomb_row][bomb_col] = "X"
    display_board()
    break

  # Check surrounding bombs (using hidden board)
  bombs_around = check_surrounding(row, col)
  board[row][col] = str(bombs_around) if bombs_around else "O"  # Display number or open space

  # Check for win condition (all non-bomb cells revealed)
  win = True
  for row in board:
    for cell in row:
      if cell == "?":
        win = False
        break
  if win:
    print("You win! Congratulations!")
    display_board()
    break

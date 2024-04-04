import random

words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

stages = ["""
    ------
    |   |
    |
    |
    |
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |
    |
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |   |
    |
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |  /|
    |
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |  /|\
    |
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |  /|\
    |  /
    |
    |
  ------------
""", """
    ------
    |   |
    |   O
    |  /|\
    |  / \
    |
    |
  ------------
"""]

# Function to select a random word
def get_word():
    return random.choice(words)

# Function to display the hangman stage
def display_hangman(lives):
    print(stages[lives])

# Function to display the guessed letters
def display_guessed(guessed_letters, hidden_word):
    # Create a list to hold the displayed word
    display = []
    for letter in hidden_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    print(" ".join(display))

def main():
    # Select a random word
    hidden_word = get_word()
    # Convert the word to a list of characters (easier to manipulate)
    word_list = list(hidden_word)

    # Initialize variables
    guessed_letters = []
    lives = 6

    # Game loop
    while lives > 0:
        # Display the hangman stage and guessed letters
        display_hangman(lives)
        display_guessed(guessed_letters, hidden_word)

        # Check if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word_list):
            print("Congratulations, You've guessed the word : ", hidden_word)
            return

        # Get user input
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            elif guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                break
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess not in word_list:
            lives -= 1
            print("Wrong guess!")

    # Display the result
    display_hangman(lives)
    display_guessed(guessed_letters, hidden_word)
    print("You lose! The word was", hidden_word)

if __name__ == "__main__":
    main()

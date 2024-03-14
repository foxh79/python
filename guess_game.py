# Define the secret number that the user will try to guess
secret_number = 9

# Initialize the guess count to 0
guess_count = 0

# Set the maximum number of guesses allowed
guess_limit = 3

# Start a while loop to allow the user to guess the secret number
while guess_count < guess_limit:
    # Get the user's guess and increment the guess count
    guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    # Check if the user's guess is too low
    if guess < secret_number:
        print("Too low!")
    # Check if the user's guess is too high
    elif guess > secret_number:
        print("Too high!")
    # If the user's guess is correct, print a success message and exit the loop
    else:
        print("You got it!")
        break

# Print a message to indicate that the game is over
print("Game over!")

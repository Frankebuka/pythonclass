import random  # Import the random module

while True:  # Start an outer loop for replaying the game
    correct_number = random.randint(1, 10)  # Set the correct number to a random number between 1 and 10
    print(correct_number)
    max_attempts = 3  # Maximum number of attempts

    while True:  # Start an inner loop for the game
        guess = int(input("Guess a number: "))  # Ask the user to guess a number

        if guess == correct_number:  # If the guess is correct
            print("Congratulations! You've guessed the correct number.")  # Print a winning message
            break  # End this round of the game
        else:  # If the guess is incorrect
            max_attempts -= 1  # Decrement the counter
            if max_attempts == 0:  # If the maximum number of attempts has been reached
                print("Sorry, you've reached the maximum number of attempts. Game over.")
                break  # End this round of the game
            else:
                print("Sorry, that's not correct. Try again. Your remaining attempts is",max_attempts)  # Ask the user to try again

    play_again = input("Do you want to play again? (yes/no): ")  # Ask the user if they want to play again
    if play_again.lower() != "yes":  # If the user doesn't want to play again
        break  # End the game
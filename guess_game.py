import random 

while True: 
    correct_number = random.randint(1, 10) 
    print(correct_number)
    max_attempts = 3 

    while True: 
        guess = int(input("Guess a number: ")) 

        if guess == correct_number: 
            print("Congratulations! You've guessed the correct number.") 
            break 
        else: 
            max_attempts -= 1 
            if max_attempts == 0: 
                print("Sorry, you've reached the maximum number of attempts. Game over.")
                break 
            else:
                print("Sorry, that's not correct. Try again. Your remaining attempts is",max_attempts)

    play_again = input("Do you want to play again? (yes/no): ") 
    if play_again.lower() != "yes": 
        break 
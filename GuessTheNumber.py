import random


def guessTheNumber():
    number = random.randint(1, 100)
    print("\n-----------------Start of 'Guess The Number'-----------------")
    numberOfGuesses = 5
    lower_bound = 1
    upper_bound = 100

    while numberOfGuesses > 0:
        try:
            guess = int(input(
                f"Guess a number between {lower_bound} and {upper_bound}, you have {numberOfGuesses} guesses left: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        difference = abs(number - guess)
        numberOfGuesses -= 1

        if guess < number:
            print(f"\nThe number was too low. You have {numberOfGuesses} guesses left.")
            lower_bound = guess + 1  # Update the lower bound
            if difference <= 5:
                upper_bound = min(guess + 5, 100)
                print(f"You're within 5 numbers of the correct answer!")
            elif difference <= 10:
                upper_bound = min(guess + 10, 100)
                print(f"You're within 10 numbers of the correct answer!")
            elif difference <= 25:
                upper_bound = min(guess + 25, 100)
                print(f"You're within 25 numbers of the correct answer!")
            elif difference <= 50:
                upper_bound = min(guess + 50, 100)
                print(f"You're within 50 numbers of the correct answer!")

        elif guess > number:
            print(f"\nThe number was too high. You have {numberOfGuesses} guesses left.")
            upper_bound = guess - 1  # Update the upper bound
            if difference <= 5:
                lower_bound = max(guess - 5, 1)
                print(f"You're within 5 numbers of the correct answer!")
            elif difference <= 10:
                lower_bound = max(guess - 10, 1)
                print(f"You're within 10 numbers of the correct answer!")
            elif difference <= 25:
                lower_bound = max(guess - 25, 1)
                print(f"You're within 25 numbers of the correct answer!")
            elif difference <= 50:
                lower_bound = max(guess - 50, 1)
                print(f"You're within 50 numbers of the correct answer!")

        else:
            print("\nYou guessed correct!")
            print(f"The number was: {number}")
            guesses_used = 5 - numberOfGuesses
            print(f"You won on try number {guesses_used}!")
            break

    if numberOfGuesses == 0:
        print(f"You ran out of guesses. The correct number was {number}. GAME OVER!!")

    playAgain = input("Do you want to play again? 'y' to play again, anything else to quit: ")
    if playAgain.lower() == 'y':
        guessTheNumber()
    else:
        print("Thanks for playing! Hope you enjoyed the game.")


guessTheNumber()


"""
Number Guessing Game (CLI)
Author: Prakhar Srivastava
Description: User tries to guess a randomly generated number.
"""

import random
def guessing_game():
    print("\n===== Number Guessing Game =====")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! ⬇️\n")
        elif guess > secret_number:
            print("Too high! ⬆️\n")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            break
    else:
        print(f"\n❌ Game Over! The number was {secret_number}.")


if __name__ == "__main__":
    guessing_game()

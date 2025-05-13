"""Bagels
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle
"""

import random
import sys

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    return "".join(str(random.randint(0, 9)) for _ in range(NUM_DIGITS))


def getClues(guess: str, secretNum: str):
    if guess == secretNum:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"

    clues.sort()

    return " ".join(clues)


def main():
    print(
        f"""Bagels, a deductive logic game.

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
    Pico         One digit is correct but in the wrong position. 
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
        
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
"""
    )

    while True:
        secretNum = getSecretNum()

        print("I have thought up a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        for numGuesses in range(1, MAX_GUESSES + 1):
            guess = ""

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break

            if numGuesses >= MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}.")

        print("Do you want to play again? (yes or no)")

        if not input("> ").lower().startswith("y"):
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)

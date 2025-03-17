from functions import MAX_GUESSES, NUM_DIGITS, getClues, getSecretNum

print(
    f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

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

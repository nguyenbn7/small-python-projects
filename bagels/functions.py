import random

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

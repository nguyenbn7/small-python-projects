import logging
import random

logging.basicConfig(
    level=logging.WARN, format=" %(asctime)s - %(levelname)s - %(message)s"
)

guess = ""
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug(
    f"{toss} (toss value) {'!=' if toss != guess else '=='} {guess} (guess value)"
)
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guesss = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")

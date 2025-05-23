#! python3
"""Collatz Sequence

Generates numbers for the Collatz sequence, given a starting number.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math
"""

import sys
import time


def main():

    print(
        """Collatz Sequence, or, the 3n + 1 Problem

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
"""
    )

    print("Enter a starting number (greater than 0) or QUIT:")
    response = input("> ")

    if not response.isdecimal() or response == "0":
        print("You must enter an integer greater than 0.")
        sys.exit()

    n = int(response)
    print(n, end="", flush=True)

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        print(", " + str(n), end="", flush=True)
        time.sleep(0.1)

    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)

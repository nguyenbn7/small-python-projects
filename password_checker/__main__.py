import sys
from getpass import getpass

from functions import get_password_leaks_count
from readchar import readchar

while True:
    try:
        prompt_msg = "Enter a password or Ctrl-c to exit: "
        password = getpass(prompt_msg)
        count = get_password_leaks_count(password)
        if count:
            print(
                f"Password you entered was found {count} times... you should probably change your password"
            )
        else:
            print(f"Password you entered was NOT found. Carry on!")
    except KeyboardInterrupt:
        print()
        quit_msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
        print(quit_msg, end="", flush=True)
        res = readchar()
        if res == "y":
            print("")
            sys.exit(1)
        else:
            print("", end="\r", flush=True)
            print(
                " " * (len(quit_msg) + len(prompt_msg)), end="", flush=True
            )  # clear the printed line
            print("    ", end="\r", flush=True)

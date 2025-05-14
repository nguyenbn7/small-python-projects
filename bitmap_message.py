#! python3
"""Bitmap Message

Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic
"""

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""


def main():
    print("Bitmap Message")
    print("Enter the message to display with the bitmap.")
    message = input("> ")

    if message == "":
        sys.exit()

    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == " ":
                print(" ", end="")
            else:
                print(message[i % len(message)], end="")
        print()

    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)

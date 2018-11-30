"""
    author: Chris Cheney
    Solve ceasar cipher
"""

import sys

def shift(phrase, offset):
    """
        Shift the characters in a phrase
        parameters:
            phrase: string
            offset: int
    """
    shifted = ""
    phrase = phrase.lower()
    for letter in phrase:
        if letter != " ":
            encodedShifted = ord(letter) + offset
            if encodedShifted > ord("z"):
                encodedShifted -= ord("z") - ord("a") + 1
            letter = chr(encodedShifted)
        shifted += letter

    return shifted


def main():
    encoded = []
    for arg in sys.argv[1:]:
        encoded.append(arg)
    encoded = ' '.join(encoded)

    for i in range(1, 26):
        print(str(i) + ": " + shift(encoded, i))


if __name__ == "__main__":
    main()

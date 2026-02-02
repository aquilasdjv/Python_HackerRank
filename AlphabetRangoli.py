# AlphabetRangoli.py
"""
Docstring for AlphabetRangoli
This module contains functions to print an alphabet rangoli of a given size.
Authors: Aquilas DJENONTIN
"""
import string

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def print_rangoli(size):
    """Prints an alphabet rangoli of the specified size.
    Args:
        size (int): The size of the rangoli (number of letters).
    using string module
    """

    alpha = string.ascii_lowercase

    # Calculate the width of the rangoli
    width = 4 * size - 3

    # Create the rangoli pattern
    lines = []
    for i in range(size):
        s = "-".join(alpha[size - 1 : i : -1] + alpha[i:size])
        lines.append(s.center(width, "-"))

    # Print the rangoli
    print("\n".join(lines[::-1] + lines[1:]))


def print_rangoli1(size):
    """
    Docstring for print_rangoli
    :param size: Description
       Prints an alphabet rangoli of the specified size.
       Args:
           size (int): The size of the rangoli (number of letters).
       using slicing and join method
    """
    useFullWord = ALPHABET[0:size]
    for i in range(size):
        s = "-".join(
            "".join(reversed(useFullWord[size - i :])) + useFullWord[size - i - 1 :]
        )
        print(s.center((size * 4) - 3, "-"))
    for i in reversed(range(size - 1)):
        s = "-".join(
            "".join(reversed(useFullWord[size - i :])) + useFullWord[size - i - 1 :]
        )
        print(s.center((size * 4) - 3, "-"))


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the size of the rangoli: "))
    print_rangoli(n)

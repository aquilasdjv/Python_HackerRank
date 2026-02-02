# StringFormatting.py

"""
Docstring for StringFormatting
This module contains functions to print numbers in different formats:
decimal, octal, hexadecimal, and binary.
Authors: Aquilas DJENONTIN
"""


def print_formatted(number):
    """Prints the decimal, octal, hexadecimal (uppercase), and binary
    representations of numbers from 1 to 'number', formatted in columns.
    Args:
        number (int): The maximum number to format.
    """
    width = len(bin(number)) - 2  # Calculate the width based on binary representation

    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(f"{decimal} {octal} {hexadecimal} {binary}")


def print_formatted1(number):
    """
    Docstring for print_formatted1
    :param number: Description
    Prints the decimal, octal, hexadecimal (uppercase), and binary
    representations of numbers from 1 to 'number', formatted in columns.
    Args:
        number (int): The maximum number to format.
    """
    width = len(f"{number:b}")  # Calculate the width based on binary representation
    for i in range(1, number + 1):
        print(
            f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}"
        )  # Formatted string literals


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_formatted(n)

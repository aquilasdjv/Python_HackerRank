# Print_Function.py
"""
Docstring for Print_Function
This module contains a function that prints numbers from 1 to the given number.
The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
123...n
Where "..." represents the consecutive values in between.
# Example
If n = 5, then the output should be 12345.
Author: aquilas DJENONTIN
"""


def print_function(nbr):
    """
    Docstring for print_function
    :param nbr: Description
    Function to print numbers from 1 to nbr without spaces
    123...n
    using list comprehension and join method
    """
    print("".join([str(x + 1) for x in range(nbr)]))


def print_function_1(nbr):
    """
    Docstring for print_function_1
    :param nbr: Description
    Function to print numbers from 1 to nbr without spaces
    123...n
    using a loop and end parameter of print function
    """
    for i in range(1, nbr + 1):
        print(i, end="")
    print()  # For a new line after printing all numbers


def print_function_2(nbr):
    """
    Docstring for print_function_2
    :param nbr: Description
    Function to print numbers from 1 to nbr without spaces
    123...n
    using unpacking operator and sep parameter of print function
    """
    print(*range(1, nbr + 1), sep="")


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_function(n)

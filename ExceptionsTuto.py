# Exceptions Tuto
# https://www.hackerrank.com/challenges/exceptions/problem

"""
Docstring for ExceptionsTuto
ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.
ValueError: Raised when a built-in operation or function receives an argument that has the right type
but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
Author: Aquilas DJENONTIN
"""


def execptions_demo():
    """Function to demonstrate handling exceptions in Python."""
    n = int(input())
    for _ in range(n):
        try:
            a, b = map(str, input().split())
            print(int(a) // int(b))
        except ZeroDivisionError as z:
            print("Error Code:", z)
        except ValueError as v:
            print("Error Code:", v)


# Example usage:
if __name__ == "__main__":
    execptions_demo()

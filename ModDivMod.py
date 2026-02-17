# Mod DivMod
# Modulo and Integer Division
# https://www.hackerrank.com/challenges/python-mod-divmod/problem
"""
Docstring for ModDivMod
This program demonstrates the use of modulo and integer division in Python.
The function mod_div_mod takes two integers a and b as input and returns a tuple containing the results of integer division (a // b), modulo (a % b), and the divmod function (divmod(a, b)).
For example, if a = 10 and b = 3, the output will be:
(3, 1, (3, 1))
Constraints:
1 <= a, b <= 100
Complexity: O(1) for time complexity, as we are performing a constant number of operations regardless of the input size.
Author: Aquilas DJENONTIN
"""


def mod_div_mod(a, b):
    """
    This function takes two integers a and b as input and returns a tuple containing the results of integer division (a // b), modulo (a % b), and the divmod function (divmod(a, b)).
    """
    return (a // b, a % b, divmod(a, b))


# Example usage:
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(*mod_div_mod(a, b), sep="\n")

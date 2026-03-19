# Integers Come In All Sizes
# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
"""
Docstring for IntegersComeInAllSizes
This program demonstrates the use of the built-in pow function in Python to calculate the power of a number and the modulus of a number raised to a power.
The function intergers_come_in_all_sizes takes four integers a, b, c, and d as input and returns the sum of a raised to the power of b and c raised to the power of d.
For example, if a = 9, b = 29, c = 7, and d = 27, the output will be:
4710194409608608369201743232
Constraints:
1 <= a, b, c, d <= 1000
Complexity: O(1) for time complexity, as we are performing a constant number of operations regardless of the input size.
Author: Aquilas DJENONTIN
"""


def intergers_come_in_all_sizes(a, b, c, d):
    """
    This function takes four integers a, b, c, and d as input and returns the sum of a raised to the power of b and c raised to the power of d.
    You can use the built-in pow function or the exponentiation operator ** to calculate the powers.
    """
    return a**b + c**d


# Example usage:
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(intergers_come_in_all_sizes(a, b, c, d))

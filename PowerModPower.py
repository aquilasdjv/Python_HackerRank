# Power - Mod Power
# https://www.hackerrank.com/challenges/python-power-mod-power/problem
"""
Docstring for PowerModPower
This program demonstrates the use of the built-in pow function in Python to calculate the power of a number and the modulus of a number raised to a power.
The function power_mod_power takes three integers a, b, and m as input and returns a tuple containing the results of a raised to the power of b (a ** b) and the modulus of a raised to the power of b with respect to m (pow(a, b, m)).
For example, if a = 3, b = 4, and m = 5, the output will be:
(81, 1)
Constraints:
1 <= a, b, m <= 100
Complexity: O(1) for time complexity, as we are performing a constant number of operations regardless of the input size.
Author: Aquilas DJENONTIN
"""


def power_mod_power(a, b, m):
    """
    This function takes three integers a, b, and m as input and returns a tuple containing the results of a raised to the power of b (a ** b) and the modulus of a raised to the power of b with respect to m (pow(a, b, m)).
    """
    return (a**b, pow(a, b, m))


def power_mod_power_v2(a, b, m):
    """
    This function is an alternative implementation of power_mod_power using the built-in pow function for both calculations.
    It takes three integers a, b, and m as input and returns a tuple containing the results of a raised to the power of b (pow(a, b)) and the modulus of a raised to the power of b with respect to m (pow(a, b, m)).
    """
    return (pow(a, b), pow(a, b, m))


# Example usage:
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    print(*power_mod_power(a, b, m), sep="\n")

# Reduce Function
# https://www.hackerrank.com/challenges/reduce-function/problem
"""
Docstring for ReduceFunction
You are given a list of fractions. Your task is to find the product of these fractions and
print the result in its simplest form.
Input Format
The first line contains an integer n, the number of fractions.
The next n lines each contain two space-separated integers, the numerator and denominator of a fraction.
Constraints
1 <= n <= 10
1 <= numerator, denominator <= 10
Output Format
Print the product of the fractions in its simplest form, as two space-separated integers: the numerator and denominator.
Sample Input
3
1 2
3 4
5 6
Sample Output
5 16
Explanation
The product of the fractions is (1/2) * (3/4) * (5/6) = 15/48. The simplest form of this fraction is 5/16, so we print "5 16".
Author: Aquilas DJENONTIN
"""

from fractions import Fraction
from functools import reduce


def product(fracs):
    """
    A function to calculate the product of a list of fractions and return the result in its simplest form.
    Complexity: O(n) since we are iterating through the list of fractions once.
    """
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


# The main function to read input, calculate the product of the fractions and print the result.
if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

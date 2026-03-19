# Triangle Quest 2
# https://www.hackerrank.com/challenges/triangle-quest-2/problem
"""
Docstring for TriangleQuest2
This program prints the squares of the first n repunits, where a repunit is a number consisting of repeated units of 1.
The function triangle_quest_2 takes an integer n as input and prints the squares of the first n repunits.
For example, if n = 5, the output will be:
1
121
12321
1234321
123454321
Constraints:
1 <= n <= 15
Complexity: O(n) for time complexity, as we are iterating through the first n repunits and calculating their squares.
Author: Aquilas DJENONTIN
"""


def triangle_quest_2(n):
    """
    This program prints the squares of the first n repunits, where a repunit is a number consisting of repeated units of 1.
    The function triangle_quest_2 takes an integer n as input and prints the squares of the first n repunits.
    """

    for i in range(1, n + 1):
        print((10**i // 9) ** 2)


def triangle_quest_2_1(n):
    """
    This function is an alternative implementation of triangle_quest_2 that uses a different formula to calculate the squares of the repunits.
    The formula used in this implementation is ((10**i-1)//9)**2, which also generates the squares of the repunits.
    The output will be the same as the original triangle_quest_2 function for the same input n.
    """
    for i in range(1, n + 1):
        print(((10**i - 1) // 9) ** 2)


# Example usage:
if __name__ == "__main__":
    triangle_quest_2(int(input()))

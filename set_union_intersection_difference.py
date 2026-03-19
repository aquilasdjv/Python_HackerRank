"""
Docstring for SetUnionIntersectionDifference
This module defines three functions: union, intersection, difference, and symmetric_difference which perform set operations on two sets a and b.
The main block of the code reads input from the user, creates two sets, and prints the results of the three operations.
The input format is as follows:
- The first line contains an integer n, the number of elements in set a.
- The second line contains n space-separated integers, the elements of set a.
- The third line contains an integer m, the number of elements in set b.
- The fourth line contains m space-separated integers, the elements of set b.
The output format is as follows:
- The first line contains the number of elements in the union of sets a and b.
- The second line contains the number of elements in the intersection of sets a and b.
- The third line contains the number of elements in the difference of sets a and b (elements that are in a but not in b).
- The fourth line contains the number of elements in the symmetric difference of sets a and b (elements that are in either a or b but not in both).
Author: Aquilas DJENONTIN
"""


def union(a, b):
    """Returns the union of two sets a and b."""
    return a.union(b)


def intersection(a, b):
    """Returns the intersection of two sets a and b."""
    return a.intersection(b)


def difference(a, b):
    """Returns the difference of two sets a and b."""
    return a.difference(b)


def symmetric_difference(a, b):
    """Returns the symmetric difference of two sets a and b."""
    return a.symmetric_difference(b)


if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))

    print(len(union(a, b)))
    print(len(a.intersection(b)))
    print(len(a.difference(b)))
    print(len(symmetric_difference(a, b)))

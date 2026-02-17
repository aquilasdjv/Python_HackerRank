# Subset and Superset
"""
Docstring for SubsetAndSuperset
This module defines two functions: subSet and superSet, which check if one set is a subset or a superset of another set, respectively.
The subSet function reads input for multiple test cases, where each test case consists of two sets A and B. It checks if A is a subset of B and prints the result.
The superSet function reads input for a set A and multiple sets B, and checks if A is a superset of the union of all sets B, printing the result.
Author: Aquilas DJENONTIN
"""


def subSet():
    """
    The subSet function reads input from the user to determine if set A is a subset of set B. The input format is as follows:
    - The first line contains an integer T, the number of test cases.
    - For each test case, the first line contains an integer a, the number of elements in set A, followed by a line containing a space-separated integers representing the elements of set A.
    - The next line contains an integer b, the number of elements in set B, followed by a line containing b space-separated integers representing the elements of set B.
    The function prints True if A is a subset of B, and False otherwise.
    Complexity: O(n) where n is the number of elements in the larger set (either A or B) for each test case.
    """
    T = int(input())
    for _ in range(T):
        a = int(input())
        A = set(map(int, input().split()))
        b = int(input())
        B = set(map(int, input().split()))

        print(A.issubset(B))


def superSet():
    """
    The superSet function reads input from the user to determine if set A is a superset of set B. The input format is as follows:
    - The first line contains space-separated integers representing the elements of set A.
    - The next line contains an integer n, the number of sets to compare with A.
    - For each of the next n lines, there are space-separated integers representing the elements of set B.
    The function prints True if A is a superset of B, and False otherwise.
    Complexity: O(n) where n is the number of elements in the larger set (either A or B) for each test case.
    """
    A = set(map(int, input().split()))
    n = int(input())
    B = set()
    for _ in range(n):
        B.update(set(map(int, input().split())))

    print(A.issuperset(B))

# Main block to execute the functions
if __name__ == "__main__":
    subSet()
    superSet()

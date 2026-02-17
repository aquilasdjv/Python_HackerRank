# Symmetric Difference
"""
Docstring for SymmetricDifference
This module contains three functions that compute the symmetric difference of two sets of integers.
The symmetric difference is the set of elements that are in either of the sets, but not in both.
The functions read input from the user, compute the symmetric difference, and print the results in sorted order.
The first function, `sym()`, computes the symmetric difference using the `difference()` and `union()` methods of sets.
The second function, `sym2()`, computes the symmetric difference using the `symmetric_difference()` method of sets.
The third function, `sym3()`, computes the symmetric difference using the bitwise XOR operator (`^`) on sets.
Author: Aquilas DJENONTIN
"""


def sym():
    """
    Docstring for sym
    This function reads two sets of integers from the user, computes their symmetric difference using the `difference()` and `union()` methods, and prints the results in sorted order.
    The function first reads an integer `n` which represents the number of elements in the first set, then reads the elements of the first set `a`.
    Next, it reads an integer `m` which represents the number of elements in the second set, then reads the elements of the second set `b`.
    The symmetric difference is computed by taking the difference of `a` with `b` and the difference of `b` with `a`, and then taking the union of these two differences.
    Finally, the results are sorted and printed, with each element on a new line.
    """
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    s = sorted(a.difference(b).union(b.difference(a)))
    print(*s, sep="\n")


def sym2():
    """
    Docstring for sym2
    This function reads two sets of integers from the user, computes their symmetric difference using the `symmetric_difference()` method, and prints the results in sorted order.
    The function first reads an integer `n` which represents the number of elements in the first set, then reads the elements of the first set `a`.
    Next, it reads an integer `m` which represents the number of elements in the second set, then reads the elements of the second set `b`.
    The symmetric difference is computed using the `symmetric_difference()` method of sets, which returns a new set containing elements that are in either `a` or `b` but not in both.
    Finally, the results are sorted and printed, with each element on a new line.
    """
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    s = sorted(a.symmetric_difference(b))
    print(*s, sep="\n")


def sym3():
    """
    Docstring for sym3
    This function reads two sets of integers from the user, computes their symmetric difference using the bitwise XOR operator (`^`), and prints the results in sorted order.
    The function first reads an integer `n` which represents the number of elements in the first set, then reads the elements of the first set `a`.
    Next, it reads an integer `m` which represents the number of elements in the second set, then reads the elements of the second set `b`.
    The symmetric difference is computed using the bitwise XOR operator (`^`) on sets, which returns a new set containing elements that are in either `a` or `b` but not in both.
    Finally, the results are sorted and printed, with each element on a new line.
    """
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    s = sorted(a ^ b)
    print(*s, sep="\n")


# The main function to execute the symmetric difference computation
if __name__ == "__main__":
    sym()

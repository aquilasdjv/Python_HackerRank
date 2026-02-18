"""
Maximize It! - HackerRank Challenge Solution

This file contains multiple implementations of the solution to the HackerRank
problem "Maximize It!". The problem asks to compute the maximum possible value
of (x1^2 + x2^2 + ... + xk^2) % m, where xi is selected from k lists.

The file contains four versions of the solution:
- maximizeIt(): Basic iterative implementation
- maximizeIt_v2(): Uses itertools.product for cleaner syntax
- maximizeIt_v3(): Uses set comprehension with nested loops
- maximizeIt_v4(): Pre-computes squares for optimization

Author: Aquilas DJENONTIN
"""
from itertools import product

def maximizeIt():
    """
    Computes the maximum possible value of:
        (x1^2 + x2^2 + ... + xk^2) % m

    Time Complexity:
        For each of k lists, we combine all current possible values with
        all elements of the new list:
            O(k * |possible| * avg_len(arr))

        Since possible ⊆ {0, 1, ..., m-1}, we have:
            |possible| ≤ m
        Worst case:
            O(k * m * avg_len(arr))

    Space Complexity:
        O(|possible|) ≤ O(m)
    """

    k, m = map(int, input().split())
    possible = {0}

    for _ in range(k):
        arr = list(map(int, input().split()))[1:]
        new_set = set()
        for p in possible:
            for x in arr:
                new_set.add((p + x * x) % m)
        possible = new_set
    print(max(possible))


def maximizeIt_v2():
    """
    Computes the maximum possible value of:
        (x1^2 + x2^2 + ... + xk^2) % m

    Time Complexity:
        For each of k lists, we combine all current possible values with
        all elements of the new list:
            O(k * |possible| * avg_len(arr))

        Since possible ⊆ {0, 1, ..., m-1}, we have:
            |possible| ≤ m
        Worst case:
            O(k * m * avg_len(arr))

    Space Complexity:
        O(|possible|) ≤ O(m)
    """

    k, m = map(int, input().split())
    possible = {0}

    for _ in range(k):
        arr = list(map(int, input().split()))[1:]
        possible = {(p + x * x) % m for p, x in product(possible, arr)}

    print(max(possible))


def maximizeIt_v3():
    """
    Computes the maximum possible value of:
        (x1^2 + x2^2 + ... + xk^2) % m

    Time Complexity:
        For each of k iterations:
            O(|possible| * len(arr))

        Total:
            O(k * |possible| * avg_len(arr))
        Worst case (|possible| ≤ m):
            O(k * m * avg_len(arr))

    Space Complexity:
        O(|possible|) ≤ O(m)
    """

    k, m = map(int, input().split())
    possible = {0}

    for _ in range(k):
        arr = list(map(int, input().split()))[1:]
        possible = {(p + x * x) % m for p in possible for x in arr}

    print(max(possible))


def maximizeIt_v4():
    """
    Computes the maximum possible value of:
        (x1^2 + x2^2 + ... + xk^2) % m

    Time Complexity:
        Per iteration:
            - Squaring elements: O(len(arr))
            - Combining possibilities: O(|possible| * len(arr))
        Total:
            O(k * |possible| * avg_len(arr))

    Space Complexity:
        O(|possible| + len(arr)) ≤ O(m + max_len(arr))
    """

    k, m = map(int, input().split())
    possible = {0}

    for _ in range(k):
        arr = list(map(int, input().split()))[1:]
        squares = [x * x for x in arr]
        possible = {(p + sq) % m for p in possible for sq in squares}

    print(max(possible))

# Example usage:
if __name__ == "__main__":
    maximizeIt()

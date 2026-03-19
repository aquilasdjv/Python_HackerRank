# Piling Up
# https://www.hackerrank.com/challenges/piling-up/problem
"""
Docstring for PilingUp
You are given a list of cubes, where the length of each cube is between 1 and 100. You need to create a single vertical pile of cubes. The condition is that if cube i is on top of cube j, then the length of cube i must be less than or equal to the length of cube j. You can pick up either the leftmost or the rightmost cube each time.
Input Format
The first line contains a single integer T, the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N, the number of cubes. The second line contains N space-separated integers x1, x2,..., xN, where xi is the length of the ith cube.
Constraints
1 <= T <= 5
1 <= N <= 10^5
1 <= x_i <= 100
Output Format
For each test case, print "Yes" if it is possible to pile up the cubes. Otherwise, print "No".
Sample Input
2
6
4 3 2 1 3 4
3
1 3 2
Sample Output
Yes
No
Explanation
In the first test case, pick up the cubes in this order: 4, 4, 3, 3, 2, 1. In the second test case, no valid order exists.
Author: Aquilas DJENONTIN
"""

from collections import deque


def piling_up():
    """
    Determine if it's possible to pile up the cubes according to the given rules.
    Complexity: O(n) where n is the number of cubes.
    """
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        dq = deque(map(int, input().split()))
        last = float("inf")
        ok = True

        while dq:
            left, right = dq[0], dq[-1]
            pick_from_left = left >= right
            pick = left if pick_from_left else right

            if pick <= last:
                last = pick
                if pick_from_left:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                ok = False
                break

        print("Yes" if ok else "No")


# Example usage:
if __name__ == "__main__":
    piling_up()

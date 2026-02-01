# List_Comprehensions.py
"""
Docstring for List_Comprehensions
This module demonstrates the use of list comprehensions in Python.
It generates a list of all possible coordinates (i, j, k) on a 3D grid
where the sum of the coordinates is not equal to a given integer n.
The included code stub will read four integers x, y, z, and n from STDIN.
# Example
If x = 1, y = 1, z = 1, and n = 2, then the output should be:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
This is because the coordinates [0, 1, 1], [1, 0, 1], and [1, 1, 0] all sum to 2 and are excluded.
Author: aquilas DJENONTIN
"""

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if sum([i, j, k]) != n
    ])

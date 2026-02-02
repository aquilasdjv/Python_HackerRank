# DesihnerDoorMat.py
"""
This module provides functionality to create a designer door mat pattern.
It includes a function `designer_door_mat` and `designer_door_mat1` that prints the door mat pattern
based on the given dimensions.
Author: Aquilas DJENONTIN"""


def designer_door_mat(n, m):
    """
    Docstring for designer_door_mat function.
    :param n: Description
    :param m: Description
    :return: None
    prints the designer door mat pattern
    """
    for i in range(1, n, 2):
        out = ".|." * i
        print(out.center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in reversed(range(1, n, 2)):
        out = ".|." * i
        print(out.center(m, "-"))


def designer_door_mat1(n, m):
    """
    Docstring for designer_door_mat1 function.
    :param n: Description
    :param m: Description
    :return: None
    prints the designer door mat pattern
    """
    pattern = [".|."] * (n // 2)
    for i in range(n // 2):
        print((pattern[i] * (2 * i + 1)).center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n // 2 - 1, -1, -1):
        print((pattern[i] * (2 * i + 1)).center(m, "-"))


if __name__ == "__main__":
    n, m = map(int, input().split())
    designer_door_mat(n, m)

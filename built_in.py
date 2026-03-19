# https://www.hackerrank.com/challenges/zipped/problem
# https://www.hackerrank.com/challenges/python-eval/problem
# https://www.hackerrank.com/challenges/any-or-all/problem
# https://www.hackerrank.com/challenges/input/problem
"""
This module contains three functions that demonstrate the use of built-in functions in Python: 'zip', 'eval', 'any', and 'all'.
The 'zipped' function reads a matrix of floating-point numbers, transposes it, and prints the average of each column.
The 'inputed' function evaluates a mathematical expression with a variable 'x' and compares it to a given value 'k'.
The 'any_all' function checks if any of the integers in a list are even and if all of them are even.
Author: Aquilas DJENONTIN
"""


def zipped():
    """
    A function to read a matrix of floating-point numbers, transpose it, and print the average of each column.
    The function first reads the dimensions of the matrix (n rows and x columns) from input. It then reads
    the matrix values, transposes the matrix using the zip function, and calculates the average of each column by summing the values and dividing by the number of rows (x).
    Complexity: O(n*x) since we need to read n*x values and perform operations on them.
    """
    n, x = map(int, input().split())
    A = []
    for _ in range(x):
        A.append(list(map(float, input().split())))

    A = zip(*A)

    for y in A:
        print(sum(list(y)) / x)


def inputed():
    """
    A function to evaluate a mathematical expression with a variable 'x' and compare it to a given value 'k'.
    The function reads the values of 'x' and 'k' from input, as well as the expression 'p' which contains 'x'.
    It then replaces 'x' in the expression with the actual value of 'x', evaluates the expression, and checks if it equals 'k'.
    This challenge was made for pyhton 2, but it works in python 3 as well.
    Complexity: O(1) since we are performing a constant number of operations.
    """
    x, k = map(int, input().split())
    p = input()
    pl = f"{p.replace('x',str(x))}"

    print(eval(pl) == k)


def any_all():
    """
    A function to read a list of integers and check if any of them are even and if all of them are even.
    The function reads the number of integers 'n' from input, followed by the list of integers.
    It then uses the built-in 'any' and 'all' functions to check for even numbers and prints the results.
    Complexity: O(n) since we need to check each integer in the list.
    """
    n = input()
    arr = list(map(int, input().split()))
    print(all([all([x >= 0 for x in arr]), any([str(x) == str(x)[::-1] for x in arr])]))


# The main function to call the above functions.
if __name__ == "__main__":
    zipped()
    inputed()
    any_all()

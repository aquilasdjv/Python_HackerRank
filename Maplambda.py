# Map lambda functions
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
"""
Docstring for Maplambda
You are given a function f and a list of numbers. Your task is to apply the function
to each element of the list and print the result.
Input Format
The first line contains an integer n, the number of elements in the list.
The second line contains n space-separated integers, the elements of the list.
Constraints
1 <= n <= 10
-100 <= x <= 100, where x is an element of the list.
Output Format
Print the result of applying the function to each element of the list, space-separated.
Sample Input
5
0 1 2 3 4
Sample Output
0 1 8 27 64
Explanation
The function f is defined as f(x) = x^3. Applying this function to each element of the list gives us the output.
Author: Aquilas DJENONTIN
"""

cube = lambda x: x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    """
    A function to generate a list of Fibonacci numbers up to n.
    Complexity: O(n) since we are generating n Fibonacci numbers.
    """
    a, b = 0, 1
    l = []
    for _ in range(n):
        l.append(a)
        a, b = b, a + b
    return l


# The main function to read input, generate Fibonacci numbers, apply the cube function and print the result.
if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Triangle Quest
# https://www.hackerrank.com/challenges/python-quest-1/problem
"""Docstring for TriangleQuest
This program generates a specific pattern of numbers based on the input integer n.
The pattern consists of lines of numbers where each line i (from 1 to n) contains the number i repeated i times. For example, if n = 5, the output will be:
1
22
333
4444
55555
The function triangle_quest takes an integer n as input and prints the desired pattern. The pattern is generated using a mathematical formula that calculates the required number for each line without using string manipulation, which is not allowed in this challenge.
Constraints:
1 <= n <= 9
Complexity: O(n) for time complexity, as we need to generate n lines of output.
Author: Aquilas DJENONTIN
"""


def triangle_quest(n):
    for i in range(1, n + 1):
        # This is a mathematical formula to generate the desired pattern. The expression (10**i - 1) generates a number consisting of i digits of 9 (e.g., for i=3, it generates 999).
        # Dividing by 9 converts this to a number consisting of i digits of 1 (e.g., for i=3, it becomes 111). Finally, multiplying by i gives the final pattern (e.g., for i=3, it results in 333).
        print(((10**i - 1) // 9) * i)
        # Here is an alternative way to achieve the same result using string manipulation:
        # print(str(i) * i)
        # print(f"{i}"*i)
        # But the first method is more efficient as it avoids string concatenation and directly computes the desired number using arithmetic operations.
        # and string manipulation is not allowed in this challenge, so we will stick to the first method.


# Example usage:
if __name__ == "__main__":
    n = int(input())
    triangle_quest(n)

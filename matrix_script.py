# Matrix Script
# https://www.hackerrank.com/challenges/matrix-script/problem
"""
Docstring for MatrixScript
You are given a 2D matrix of size NXM. The matrix contains alphanumeric characters
Your task is to read the matrix column-wise and convert it into a single string. After reading the string, you need to replace any consecutive non-alphanumeric characters between two alphanumeric characters with a single space.
Input Format
The first line contains space-separated integers N and M, the number of rows and columns in the matrix.
The next N lines contain M space-separated alphanumeric characters, denoting the elements of the matrix.
Constraints
0 < N < 100
0 < M < 100
Output Format
Print the decoded string after replacing consecutive non-alphanumeric characters with a single space.
Sample Input
7 3
Tsi
h%x
i #
sM
$a
$t%
ir
Sample Output
This is Matrix#  %!
Explanation
The characters are read column-wise, resulting in the string "This$#is% Matrix%  !". After replacing consecutive non-alphanumeric characters with a single space, we get "This is Matrix#  %!".
Author: Aquilas DJENONTIN
"""

import re


def matrix_script():
    """
    A function to read a 2D matrix, convert it into a string by reading column-wise, and replace consecutive non-alphanumeric characters with a single space.
    Complexity: O(N*M) since we are iterating through the matrix once to read the characters and once to replace the non-alphanumeric characters.
    """
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    ch = ""
    for i in range(m):
        for j in range(n):
            ch += matrix[j][i]

    clean = re.sub(r"(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])", " ", ch)
    print(clean)


if __name__ == "__main__":
    matrix_script()

# Hex Color Code
# https://www.hackerrank.com/challenges/hex-color-code/problem
"""
Docstring for HexColorCode
You are given a string S. Your task is to find and print all the valid hex color codes from the string S, in order of their occurrence.
Input Format
The first line contains an integer N, the number of lines in the string S.
The next N lines each contain a part of the string S.
Constraints
1 <= N <= 30
1 <= len(S) <= 100
Output Format
Print the valid hex color codes in order of their occurrence from the string S, one per line.
Sample Input
4
{#FfFDf2}
{#fd3}
{#FD3}
{#123456789}
Sample Output
#FfFDf2
#fd3
#FD3
Explanation
The first three lines of the input contain valid hex color codes, so we print them.
The fourth line does not contain a valid hex color code because it has more than 6 hexadecimal digits, so we do not print it.
Author: Aquilas DJENONTIN
"""

import re


def hex_color_code():
    """
    A function to find and print all valid hex color codes from the input string.
    Complexity: O(n) since we are iterating through the input string once.
    """
    n = int(input())
    # This pattern matches valid hex color codes that start with a '#' followed by 3 to 6 hexadecimal digits, and are enclosed within curly braces.
    pattern = r"(?i)(#[0-9A-F]{3,6})"
    s = ""
    for _ in range(n):
        s += input()
    # This pattern finds all substrings that are enclosed within curly braces in the input string.
    m = re.findall(r"\{([^}]*)\}", s)
    for x in m:
        p = re.findall(pattern, x)
        for y in p:
            print(y)


# The main function to read input and call the hex_color_code function.
if __name__ == "__main__":
    hex_color_code()

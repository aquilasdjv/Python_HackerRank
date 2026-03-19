# Detect Floating Point Number
# https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""
Docstring for DetectFloatingPointNumber
You are given a string S. Your task is to find out if the string S is a
valid floating point number or not.
Input Format
The first line contains an integer T, the number of test cases.
The next T lines each contain a string S.
Constraints
1 <= T <= 100
1 <= len(S) <= 100
Output Format
Print True if S is a valid floating point number, otherwise print False.
Sample Input
4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output
False
True
True
False
Explanation
The first string 4.0O0 is not a valid floating point number because it contains
the letter O. The second string -1.00 is a valid floating point number because it has a negative sign, followed by digits,
a decimal point and more digits. The third string +4.54 is a valid floating point number because it has a positive sign, followed by digits,
a decimal point and more digits. The fourth string SomeRandomStuff is not a valid floating point number because it contains letters.
Author: Aquilas DJENONTIN
"""

import re

if __name__ == "__main__":
    for _ in range(int(input())):
        m = re.fullmatch(r"^(?![-+]?0(\.0*)?$)[-+]?(?:\d+(\.\d*)?|\.\d+)$", input())
        print(bool(m))

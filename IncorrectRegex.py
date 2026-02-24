# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem
"""
Docstring for IncorrectRegex
You are given a string S. Your task is to find out whether S is a valid regex or not.
Input Format
The first line contains integer T, the number of test cases. The next T lines each contain a string S.
Constraints
1 <= T <= 100
1 <= len(S) <= 100
Output Format
For each test case, print "True" if S is a valid regex. Otherwise, print "False".
Sample Input
2
([A-Z])(.+)([0-9])
batcat
Sample Output
True
False
Explanation
The first test case is a valid regex. The second test case is not a valid regex.
Author: Aquilas DJENONTIN
"""
import re


def incorrect_regex_demo():
    """
    Check if the given string S is a valid regex.
    Complexity: O(n) where n is the length of the string S, since re.compile() may need to parse the entire string.
    """
    for _ in range(int(input())):
        pattern = input()
        try:
            re.compile(pattern)
            print(True)
        except re.error:
            print(False)


# Example usage:
if __name__ == "__main__":
    incorrect_regex_demo()

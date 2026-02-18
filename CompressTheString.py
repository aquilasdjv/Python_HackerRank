# Compress the String!
# https://www.hackerrank.com/challenges/compress-the-string/problem
"""
Docstring for CompressTheString
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
For a better understanding of the problem, check the explanation.
Input Format
A single line of input consisting of the string S.
Constraints
0 < len(S) <= 10^4
Output Format
Output the modified string according to the description in the problem statement.
Sample Input
aaabccdddde
Sample Output
(3, a) (1, b) (2, c) (4, d) (1, e)
Author: Aquilas DJENONTIN
"""
from itertools import groupby


def compress_string(s):
    """
    Compress the string using groupby from itertools.
    :param s: The input string to be compressed.
    :return: A list of compressed string segments in the format (X, c).
    Complexity Analysis:
    Time Complexity: O(n), where n is the length of the input string. We traverse the string once to group the characters and create the compressed output.
    Space Complexity: O(n), in the worst case, if all characters in the string are unique, we will have n groups, and the output list will also contain n elements.
    """
    return [str((len(list(g)), int(x))) for x, g in groupby(s)]

# Example usage:
if __name__ == "__main__":
    s = input()
    result = compress_string(s)
    print(*result, sep=" ")

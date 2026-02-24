# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem
"""
Docstring for CompanyLogo
You are given a string S. Your task is to find the top three most common characters in S. Print the three most common characters along with their occurrence count. Sort in descending order of occurrence count, then in ascending order of ASCII values.
Input Format
A single line of input containing the string S.
Constraints
0 < len(S) <= 10^4
Output Format
Print the three most common characters along with their occurrence count each on a separate line. Sort output
in descending order of occurrence count, then in ascending order of ASCII values.
Sample Input
aabbbccde
Sample Output
b 3
a 2
c 2
Explanation
Here, b occurs 3 times. a and c occur 2 times each. The rest
of the characters occur once each. The three most common characters are b, a, and c. They are printed in descending order of occurrence count. a and c have the same occurrence count, so they are sorted in ascending order of their ASCII values.
Author: Aquilas DJENONTIN
"""
from collections import Counter, defaultdict, OrderedDict


def company_logo(s):
    """Find the top three most common characters in S.
    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count, then in ascending order of ASCII values.
    Complexity: O(n log n) where n is the length of the string S.
    """
    l = Counter(s)
    sorted_l = sorted(l.items(), key=lambda x: (-x[1], x[0]))
    return sorted_l[:3]


def company_logo_v2(s):
    """Find the top three most common characters in S.
    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count, then in ascending order of ASCII values.
    Complexity: O(n log n) where n is the length of the string S.
    """
    l = defaultdict(int)
    for ch in s:
        l[ch] += 1
    sorted_l = sorted(l.items(), key=lambda x: (-x[1], x[0]))
    return sorted_l[:3]


def company_logo_v3(s):
    """Find the top three most common characters in S.
    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count, then in ascending order of ASCII values.
    Complexity: O(n log n) where n is the length of the string S.
    """
    l = OrderedDict()
    for ch in s:
        if ch in l.keys():
            l[ch] += 1
        else:
            l[ch] = 1
    sorted_l = sorted(l.items(), key=lambda x: (-x[1], x[0]))
    return sorted_l[:3]


# Example usage:
if __name__ == "__main__":
    s = input()
    result = company_logo(s)
    for x in result:
        print(f"{x[0]} {x[1]}")

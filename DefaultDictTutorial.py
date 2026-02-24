# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""
Docstring for DefaultDictTutorial
You are given n words. Some words may repeat. For each word, output its index (starting from 1) in the list of words the first time it appears, otherwise print -1.
Input Format
The first line contains an integer n, the number of words. The next n lines each contain a word.
Constraints
1 <= n <= 10^5
1 <= length of each word <= 20
Output Format
Output n lines. The ith line should contain the index of the first occurrence of the ith word in the input list, or -1 if it has appeared before.
Sample Input
5
abc
def
abc
ghi
def
Sample Output
1
2
-1
4
-1
Explanation
The first occurrence of "abc" is at index 1, the first occurrence of "def" is at index 2, and the first occurrence of "ghi" is at index 4. The second occurrences of "abc" and "def" are at indices 3 and 5, respectively, so we print -1 for those.
Author: Aquilas DJENONTIN
"""

from collections import defaultdict


def defaultdict_demo():
    """
    For each word, output its index (starting from 1) in the list of words the first time it appears, otherwise print -1.
    Complexity: O(n) where n is the number of words, since we are iterating through the list of words once.
    """
    n, m = map(int, input().split())

    d = defaultdict(list)
    for i in range(n):
        v = input()
        d[v].append(i + 1)

    for _ in range(m):
        v = input()
        if v in d.keys():
            print(*d[v], sep=" ")
        else:
            print(-1)


# Example usage:
if __name__ == "__main__":
    defaultdict_demo()

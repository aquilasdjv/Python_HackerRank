# Word Order
# https://www.hackerrank.com/challenges/word-order/problem
"""
Docstring for WordOrder
Print the number of distinct words in a list. Also print the number of occurrences for each distinct word according to their appearance in the list.
Input Format
The first line of input contains an integer N, the total number of words. The next N lines each contain a word.
Constraints
1 <= N <= 10^5
The sum of the lengths of all the words do not exceed 10^6.
Output Format
Print the number of distinct words in the list. Then print the number of occurrences for each distinct
word according to their appearance in the list.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
Explanation
There are 3 distinct words. Here, "bcdef" appears twice, and the other two words appear once each.
Author: Aquilas DJENONTIN
"""

from collections import defaultdict


def wordorder():
    """
    Print the number of distinct words in a list. Also print the number of occurrences for each distinct word according to their appearance in the list.
    Complexity: O(n) where n is the number of words.
    """
    n = int(input())
    a = defaultdict(int)
    for _ in range(n):
        userInput = input()
        a[userInput] += 1

    print(len(a.keys()))
    print(*a.values())


# Example usage:
if __name__ == "__main__":
    wordorder()

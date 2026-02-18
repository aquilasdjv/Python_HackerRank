# Iterables and Iterators
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations

"""
Docstring for Iterables and Iterators
In this task, You are given a list of N lowercase English letters. For a given integer k, you can select any k indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.
Input Format :
The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer k, denoting the number of indices to be selected.
Output Format :
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
Note: The answer must be correct up to 3 decimal places.
Constraints
1 <= N <= 10
1 <= k <= N
All the letters in the list are lowercase English letters.
Sample Input
4
a a c d
2
Sample Output
0.8333
Author: Aquilas DJENONTIN
"""


def comb_count(N, k):
    """
    Calculate the probability that at least one selected index contains the letter 'a'.
    
    Parameters:
    N (iterable): An iterable of lowercase English letters
    k (int): The number of indices to be selected
    
    Returns:
    float: The probability that at least one of the k selected indices contains 'a'
    
    Complexity: O(n!/(k!(n-k)!)) for time complexity, where n
    is the length of the input string N and k is the length of the combinations, since we need to generate all possible combinations of length k from n characters.
    """
    T = list(combinations(N, k))
    return len([t for t in T if "a" in t]) / len(T)


# Example usage:
if __name__ == "__main__":
    n = int(input())
    N = map(str, input().split())
    k = int(input())
    result = comb_count(N, k)
    print(result)

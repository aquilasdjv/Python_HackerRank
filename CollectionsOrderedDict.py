# Collections OrderedDict
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""
Docstring for CollectionsOrderedDict
You are given N words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
Input Format
The first line contains the integer N, the number of words. The next N lines each contain a word.
Constraints
1 <= N <= 10^5
The sum of the lengths of all the words do not exceed 10^6.
Output Format
Output N lines. The ith line should contain the number of occurrences of the ith word in the input, followed by a space, followed by the word itself.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
2 bcdef
1 abcdefg
1 bcde
Explanation
There are 3 distinct words. Here, "bcdef" appears twice, and the other two words appear once each.
Author: Aquilas DJENONTIN
"""

from collections import OrderedDict


def orderdict_demo():
    """
    Count the occurrences of each word in the input and print them in the order they first appeared.
    Complexity: O(n) where n is the number of words, since we are iterating through the list of words once.
    """
    n = int(input())
    orderdict = OrderedDict()
    for _ in range(n):
        userInput = input().split()
        if " ".join(userInput[:-1]) in orderdict.keys():
            orderdict[" ".join(userInput[:-1])][0] += 1
        else:
            orderdict[" ".join(userInput[:-1])] = [1, int(userInput[-1])]

    for i, val in orderdict.items():
        print(f"{i} {val[0]*val[1]}")


# Example usage:
if __name__ == "__main__":
    orderdict_demo()

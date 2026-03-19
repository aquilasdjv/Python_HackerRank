# Words Score
# https://www.hackerrank.com/challenges/word-score/problem
"""
Docstring for word_score
You are given a list of words. Each word has a score which is calculated as follows:
- If the word contains no vowels, then the score of the word is 2.
- If the word contains an even number of vowels, then the score of the word is 2.
- If the word contains an odd number of vowels, then the score of the word is 1.
The total score of the list of words is the sum of the scores of each word in the list.
Input Format
The first line contains an integer N, the number of words in the list.
The second line contains N space-separated words.
Constraints
1 <= N <= 100
1 <= length of each word <= 100
Output Format
Print the total score of the list of words.
Sample Input
4
hello world hackerrank python
Sample Output
9
Explanation
The score of "hello" is 1 (2 vowels), the score of "world" is 2 (1 vowel), 
the score of "hackerrank" is 1 (3 vowels), and the score of "python" is 2 (1 vowel). Therefore, the total score is 1 + 2 + 1 + 2 = 6.
Author: Aquilas DJENONTIN
"""

import re


def word_score(words):
    """
    Calculate the total score of a list of words based on the number of vowels in each word.
    Complexity: O(N*M) where N is the number of words and M is the average length of the words, 
    since we are iterating through each word and counting the number of vowels in each word.
    """
    score = 0
    pattern = r"(?i)([aeiouy])"
    for word in words:
        m = re.findall(pattern, word)
        if m:
            score += 2 if len(m) % 2 == 0 else 1
        else:
            score += 2
    return score


def word_score_v2(words):
    """
    Calculate the total score of a list of words based on the number of vowels in each word using a more efficient approach.
    Complexity: O(N*M) where N is the number of words and M is the average length of the words, 
    since we are iterating through each word and counting the number of vowels in each word.
    """
    score = 0
    vowels = set("aeiouyAEIOUY")
    for word in words:
        count = sum(1 for char in word if char in vowels)
        if count == 0:
            score += 2
        elif count % 2 == 0:
            score += 2
        else:
            score += 1
    return score


if __name__ == "__main__":
    words = input("Enter a list of words separated by spaces: ").split()
    print(word_score(words))

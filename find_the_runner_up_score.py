# Find the Runner-Up Score
"""
Docstring for Find_the_Runner-Up_Score
Given the participants' scores, find the score of the runner-up.
Example:
Input:
5
10 20 20 30 40
Output:30
Instructions:
1. Read an integer n from input, the number of scores.
2. Read n space-separated integers representing the scores.
3. Remove duplicates and sort the scores.
4. Print the second highest score.
Author: aquilas DJENONTIN
"""

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    sort_arr = list(set(arr))
    sort_arr.sort()
    print(sort_arr[-2] if len(sort_arr) > 1 else sort_arr[-1])

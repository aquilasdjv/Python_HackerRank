#!/bin/python3
# Athlete Sort
# https://www.hackerrank.com/challenges/python-sort-sort/problem
"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Constraints
2 <= n <= 10
-100 <= A[i] <= 100
Output Format
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Complexity: O(n log n) due to the sorting step, where n is the number of scores. The rest of the operations are O(n) for reading input and finding the runner-up score.
Author: Aquilas DJENONTIN
"""


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr.sort(key=lambda elt: elt[k])
    
    for elt in arr:
        print(*elt)

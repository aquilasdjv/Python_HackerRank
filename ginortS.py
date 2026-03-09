# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem
"""
Given a string S, sort it in the following manner:
1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.
The sorted order is as follows: sorted lowercase letters, sorted uppercase letters, sorted odd digits, sorted even digits.
Input Format
A single line of input containing the string S.
Constraints
0 < len(S) < 1000
Output Format
Output the sorted string S.
Sample Input 0
Sorting1234
Sample Output 0
ginortS1324
Complexity: O(n log n) due to the sorting step, where n is the length of the input string. The rest of the operations are O(n) for iterating through the string and categorizing characters.
Author: Aquilas DJENONTIN
"""


def ginortS():
    """
    Given a string S, sort it in the following manner:
    1. All sorted lowercase letters are ahead of uppercase letters.
    2. All sorted uppercase letters are ahead of digits.
    3. All sorted odd digits are ahead of sorted even digits.
    The sorted order is as follows: sorted lowercase letters, sorted uppercase letters, sorted odd digits, sorted even digits.
    Complexity: O(n log n) due to the sorting step, where n is the length
    of the input string. The rest of the operations are O(n) for iterating through the string and categorizing characters.
    """
    user_input = input()
    alpha = []
    digit = []
    for elt in user_input:
        if elt.isdigit():
            digit.append(int(elt))
        else:
            alpha.append(elt)

    alpha.sort()
    digit.sort()

    low = [x for x in alpha if x.islower()]
    up = [x for x in alpha if x.isupper()]
    odd = [x for x in digit if x % 2 != 0]
    even = [x for x in digit if x % 2 == 0]

    odd.extend(even)
    low.extend(up)
    low.extend(map(str, odd))

    print("".join(low))


# The main function to call the above function.
if __name__ == "__main__":
    ginortS()

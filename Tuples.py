# Tuples.py
"""
Docstring for Tuples
Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
Input Format
The first line contains an integer,n , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.
Output Format
Print the result of hash(t).
Example:
Input:
2
1 2
Output:
3713081631934410656
Authored by: Aquilas DJENONTIN
"""

if __name__ == "__main__":
    # n = int(raw_input())
    # integer_list = map(int, raw_input().split())
    # is what python 2 used to have the correct output for this challenge.
    # But for python 3, we use input() instead of raw_input() as below:
    # The result change because of the different hash function between python 2 and 3.
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# Collections deque
# https://www.hackerrank.com/challenges/py-collections-deque/problem
"""
Docstring for CollectionsDeque
Deque is a double-ended queue that allows you to add and remove elements from both ends efficiently.
It is part of the collections module in Python. The deque class provides methods for adding and removing elements from both ends of the queue,
making it a versatile data structure for various applications.
In this challenge, you will be given a series of commands to manipulate a deque.
The commands can be one of the following:
- append x: Add x to the right end of the deque.
- appendleft x: Add x to the left end of the deque.
- pop: Remove and return an element from the right end of the deque.
- popleft: Remove and return an element from the left end of the deque.
After processing all the commands, you need to print the final state of the deque.
A sample input and output is provided below for better understanding.
Sample Input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output:
2 3
In this example, we start with an empty deque. We append 1, 2, and 3 to the right end, resulting in the deque [1, 2, 3]. Then we append 4 to the left end, making it [4, 1, 2, 3].
Next, we pop an element from the right end, which removes 3, leaving us with [4, 1, 2]. Finally, we popleft an element from the left end, which removes 4, resulting in the final deque [1, 2]. We then print the elements of the deque separated by a space.
Author: Aquilas DJENONTIN
"""
from collections import deque


def deque_demo():
    """Demonstrates the use of deque to process a series of commands."""
    n = int(input())
    l = deque()
    for _ in range(n):
        userInput = input().split()
        fun, val = (
            (userInput[0], userInput[1]) if len(userInput) > 1 else (userInput[0], 0)
        )
        if fun == "append":
            l.append(int(val))
        elif fun == "appendleft":
            l.appendleft(int(val))
        elif fun == "pop":
            l.pop()
        elif fun == "popleft":
            l.popleft()

    print(*l)


# Example usage:
if __name__ == "__main__":
    deque_demo()

# Lists.py
"""
Docstring for Lists Module
This script performs a series of list operations based on user input.
Each operation modifies the list accordingly, and the final state of the list can be printed.
Example usage:
Input:
12
append 1
append 2
insert 3 0
print
Output:
[0, 1, 2, 3]
Author: Aquilas DJENONTIN
"""
if __name__ == "__main__":
    N = int(input())
    a = []
    for _ in range(N):
        userInput = input()
        if "append" in userInput:
            a.append(int(userInput.split()[1]))
        elif "insert" in userInput:
            a.insert(int(userInput.split()[1]), int(userInput.split()[2]))
        elif "remove" in userInput:
            a.remove(int(userInput.split()[1]))
        elif "sort" in userInput:
            a.sort()
        elif "pop" in userInput:
            a.pop()
        elif "reverse" in userInput:
            a.reverse()
        elif "print" in userInput:
            print(a)

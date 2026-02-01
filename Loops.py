# Loops.py
"""
Docstring for Module demonstrating various loop constructs in Python.
: This script showcases the use of for loops, while loops.
The script takes an integer input and performs iterations based on that input.
printing the square of the iteration variable in each loop.
@author aquilas djenontin
"""

if __name__ == "__main__":
    n = int(input().strip())
    # For loop example
    print("For Loop:")
    for i in range(n):
        print(f"Iteration {i**2}")

    # While loop example
    print("\nWhile Loop:")
    count = 0
    while count < n:
        print(f"Count is {count**2}")
        count += 1

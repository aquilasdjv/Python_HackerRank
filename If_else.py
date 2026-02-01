# If_else.py
"""
Docstring for If_else
: This script reads an integer from input and prints "Weird" or "Not Weird"
    based on specific conditions.
@author aquilas djenontin
"""

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")

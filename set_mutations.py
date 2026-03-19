# Set Mutations
"""
Docstring for SetMutations
This module defines a main block of code that reads input from the user to perform set mutations on a set s. The input format is as follows:
- The first line contains an integer n, the number of elements in set s.
- The second line contains n space-separated integers, the elements of set s.
- The third line contains an integer m, the number of operations to perform on set s.
- The next m lines contain the operations to perform on set s. Each operation consists of a command followed by a set of integers. The commands can be one of the following:
  - 'intersection_update': Updates set s to be the intersection of s and the provided set.
  - 'update': Updates set s to be the union of s and the provided set.
  - 'symmetric_difference_update': Updates set s to be the symmetric difference of s and the provided set.
  - 'difference_update': Updates set s to be the difference of s and the provided set.
After performing all the operations, the code calculates the sum of the elements in set s and prints the result.
Author: Aquilas DJENONTIN
"""

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        user_input = input()
        s2 = set(map(int, input().split()))
        if "intersection_update" == user_input.split()[0]:
            s.intersection_update(s2)
        elif "update" == user_input.split()[0]:
            s.update(s2)
        elif "symmetric_difference_update" == user_input.split()[0]:
            s.symmetric_difference_update(s2)
        elif "difference_update" == user_input.split()[0]:
            s.difference_update(s2)

    print(sum(s))

# Collections Counter
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def count_shoes():
    x = int(input())
    sizes = Counter(map(int, input().split()))
    n = int(input())
    N = 0
    for _ in range(n):
        size, customer = map(int, input().split())
        if size in sizes.keys() and sizes[size] > 0:
            N += int(customer)
            sizes[size] -= 1
            
    print(N)

# Example usage:
if __name__ == "__main__":
    count_shoes()
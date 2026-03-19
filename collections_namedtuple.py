# Collections namedtuple
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple


def namedtuple_demo():
    n = int(input())
    Student = namedtuple("Student", input())
    print(
        round(
            sum([int(x.MARKS) for x in [Student(*input().split()) for i in range(n)]])
            / n,
            2,
        )
    )


# Example usage:
if __name__ == "__main__":
    namedtuple_demo()

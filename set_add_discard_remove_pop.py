# SetAddDiscardRemovePop.py
"""
Docstring for SetAddDiscardRemovePop
This script contains functions to demonstrate the use of set operations in Python,
specifically adding elements to a set, discarding elements from a set,
removing elements from a set, and popping elements from a set.
The `setAdd()` function reads an integer `n` from the user, then reads `n` country names and adds them to a set. It finally prints the number of unique country names in the set.
The `setDiscard(s, k)` function takes a set `s` and an element `k`, discards `k` from the set `s` if it is present, and returns the modified set.
The `setRemove(s, k)` function takes a set `s` and an element `k`, removes `k` from the set `s` if it is present, and returns the modified set. If `k` is not present in the set, it raises a `KeyError`.
The `setPop(s)` function takes a set `s`, pops an arbitrary element from the set, and returns the modified set. If the set is empty, it raises a `KeyError`.
Author: Aquilas DJENONTIN
"""


def setAdd():
    """
    Docstring for setAdd
    This function reads an integer `n` from the user, then reads `n` country names and adds them to a set. It finally prints the number of unique country names in the set.
    The function first initializes an empty set called `country`. It then iterates `n`
    times, reading a country name from the user and adding it to the `country` set. Since sets do not allow duplicate elements, only unique country names will be stored in the set.
    After all country names have been added to the set, the function prints the length of the `country` set, which represents the number of unique country names entered by the user.

    """
    n = int(input())
    country = set()
    for _ in range(n):
        country.add(input())

    print(len(country))


def setDiscard(s, k):
    """
    Docstring for setDiscard
    This function takes a set `s` and an element `k`, discards `k` from the set `s` if it is present, and returns the modified set.
    The `discard()` method of a set removes the specified element from the set if it is
    present. If the element is not present in the set, the `discard()` method does nothing
    and does not raise an error. This makes it a safe way to remove elements from a set without worrying about whether the element exists in the set or not.
    """
    s.discard(k)
    return s


def setRemove(s, k):
    """
    Docstring for setRemove
    This function takes a set `s` and an element `k`, removes `k` from the set `s` if it is present, and returns the modified set. If `k` is not present in the set, it raises a `KeyError`.
    The `remove()` method of a set removes the specified element from the set if it is
    present. If the element is not present in the set, the `remove()` method raises a `KeyError`.
    This means that you need to be sure that the element you want to remove is actually in the set before calling the `remove()` method, otherwise your program may crash with an error.
    """
    s.remove(k)
    return s


def setPop(s):
    """
    Docstring for setPop
    This function takes a set `s`, pops an arbitrary element from the set, and returns the modified set. If the set is empty, it raises a `KeyError`.
    The `pop()` method of a set removes and returns an arbitrary element from the set. If the set is empty, it raises a `KeyError`.
    This method is useful when you want to remove an element from a set but do not care which element is removed. However,
    since the element removed is arbitrary, you should not rely on the order of elements in the set when using the `pop()` method.
    """
    s.pop()
    return s


if __name__ == "__main__":
    setAdd()
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        userInput = input()
        if "pop" in userInput:
            s = setPop(s)
        elif "remove" in userInput:
            s = setRemove(s, int(userInput.split()[1]))
        elif "discard" in userInput:
            s = setDiscard(s, int(userInput.split()[1]))
    print(sum(s))

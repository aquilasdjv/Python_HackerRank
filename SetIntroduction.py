# SetIntroduction.py
"""
Docstring for SetIntroduction
This module contains functions to calculate the average of unique elements in a list. It demonstrates the use
of sets to remove duplicates and calculate the average. The module includes two functions, average and average1, 
which perform the same calculation using different approaches. The code also includes a test case to demonstrate the functionality of the average function.
Authors: Aquilas DJENONTIN
"""


def average(array):
    """
    Docstring for average function
    This function takes an array as input, removes duplicates by converting it to a set, and calculates the average of the unique elements. It returns the average value.
    Parameters:
    array (list): A list of numbers from which the average of unique elements will be calculated.
    Returns:
    float: The average of the unique elements in the input array.
    Complexity: O(n) where n is the number of elements in the input array, due to the conversion to a set and the iteration to calculate the total sum.
    """
    l = set(array)
    total = 0
    for n in l:
        total += n
    return total / len(l)


def average1(array):
    """
    Docstring for average1 function
    This function takes an array as input, removes duplicates by converting it to a set, and calculates the average of the unique elements using a more concise approach. It returns the average value.
    Parameters:
    array (list): A list of numbers from which the average of unique elements will be calculated
    Returns:
    float: The average of the unique elements in the input array.
    Complexity: O(n) where n is the number of elements in the input array, due to the conversion to a set and the iteration to calculate the total sum.
    """
    l = set(array)
    return sum(l) / len(l)


# The following code is for testing the average function. It reads input from the user, processes it, and prints the result.
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

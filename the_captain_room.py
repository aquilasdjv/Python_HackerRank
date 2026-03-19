# The captain's room
"""
Docstring for TheCaptainRoom
This module defines a main block of code that reads input from the user to find the captain's room number. The input format is as follows:
- The first line contains an integer k, the size of each group of tourists.
- The second line contains space-separated integers representing the room numbers of the tourists, where each room number appears k times except for the captain's room number which appears only once.
The code uses a set to keep track of the unique room numbers and a variable to keep track of the sum of the room numbers. It iterates through the list of room numbers, adding each number to the set and updating the sum. Finally, it calculates the captain's room number using the formula: (sum of unique room numbers * k - sum of all room numbers) // (k - 1) and prints the result.
Author: Aquilas DJENONTIN
"""


def captain_room(k, room_numbers):
    """
    Returns the captain's room number given the size of each group of tourists and a list of room numbers.
    complexity: O(n) where n is the number of room numbers in the input list.
    """
    unique_rooms = set()
    sum_of_rooms = 0

    for room in room_numbers:
        unique_rooms.add(room)
        sum_of_rooms += room

    captain_room = (sum(unique_rooms) * k - sum_of_rooms) // (k - 1)
    return captain_room


def captain_room_v2(k, room_numbers):
    """
    Docstring for captain_room_v2
    This function is an optimized version of the captain_room function.
    It uses a set to store unique room numbers and calculates the sum of all room numbers in a single pass through the list.
    The complexity of this function is O(n) where n is the number of room numbers in the input list.
    """
    unique_rooms = set(room_numbers)
    sum_of_rooms = sum(room_numbers)

    captain_room = (sum(unique_rooms) * k - sum_of_rooms) // (k - 1)
    return captain_room


if __name__ == "__main__":
    k = int(input())
    room_numbers = list(map(int, input().split()))
    print(captain_room(k, room_numbers))

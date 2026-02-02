# Mutations.py
"""
Docstring for Mutations
This module contains a function to mutate a string by replacing a character at a specified index.
Function: mutate_string
Parameters:
    string (str): The original string to be mutated.
    position (int): The index of the character to be replaced.
    character (str): The new character to insert at the specified index.
Returns:
    str: The mutated string with the character replaced.
Authors:
    Aquilas DJENONTIN
"""


def mutate_string(string, position, character):
    """
    Docstring for mutate_string
    :param string: The original string to be mutated.
    :param position: The index of the character to be replaced.
    :param character: The new character to insert at the specified index.
    :return: The mutated string with the character replaced.
    This function replaces a character at a specified index in a string with a new character.
    """
    # Convert the string to a list to allow mutation
    string_list = list(string)
    # Replace the character at the specified position
    string_list[position] = character
    # Join the list back into a string
    mutated_string = "".join(string_list)
    return mutated_string


# Example usage
if __name__ == "__main__":
    s = input("Enter the original string: ")
    i, c = input("Enter the position and new character (separated by space): ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)  # Output the mutated string

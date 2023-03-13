#!/usr/bin/python3

"""
This module contains a function replace_in_list that replaces an element
in a list at a specific position.
"""


def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element (int): The new element to replace with.

    Returns:
        The modified list if idx is within the range of the list,
        otherwise the original list.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list

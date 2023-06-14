"""
This exercise stub and the test suite contain several enumerated constants.

For this challenge, enumerated constants are written as a NAME assigned to an 
arbitrary, but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def sublist(list_one, list_two):
    one = str(list_one)[1:-1]
    two = str(list_two)[1:-1]
    if one == two:
        return EQUAL
    elif one in two:
        return SUBLIST
    elif two in one:
        return SUPERLIST
    else:
        return UNEQUAL
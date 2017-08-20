"""
#1 out of 6
"""


def delete_digit(n):
    """
    Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
    """
    max = -1
    str_n = str(n)
    for idx, dig in enumerate(str_n):
        num = int(str_n[:idx] + str_n[idx+1:])
        if num > max:
            max = num
    return max


def integer_to_sting_of_fixed_width(number, width):
    """
    Given a positive integer number and a certain length, we need to modify the given number to have a specified length.
    We are allowed to do that either by cutting out leading digits (if the number needs to be shortened)
        or by adding 0s in front of the original number.
    """
    str_n = str(number)
    if width < len(str_n):
        return str_n[len(str_n)-width:]
    elif width > len(str_n):
        return ('0' * (width - len(str_n))) + str_n
    return str_n


def array_maximal_adjacent_difference(inputArray):
    """ Given an array of integers, find the maximal absolute difference between any two of its adjacent elements. """
    max = -1
    for i in range(1, len(inputArray)):
        result = abs(inputArray[i] - inputArray[i-1])
        if result > max:
            max = result

    return max

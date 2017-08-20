"""
#1/6
"""


def sumOfSquares(n):
    return sum(x**2 for x in range(1, n+1))


def ballsDistribution(colors, ballsPerColor, boxSize):
    """
    You have a set of balls that are colored in such a way that there is ballsPerColor balls of each of the given number of colors. You also have an infinite number of boxes of the same max capacity boxSize.

    You distribute the balls among the boxes as follows:

    first you fill up the first box, then the second, etc.
    first you use all of the balls of the first color, then all of the balls of the second color, etc.
    Find the number of colors for which there is more than one box that contains a ball of that color.
    """
    box_size = boxSize
    cls = 0
    for color in range(colors):
        if box_size == 0:
            box_size = boxSize
        if ballsPerColor > box_size:
            balls = ballsPerColor - box_size
            box_size = balls % boxSize if balls > boxSize else boxSize % balls
            cls += 1
        elif ballsPerColor < box_size:
            box_size -= ballsPerColor
        else:
            box_size = boxSize
    return cls


def swap_case(text):
    """
    Change the capitalization of all letters in a given string.
    """
    return ''.join(tx.lower() if tx.isupper() else tx.upper() for tx in text)

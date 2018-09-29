# shapes.py
# module
"""A collection of funcitons for Printing basic shapes."""
CHAR = '*'
def rectangle(height, width):
    """ Prints a rectangle. """
    for row in range(height):
        for col in range(width):
            print(CHAR, end='')
        print()

def square(side):
    """ Prints a square. """
    rectangle(side,side)

def triangle(height):
    """ Prints a right triangle. """
    for row in range(height):
        for col in range(1, row+2):
            print(CHAR, end='')
        print()
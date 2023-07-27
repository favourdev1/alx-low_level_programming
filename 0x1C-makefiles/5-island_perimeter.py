#!/usr/bin/python3
"""
This module contains a function that returns
the perimeter of the island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island
    """
    if not grid:
        return (0)

    r = 0
    """ horizontal scanning """
    for line in grid:
        """ left to right scanning """
        for cell in line:
            if cell == 1:
                r += 1
                break

        """ right to left scanning """
        for cell in line[::-1]:
            if cell == 1:
                r += 1
                break

    """ vertical scanning """
    for x in range(len(grid[0])):
        """ top to bottom scanning """
        for line in grid:
            if line[x] == 1:
                r += 1
                break

        """ bottom to top scanning """
        for line in grid[::-1]:
            if line[x] == 1:
                r += 1
                break

    return (r)

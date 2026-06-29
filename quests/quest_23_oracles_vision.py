#!/usr/bin/env python3
"""Quest 23: The Oracle's Vision - functions that return a value."""


def calculate_area(length, width):
    """Compute and return the area of a rectangle, instead of printing it."""
    return length * width


# Because the function returns a value, we can store it in a variable
# and use it however we like (print it, do more math with it, etc.).
area_one = calculate_area(5, 3)
area_two = calculate_area(10, 2)

print(f"The first rectangle has an area of {area_one}.")
print(f"The second rectangle has an area of {area_two}.")

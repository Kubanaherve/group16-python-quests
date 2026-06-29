#!/usr/bin/env python3
"""Quest 21: The Reusable Incantation - defining a function with def."""


def greet_adventurer():
    """Print a welcome message. Defined once, callable many times."""
    print("Welcome, adventurer! May fortune favor your code.")


# Calling the function three times reuses the same code without copy-pasting it.
greet_adventurer()
greet_adventurer()
greet_adventurer()

#!/usr/bin/env python3
"""Quest 24: The Master Spell - calling a function from inside another."""


def ask_for_age():
    """Ask the user for their age and return it as an integer."""
    age = int(input("How old are you? "))
    return age


def can_they_vote(age):
    """Print whether someone of this age can vote."""
    if age >= 18:
        print("You can vote!")
    else:
        print("You cannot vote yet.")


# We break the problem into two small functions, then chain them together:
# the result of one becomes the input to the next.
user_age = ask_for_age()
can_they_vote(user_age)

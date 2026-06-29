#!/usr/bin/env python3
"""Quest 22: The Personalized Scroll - functions with parameters."""


def personalized_greeting(name, quest):
    """Greet the user using the name and quest passed in as arguments."""
    print(f"Greetings, {name}! Your quest, '{quest}', has been recorded.")


user_name = input("What is your name? ")
user_quest = input("What is your quest? ")

# The values we collected are passed into the function as arguments,
# which fill the `name` and `quest` parameters.
personalized_greeting(user_name, user_quest)

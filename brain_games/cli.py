"""Cli."""

import prompt


def welcome_user():
    """Run game."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))

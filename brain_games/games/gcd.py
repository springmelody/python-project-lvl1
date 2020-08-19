"""Brain gcd game functions."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_value, second_value):
    """Return GCD of two numbers."""
    if second_value > 0:
        return get_gcd(second_value, first_value % second_value)
    return abs(first_value)


def get_game_data():
    """Get the game data."""
    first_value = randint(1, 100)
    second_value = randint(1, 100)
    question = f'{first_value} {second_value}'
    correct_answer = str(get_gcd(first_value, second_value))
    return question, correct_answer

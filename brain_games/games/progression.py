"""Brain progression game functions."""

from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def make_progression(initial_value, difference, length=LENGTH_PROGRESSION):
    """Make arithmetic progression."""
    maximum_value = (difference * length) + initial_value
    return range(initial_value, maximum_value, difference)


def get_game_data():
    """Get the game data."""
    progression = list(make_progression(randint(1, 100), randint(1, 5)))
    hidden_item_index = progression.index(choice(progression))
    correct_answer = str(progression[hidden_item_index])
    progression[hidden_item_index] = '..'
    question = ' '.join(list(map(str, progression)))
    return question, correct_answer

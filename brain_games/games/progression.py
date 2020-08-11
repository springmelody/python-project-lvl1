"""Brain progression game functions."""

from random import choice, randint

from brain_games.engine import play_game

DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def make_progression(length):
    """Make arithmetic progression."""
    initial_value = randint(1, 100)
    difference = randint(1, 5)
    maximum_value = (difference * length) + initial_value
    return range(initial_value, maximum_value, difference)


def get_game_data():
    """Get the game data."""
    progression = list(make_progression(LENGTH_PROGRESSION))
    hidden_item_index = progression.index(choice(progression))
    correct_answer = str(progression[hidden_item_index])
    progression[hidden_item_index] = '..'
    question = ' '.join(list(map(str, progression)))
    return question, correct_answer


def start_game():
    """Get the game data."""
    play_game(DESCRIPTION, get_game_data)

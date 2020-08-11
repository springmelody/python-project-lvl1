"""Brain even game functions."""

from random import randint

from brain_games.engine import play_game

DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'"


def is_even(number):
    """Check the evenness of the number."""
    return number % 2 == 0


def get_game_data():
    """Get the game data."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def start_game():
    """Start the game."""
    play_game(DESCRIPTION, get_game_data)

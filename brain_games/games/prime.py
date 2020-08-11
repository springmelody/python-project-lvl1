"""Brain prime game functions."""

from random import randint

from brain_games.engine import play_game

DESCRIPTION = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(number):
    """Check the number prime or not."""
    if number < 2:
        return False
    count = 2
    while count <= number // 2:
        if number % count == 0:
            return False
    return True


def get_game_data():
    """Get the game data."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def start_game():
    """Start the game."""
    play_game(DESCRIPTION, get_game_data)

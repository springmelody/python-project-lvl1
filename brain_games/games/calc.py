"""Brain calc game functions."""

import operator
from random import choice, randint

from brain_games.engine import play_game

DESCRIPTION = 'What is the result of the expression?'
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_operations():
    """Generate operation."""
    return choice(list(operations.keys()))


def correct_answer(first_operand, operation, second_operand):
    """Return correct answer."""
    return str(operations[operation](first_operand, second_operand))


def get_game_data():
    """Get the game data."""
    first_operand = randint(1, 20)
    second_operand = randint(1, 20)
    operation = generate_operations()
    question = f'{first_operand} {operation} {second_operand}'
    answer = correct_answer(first_operand, operation, second_operand)
    return question, answer


def start_game():
    """Start the game."""
    play_game(DESCRIPTION, get_game_data)

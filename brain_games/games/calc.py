"""Brain calc game functions."""

import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_operation():
    """Generate operation."""
    return choice(list(operations.keys()))


def get_correct_answer(first_operand, operation, second_operand):
    """Return correct answer."""
    return str(operations[operation](first_operand, second_operand))


def get_game_data():
    """Get the game data."""
    first_operand = randint(1, 20)
    second_operand = randint(1, 20)
    operation = generate_operation()
    question = f'{first_operand} {operation} {second_operand}'
    answer = get_correct_answer(first_operand, operation, second_operand)
    return question, answer

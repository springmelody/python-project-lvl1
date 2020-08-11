"""Engine game."""
import prompt

round_count = 3


def play_game(description, get_game_data):
    """Game engine logic."""
    print('Welcome to the Brain Games!')
    print(f'{description}\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    counter = 0
    while counter < round_count:
        question, correct_answer = get_game_data()
        print(f'Question: {question} ')
        player_answer = prompt.string('Your answer ')
        if correct_answer == player_answer:
            print('\nCorrect!\n')
            counter += 1
        else:
            print(f'\n{player_answer} is wrong answer ;(.')
            print(f"Correct answer was {correct_answer}. Let\'s try again!")
            return

    print(f'Congratulations, {name}')

"""Brain-even game."""

from brain_games.generator import generate_number

GAME_RULES = (
    'Answer "yes" if a number is even, otherwise answer "no".'
)


def get_correct_answer():
    number = generate_number()
    question = '{0}'.format(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0

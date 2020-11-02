"""Brain-even game."""

from secrets import randbelow

GAME_RULES = (
    'Answer "yes" if a number is even, otherwise answer "no".'
)


def is_even(number):
    return number % 2 == 0


def get_correct_answer():
    random_number = randbelow(100)
    question = 'Question: {0}'.format(random_number)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer

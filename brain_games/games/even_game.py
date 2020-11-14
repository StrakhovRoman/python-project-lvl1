"""Brain-even game."""

import random

GAME_RULES = (
    'Answer "yes" if a number is even, otherwise answer "no".'
)

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(number) else 'no'
    return number, answer


def is_even(number):
    return number % 2 == 0

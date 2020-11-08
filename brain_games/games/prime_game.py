"""Brain-prime game."""

import math
import random

GAME_RULES = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_correct_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, int(math.sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True

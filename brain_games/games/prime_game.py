"""Brain-prime game."""

from secrets import randbelow

GAME_RULES = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


def get_correct_answer():
    random_number = randbelow(100)
    question = 'Question: {0}'.format(random_number)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer

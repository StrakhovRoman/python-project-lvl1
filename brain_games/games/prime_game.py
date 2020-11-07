"""Brain-prime game."""

from brain_games.generator import generate_number

GAME_RULES = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def get_correct_answer():
    number = generate_number()
    question = '{0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True

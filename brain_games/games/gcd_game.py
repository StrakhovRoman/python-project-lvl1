"""Brain-gcd game."""

from brain_games.generator import generate_number

GAME_RULES = (
    'Find the greatest common divisor of given numbers.'
)


def get_correct_answer():
    number1 = generate_number()
    number2 = generate_number()
    question = '{0} {1}'.format(number1, number2)
    correct_answer = find_greatest_common_divisor(number1, number2)
    return question, str(correct_answer)


def find_greatest_common_divisor(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2

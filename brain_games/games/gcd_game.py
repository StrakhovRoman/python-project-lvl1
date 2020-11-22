"""Brain-gcd game."""

import random

DESCRIPTION = (
    'Find the greatest common divisor of given numbers.'
)

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{0} {1}'.format(number1, number2)
    answer = find_greatest_common_divisor(number1, number2)
    return question, str(answer)


def find_greatest_common_divisor(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2

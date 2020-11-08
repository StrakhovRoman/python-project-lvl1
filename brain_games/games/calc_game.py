"""Brain-calc game."""

import operator
import random

GAME_RULES = (
    'What is the result of the expression?'
)


MIN_NUMBER = 1
MAX_NUMBER = 100

operations = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
}


def get_correct_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign, answer = calculate_expression(number1, number2)
    question = '{0} {1} {2}'.format(number1, sign, number2)
    return question, str(answer)


def calculate_expression(num1, num2):
    sign = random.choice(('-', '+', '*'))
    return sign, operations.get(sign)(num1, num2)

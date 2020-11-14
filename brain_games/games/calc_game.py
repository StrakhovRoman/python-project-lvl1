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


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer, math_operator = get_math_operation_and_operator(number1, number2)
    question = '{0} {1} {2}'.format(number1, math_operator, number2)
    return question, str(answer)


def get_math_operation_and_operator(num1, num2):
    math_operator = random.choice(tuple(operations.keys()))
    return operations.get(math_operator)(num1, num2), math_operator

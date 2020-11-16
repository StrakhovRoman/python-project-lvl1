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
    math_operator, math_operation = get_math_operation()
    question = '{0} {1} {2}'.format(number1, math_operator, number2)
    return question, str(math_operation(number1, number2))


def get_math_operation():
    return random.choice(tuple(operations.items()))

"""Brain-calc game."""

from operator import add, mul, sub
from secrets import choice, randbelow

GAME_RULES = (
    'What is the result of the expression?'
)


def calculate_expression(operator, num1, num2):
    operations = {
        '-': sub(num1, num2),
        '+': add(num1, num2),
        '*': mul(num1, num2),
    }
    return operations.get(operator)


def get_correct_answer():
    number1 = randbelow(60)
    number2 = number1 // 2
    operator = choice(('-', '+', '*'))
    question = 'Question: {0} {1} {2}'.format(number1, operator, number2)
    correct_answer = calculate_expression(operator, number1, number2)
    return question, str(correct_answer)

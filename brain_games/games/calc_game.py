"""Brain-calc game."""

from operator import add, mul, sub

from brain_games.generator import generate_number, generate_operator

GAME_RULES = (
    'What is the result of the expression?'
)


operations = {
    '-': sub,
    '+': add,
    '*': mul,
}


def get_correct_answer():
    number1 = generate_number()
    number2 = generate_number()
    operator = generate_operator(('-', '+', '*'))
    question = '{0} {1} {2}'.format(number1, operator, number2)
    correct_answer = calculate_expression(operator, number1, number2)
    return question, str(correct_answer)


def calculate_expression(operator, num1, num2):
    return operations.get(operator)(num1, num2)

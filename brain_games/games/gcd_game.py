"""Brain-gcd game."""

from secrets import randbelow

GAME_RULES = (
    'Find the greatest common divisor of given numbers.'
)


def find_greatest_common_divisor(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def get_correct_answer():
    number1 = randbelow(60)
    number2 = number1 // 2
    question = 'Question: {0} {1}'.format(number1, number2)
    correct_answer = find_greatest_common_divisor(number1, number2)
    return question, str(correct_answer)

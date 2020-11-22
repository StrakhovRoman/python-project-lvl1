"""Brain-progression game."""

import random

DESCRIPTION = (
    'What number is missing in the progression?'
)

MIN_NUMBER = 0
MIN_STEP = 2
MAX_STEP = 4
MAX_PROGRESSION_START_NUMBER = 50
PROGRESSION_LENGTH = 10


def get_question_and_answer():
    start = random.randint(MIN_NUMBER, MAX_PROGRESSION_START_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    removed_index = random.randint(0, len(progression) - 1)
    removed_number = progression[removed_index]
    progression[removed_index] = '..'
    return ' '.join(progression), removed_number


def get_progression(start, step, length):
    stop = start + (length * step)
    return list(map(str, range(start, stop, step)))

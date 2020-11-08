"""Brain-progression game."""

import random

GAME_RULES = (
    'What number is missing in the progression?'
)

MIN_NUMBER = 0
STEP_VALUES = (2, 3, 4)
PROGRESSION_LENGTH = 10
MAX_PROGRESSION_START_NUMBER = 50
MAX_PROGRESSION_INDEX = 9


def get_correct_answer():
    progression = get_progression()
    remove_index = random.randint(MIN_NUMBER, MAX_PROGRESSION_INDEX)
    remove_number = progression[remove_index]
    progression[remove_index] = '..'
    question = ' '.join(progression)
    return question, remove_number


def get_progression():
    step = random.choice(STEP_VALUES)
    start = random.randint(MIN_NUMBER, MAX_PROGRESSION_START_NUMBER)
    stop = start + (PROGRESSION_LENGTH * step)
    return list(map(str, range(start, stop, step)))

"""Brain-progression game."""

import random

GAME_RULES = (
    'What number is missing in the progression?'
)

MIN_NUMBER = 0
PROGRESSION_LENGTH = 10
MIN_STEP = 2
MAX_STEP = 4
MAX_PROGRESSION_START_NUMBER = 50
MAX_PROGRESSION_INDEX = PROGRESSION_LENGTH - 1


def get_question_and_answer():
    progression = get_progression()
    remove_index = random.randint(MIN_NUMBER, MAX_PROGRESSION_INDEX)
    remove_number = progression[remove_index]
    progression[remove_index] = '..'
    question = ' '.join(progression)
    return question, remove_number


def get_progression():
    step = random.randint(MIN_STEP, MAX_STEP)
    start = random.randint(MIN_NUMBER, MAX_PROGRESSION_START_NUMBER)
    stop = start + (PROGRESSION_LENGTH * step)
    return list(map(str, range(start, stop, step)))

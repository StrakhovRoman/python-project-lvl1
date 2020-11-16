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


def get_question_and_answer():
    progression = list(map(str, get_progression()))
    max_progression_index = len(progression) - 1
    removed_index = random.randint(MIN_NUMBER, max_progression_index)
    removed_number = progression[removed_index]
    progression[removed_index] = '..'
    question = ' '.join(progression)
    return question, removed_number


def get_progression():
    step = random.randint(MIN_STEP, MAX_STEP)
    start = random.randint(MIN_NUMBER, MAX_PROGRESSION_START_NUMBER)
    stop = start + (PROGRESSION_LENGTH * step)
    return range(start, stop, step)

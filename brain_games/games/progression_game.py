"""Brain-progression game."""

from brain_games.generator import generate_number

GAME_RULES = (
    'What number is missing in the progression?'
)

PROGRESSION_MAX_NUMBER = 50
PROGRESSION_MAX_INDEX = 9


def get_progression():
    step = generate_number(min_number=2, max_number=4)
    start = generate_number(max_number=PROGRESSION_MAX_NUMBER)
    stop = start + (10 * step)
    return list(map(str, range(start, stop, step)))


def get_correct_answer():
    progression = get_progression()
    remove_index = generate_number(max_number=PROGRESSION_MAX_INDEX)
    remove_number = progression.pop(remove_index)
    progression.insert(remove_index, '..')
    question = '{0}'.format(' '.join(progression))
    return question, remove_number

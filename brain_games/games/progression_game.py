"""Brain-progression game."""

from secrets import choice, randbelow

GAME_RULES = (
    'What number is missing in the progression?'
)


def get_progression():
    step = choice((2, 3, 4))
    start = randbelow(60)
    stop = start + (10 * step)
    return list(map(str, range(start, stop, step)))


def get_correct_answer():
    progression = get_progression()
    rmove_index = randbelow(10)
    rmove_number = progression.pop(rmove_index)
    progression.insert(rmove_index, '..')
    question = 'Question: {0}'.format(' '.join(progression))

    return question, rmove_number

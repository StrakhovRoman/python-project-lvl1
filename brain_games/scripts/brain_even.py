#!/usr/bin/env python

"""Brain-even game script."""

from brain_games.game_engine import run_game
from brain_games.games.even_game import GAME_RULES, get_question_and_answer


def main():
    run_game(GAME_RULES, get_question_and_answer)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""Brain-even game script."""

from brain_games.game_engine import play
from brain_games.games.even_game import GAME_RULES, get_correct_answer


def main():
    play(GAME_RULES, get_correct_answer)


if __name__ == '__main__':
    main()

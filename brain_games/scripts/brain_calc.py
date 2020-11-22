#!/usr/bin/env python

"""Brain-calc game script."""

from brain_games.game_engine import run
from brain_games.games import calc_game


def main():
    run(calc_game)


if __name__ == '__main__':
    main()

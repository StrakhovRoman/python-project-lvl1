#!/usr/bin/env python

"""Brain-even game script."""

from brain_games.game_engine import run
from brain_games.games import even_game


def main():
    run(even_game)


if __name__ == '__main__':
    main()

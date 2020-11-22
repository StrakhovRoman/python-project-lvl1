#!/usr/bin/env python

"""Brain-gcd game script."""

from brain_games.game_engine import run
from brain_games.games import gcd_game


def main():
    run(gcd_game)


if __name__ == '__main__':
    main()

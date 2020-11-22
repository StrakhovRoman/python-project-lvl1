#!/usr/bin/env python

"""Brain-prime game script."""

from brain_games.game_engine import run
from brain_games.games import prime_game


def main():
    run(prime_game)


if __name__ == '__main__':
    main()

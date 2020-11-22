#!/usr/bin/env python

"""Brain-progression game script."""

from brain_games.game_engine import run
from brain_games.games import progression


def main():
    run(progression)


if __name__ == '__main__':
    main()

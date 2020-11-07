"""Random integer number and arithmetic operation generator."""

import random


def generate_number(min_number=0, max_number=100):
    return random.randint(min_number, max_number)


def generate_operator(sequence):
    return random.choice(sequence)

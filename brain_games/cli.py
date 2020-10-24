"""Brain games сommand line interface."""

import prompt


def welcome_user():
    """Username prompt, user greet."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name.capitalize()))  # noqa: WPS421

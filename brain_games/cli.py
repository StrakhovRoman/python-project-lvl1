"""Brain-games сommand line interface."""

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')  # noqa: WPS421
    user_name = get_user_name().capitalize()
    print('Hello, {0}!'.format(user_name))  # noqa: WPS421
    return user_name


def get_user_name():
    return prompt.string('May I have your name? ')

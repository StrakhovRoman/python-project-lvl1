"""Game engine."""

import prompt

ROUND_COUNT = 3


def run_game(game_rules, play_game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ').capitalize()
    print('Hello, {0}!'.format(user_name))
    print(game_rules)
    for _ in range(ROUND_COUNT):   # noqa: WPS122
        question, correct_answer = play_game()
        print('Question: {0} '.format(question))
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                """'{0}' is wrong answer ;(. Correct answer was '{1}'
                """.format(user_answer, correct_answer),
            )
            print("Let's try again, {0}".format(user_name))
            break
    else:
        print('Congratulations, {0}!'.format(user_name))

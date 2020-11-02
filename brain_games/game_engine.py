"""Game engine."""

from time import sleep

import prompt

from brain_games import cli


def play(game_rules, game):
    user_name = cli.welcome_user()
    sleep(1)
    print(game_rules)
    sleep(1)
    round_counter = 1
    while round_counter <= 3:
        question, correct_answer = game()
        print(question)
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == correct_answer:
            print('Correct!')
            if round_counter == 3:
                print('Congratulations, {0}!'.format(user_name))
        else:
            print(
                """'{0}' is wrong answer ;(. Correct answer was '{1}'
                """.format(user_answer, correct_answer),
            )
            print("Let's try again, {0}".format(user_name))
            break
        round_counter += 1

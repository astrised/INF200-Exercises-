from random import randint

__author__ = 'Astrid Sedal'
__email__ = 'astrised@nmbu.no'


def guess_number():
    number = 0
    while number < 1:
        number = int(input('Your guess: '))
    return number


def draw_sum():
    return randint(1, 6) + randint(1, 6)


def check(answer, guess):
    return answer == guess


if __name__ == '__main__':

    verified = False
    points = 3
    correct_answer = draw_sum()
    while not verified and points > 0:
        guessed_number = guess_number()
        verified = check(correct_answer, guessed_number)
        if not verified:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(correct_answer))

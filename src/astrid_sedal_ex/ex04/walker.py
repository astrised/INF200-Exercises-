# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'
__email__ = 'astrised@nmbu.no'

import random

class Walker:
    def __init__(self, start_position, home):
        self.x = start_position
        self.h = home
        self.moves = [-1, 1]
        self.step = 0

    def move(self):
        move = random.choice(self.moves)
        self.x += move
        self.step += 1

    def is_at_home(self):
        return self.x == self.h

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.step


def simulation(distance):
    walk = Walker(0, distance)

    while not walk.is_at_home():
        walk.move()
    return walk.get_steps()


def multi_simulations(sim_n, distance):
    res = []

    for i in range(sim_n):
        res.append(simulation(distance))
    return res


if __name__ == "__main__":
    print(f'Distance:   1 -> Path lengths: {multi_simulations(5, 1)}')
    print(f'Distance:   2 -> Path lengths: {multi_simulations(5, 2)}')
    print(f'Distance:   5 -> Path lengths: {multi_simulations(5, 5)}')
    print(f'Distance:   10 -> Path lengths: {multi_simulations(5, 10)}')
    print(f'Distance:   20 -> Path lengths: {multi_simulations(5, 20)}')
    print(f'Distance:   50 -> Path lengths: {multi_simulations(5, 50)}')
    print(f'Distance:   100 -> Path lengths: {multi_simulations(5, 100)}')



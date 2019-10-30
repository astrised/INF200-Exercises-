# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walk = Walker(self.start, self.home)

        while not walk.is_at_home():
            walk.move()
        return walk.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        num_list = []
        random.seed(self.seed)

        for i in range(num_walks):
            num_list.append(Simulation.single_walk(self))
        return num_list


if __name__ == "__main__":

    sim1 = Simulation(0, 10, 12345)
    print(f'20 walks from start 0 to home 10: {sim1.run_simulation(20)}')
    sim2 = Simulation(0, 10, 12345)
    print(f'20 walks from start 0 to home 10: {sim2.run_simulation(20)}')
    sim3 = Simulation(0, 10, 54321)
    print(f'20 walks from start 0 to home 10: {sim3.run_simulation(20)}')

    sim4 = Simulation(10, 0, 12345)
    print(f'20 walks from start 0 to home 10: {sim4.run_simulation(20)}')
    sim5 = Simulation(10, 0, 12345)
    print(f'20 walks from start 0 to home 10: {sim5.run_simulation(20)}')
    sim6 = Simulation(10, 0, 54321)
    print(f'20 walks from start 0 to home 10: {sim6.run_simulation(20)}')

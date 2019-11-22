# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'

from src.astrid_sedal_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        super().move()

        if super().get_position() > self.right_limit:
            self.x = self.right_limit
            self.step -= 1

        if super().get_position() < self.left_limit:
            self.x = self.left_limit
            self.step -= 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):

        walk = BoundedWalker(self.start, self.home, self.left_limit,
                             self.right_limit)

        while not walk.is_at_home():
            walk.move()
        return walk.get_steps()


if __name__ == "__main__":
    sim1 = BoundedSimulation(0, 20, 12345, 0, 20)
    print(f'20 walks from start 0 to home 20 with left boundary 0: '
          f'{sim1.run_simulation(20)}')

    sim2 = BoundedSimulation(0, 20, 12345, -10, 20)
    print(f'20 walks from start 0 to home 20 with left boundary -10: '
          f'{sim2.run_simulation(20)}')

    sim3 = BoundedSimulation(0, 20, 12345, -100, 20)
    print(f'20 walks from start 0 to home 20 with left boundary -100: '
          f'{sim3.run_simulation(20)}')

    sim4 = BoundedSimulation(0, 20, 12345, -1000, 20)
    print(f'20 walks from start 0 to home 20 with left boundary -1000: '
          f'{sim4.run_simulation(20)}')

    sim5 = BoundedSimulation(0, 20, 12345, -10000, 20)
    print(f'20 walks from start 0 to home 20 with left boundary -10000: '
          f'{sim5.run_simulation(20)}')

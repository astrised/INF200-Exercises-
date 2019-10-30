# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'

from walker_sim import Walker, Simulation


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
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home)

    def move(self):
        super().move()
        if super().get_position() > self.right_limit:
            self.position = self.right_limit

        if super().get_position() > self.left_limit:
            self.position = self.left_limit


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
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home, seed)


if __name__ == "__main__":
    sim1 = BoundedSimulation(0, 20, 12345, 0, 20)
    print(f'20 walks from start 0 to home 20: {sim1.run_simulation(20)}')
    sim2 = BoundedSimulation(0, 20, 12345, -10, 20)
    print(f'20 walks from start 0 to home 20: {sim2.run_simulation(20)}')
    sim3 = BoundedSimulation(0, 20, 12345, -100, 20)
    print(f'20 walks from start 0 to home 20: {sim3.run_simulation(20)}')
    sim4 = BoundedSimulation(0, 20, 12345, -1000, 20)
    print(f'20 walks from start 0 to home 20: {sim4.run_simulation(20)}')
    sim5 = BoundedSimulation(0, 20, 12345, -10000, 20)
    print(f'20 walks from start 0 to home 20: {sim5.run_simulation(20)}')

#20 walks from start 0 to home 20 for each of the following left boundaries: 0, -10, -100, -1000, -10000.
# The right boundary shall be 20 in all cases.

# Print results as left boundary followed by a list of the 20 walk durations for that left boundary.

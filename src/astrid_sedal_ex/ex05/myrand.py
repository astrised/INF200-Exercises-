# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'


class LCGRand:
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.r_n = seed

    def rand(self):
        self.r_n = self.a * self.r_n % self.m
        return self.r_n

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """

        while True:
            random_number = self.rand()
            yield random_number


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """

        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError()

        next_num_generated = self.generator.rand()
        self.num_generated_numbers += 1

        if self.length == self.num_generated_numbers:
            raise StopIteration

        return next_num_generated






if __name__ == "__main__":
#lcg = LCGRand(346)
#print(lcg.rand())
#print(lcg.rand())

#test_num = [1, 7]
#lr = ListRand(test_num)
#print(lr.rand())
#print(lr.rand())
#print(lr.rand())

    random_number_generator = LCGRand(1)
    for rand in random_number_generator.random_sequence(10):
        print(rand)

    i = 1
    for rand in random_number_generator.infinite_random_sequence():
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
        i += 1

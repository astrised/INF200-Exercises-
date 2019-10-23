# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'

import random


class LCGRand:
    def __init__(self, seed):
        self.r_n = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        self.r_n = self.a * self.r_n % self.m
        return self.r_n


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.current_idx = -1
        self.n = len(numbers)

    def rand(self):
        self.current_idx += 1

        if self.current_idx >= self.n:
            raise RuntimeError('Index out of range')
        return self.numbers[self.current_idx]


if __name__ == "__main__":
    lcg = LCGRand(346)
    print(lcg.rand())
    print(lcg.rand())

    numbers = [1, 7]
    lr = ListRand(numbers)
    print(lr.rand())
    print(lr.rand())
    print(lr.rand())

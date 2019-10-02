# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (sorted_data[num_elements // 2 - 1]
                + sorted_data[num_elements // 2]) / 2


def test_one_element_list():
    """Tests if it returns the correct value for a one-element list."""

    assert median([4]) == 4

def test_odd_numbers_of_elements():
    """Tests lists with odd numbers of elements"""

    list_1 = [1, 4, 7]

    assert median(list_1) == 4
    
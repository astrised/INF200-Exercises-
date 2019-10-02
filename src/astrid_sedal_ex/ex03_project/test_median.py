# -*- coding: utf-8 -*-

__author__ = 'Astrid Hæve Sedal'
__email__ = 'astrised@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements < 1:
        raise ValueError

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (sorted_data[num_elements // 2 - 1]
                + sorted_data[num_elements // 2]) / 2


def test_one_element_list():
    """
    Tests if it returns the correct value for a one-element list.
    """

    assert median([4]) == 4


def test_odd_numbers_of_elements():
    """
    Tests lists with odd numbers of elements.
    """

    list_1 = [1, 4, 7]

    assert median(list_1) == 4


def even_numbers_of_elements():
    """
    Tests lists for even numbers of elements.
    """

    list_1 = [2, 4, 6, 8]

    assert median(list_1) == 5


def test_ordered_reverse_ordered_unordered_elements():
    """
    Tests median of lists with ordered, reverse-ordered and unordered
    elements.
    """

    list_ordered = [1, 2, 3]
    list_reverse_ordered = [3, 2, 1]
    list_unordered = [2, 3, 1]

    assert median(list_ordered) == 2
    assert median(list_reverse_ordered) == 2
    assert median(list_unordered) == 2


def test_median_rasis_value_error_on_empty_list():
    """
    Test checking that requesting the median of an empty list
    raises a ValueError exception.
    """

    with pytest.raises(ValueError):  # context manager
        median([])


def test_original_data_unchanged():
    """
    Tests that the the median function leaves the original data unchanged.
    """

    data = [1, 2, 3]

    _ = median(data)

    assert data == [1, 2, 3]


def test_tuples_and_lists():
    """
    Test that the median function works for tuples as well as lists.
    """

    tuples = (1, 2, 3)
    lists = [4, 5, 6]

    assert median(tuples) == 2
    assert median(lists) == 5

def bubble_sort(data_to_be_sorted):
    list_data = list(data_to_be_sorted)
    length_data = len(list_data)

    for i in range(length_data):
        for k in range(length_data - 1):
            if list_data[k] > list_data[k + 1]:
                list_data[k], list_data[k + 1] = list_data[k + 1], list_data[k]
    return list_data

def test_empty():
    """Test that the sorting function works for empty list"""

    empty_list = []

    assert empty_list == bubble_sort(empty_list)


def test_single():
    """Test that the sorting function works for single-element list"""

    single_element_list = [5]

    assert bubble_sort(single_element_list) ==




def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass



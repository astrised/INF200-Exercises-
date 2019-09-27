# -*- coding: utf-8 -*-


__author__ = "Astrid Hæve Sedal"
__email__ = "astrised@nmbu.no"


def bubble_sort(data):
    list_data = list(data)
    length_data = len(list_data)

    for i in range(length_data):
        for k in range(length_data - 1):
            if list_data[k] > list_data[k + 1]:
                list_data[k], list_data[k + 1] = list_data[k + 1], list_data[k]
    return list_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))

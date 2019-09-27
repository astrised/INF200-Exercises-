# -*- coding: utf-8 -*-


from math import log2


__author__ = "Astrid Hæve Sedal"
__email__ = "astrised@nmbu.no"


def letter_freq(txt):
    """
    Counts how many times a character occurs in a text.

    Returns
    -------
    freq: dict
    """
    freq = {}
    txt = txt.lower()
    for character in txt:
        keys = freq.keys()
        if character in keys:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq


def entropy(message):
    """
    The function calculates the entropy with given equation.

    Returns
    -------
    h: float
    """

    message = letter_freq(message)
    n = sum(message.values())
    h = 0
    for n_i in message.values():
        p_i = n_i / n
        h += - p_i * log2(p_i)
    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

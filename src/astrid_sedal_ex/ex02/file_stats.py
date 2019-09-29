# -*- coding: utf-8 -*-


__author__ = "Astrid Hæve Sedal"
__email__ = "astrised@nmbu.no"


def char_counts(textfilename):
    """
    The function counts how often each character code occurs in a text file.
    The text file is converted into a
    single string and encoded using utf-8.

    Returns
    -------
    frequnecies_char: list
    """

    with open(textfilename, 'r', encoding='utf-8') as f:
        textfile_string = f.read()
        f.close()

    frequencies_char = [0] * 256
    for char in textfile_string:
        frequencies_char[ord(char)] += 1

    return frequencies_char


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )

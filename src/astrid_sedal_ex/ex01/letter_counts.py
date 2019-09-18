
def letter_freq(txt):
    dict = {}
    txt = txt.lower()
    for letter in txt:
        keys = dict.keys()
        if letter in keys:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))

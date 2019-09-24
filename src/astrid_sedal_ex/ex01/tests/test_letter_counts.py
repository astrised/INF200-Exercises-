from ..letter_counts import letter_freq

def test_letter_frew_counts_on_sample_strings():
    count = letter_fres('a')
    assert count['a'] == 1

    count = letter_freq('aa')
    assert count['a'] == 2

    count = letter_freq('ab')
    assert count['a'] == 1
    assert count['b'] == 1
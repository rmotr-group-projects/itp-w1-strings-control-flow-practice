def first_half(a_string):
    x = len(a_string)
    y = int(x / 2)
    if x % 2 == 0:
        return a_string[0:y]
    else:
        return a_string[0:y + 1]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

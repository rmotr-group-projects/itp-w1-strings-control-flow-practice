def first_half(a_string):
    length = len(a_string)
    half = int(length / 2)
    if length % 2 == 0:
        return a_string[:half]
    else:
        return a_string[:half + 1]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

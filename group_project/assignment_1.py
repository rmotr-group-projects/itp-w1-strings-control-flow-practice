def first_half(a_string):
    half = int(len(a_string) / 2)
    return a_string[:half]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

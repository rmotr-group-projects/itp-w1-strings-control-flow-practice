def first_half(a_string):
    return a_string[0:int(round(float(len(a_string))/2))]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

def first_half(a_string):
    if len(a_string) % int(2) == 0:
        return a_string [:(len(a_string)/2)]
    elif len(a_string) % 2 != 0:
        return a_string [:(len(a_string)/2)+1]
        


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

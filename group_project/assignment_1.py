def first_half(a_string):
    string = a_string
    if len(string) % 2 == 0:
        return string[:int((len(string) / 2))]
    return string[:int((len(string) / 2 + 1))]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

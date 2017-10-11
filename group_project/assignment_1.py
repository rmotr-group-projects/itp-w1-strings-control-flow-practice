def first_half(a_string):
    if len(a_string) % 2 == 0:
       half_str = a_string[:3]
       return half_str
    elif len(a_string) % 2 != 0:
        odd_half_str = a_string[:4]
        return odd_half_str


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

def first_half(a_string):
    idx = int(len(a_string)/2)
    if len(a_string) % 2 == 0:
        return a_string[:idx]
    else:
        return a_string[:idx+1]

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

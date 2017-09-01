def first_half(a_string):
    length = len(a_string)
    half_length = length/2
    if length % 2 == 0:
        return a_string[:half_length]
    return a_string[:half_length + 1]

print(first_half('abcdefg'))
    



def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

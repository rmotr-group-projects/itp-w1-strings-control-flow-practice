def first_half(a_string):
 # figure out if odd or even
    if len(a_string)%2 == 0:
        # we are even return the first half positions 0 1 2
        return a_string[:(len(a_string)/2)]
    else:
        # we are odd return the first half plus an extra positions 0 1 2 3
        return a_string[:(len(a_string)/2)+1]

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'
    
print(first_half('abcdef'))
print(first_half('abcXdef'))
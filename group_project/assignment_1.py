def first_half(a_string):
    str_len = len(a_string)
    
    if (str_len % 2) == 0:
        return a_string[0:(str_len/2)] 
    else:
        return a_string[0:(str_len/2) + 1]

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

def first_half(a_string):
    length = int(len(a_string)/2)
    
    if len(a_string) % 2 == 0:
        return(a_string[0:length])
    
    elif len(a_string) % 2 != 0:
        odd_length = int(len(a_string)/2 +1)
        return(a_string[0:odd_length])



def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

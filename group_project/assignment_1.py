def first_half(a_string):
    if len(a_string)%2==0:
        return a_string[0:int(len(a_string) / 2)]
    if len(a_string)%2==1:
        return a_string[0:int((len(a_string)/2)+1)]
        
        
print(first_half('abcdef'))
print(first_half('abcXdef'))


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

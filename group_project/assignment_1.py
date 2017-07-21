def first_half(a_string):
    length = len(a_string)
    if len(a_string) % 2 == 0:
        half_string = a_string[0:int(length/2)]
    else:
        half_string = a_string[0:int((length/2)+1)]
    return half_string

print(first_half('abcdef'))
print(first_half('abcXdef'))

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'

def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'
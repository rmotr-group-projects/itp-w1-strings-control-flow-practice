def first_half(a_string):
    length = len(a_string)
    if length % 2 == 0:
        return(a_string[0:length/2])
    else:
        return(a_string[0:((length/2)+1)])
        
print("richard")

print(first_half("Rich"))
print(first_half("Richa"))
        
print(first_half('abcdef'))    
print(first_half('abcXdef'))
        


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

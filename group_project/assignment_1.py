def first_half(a_string):
#    length=len(a_string)
#    if length % 2 != 0:
#       length+=1
#    halflen = int(length/2)
#    result=a_string[0:halflen]
#    return result

# so +1 if odd
# 

    odd_even = (len(a_string) % 2 )
    # 1 or 0
    
    return a_string[0:((len(a_string) / 2) + odd_even)]

def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'

# py.test -v --tb=short group_project/assignment_1.py


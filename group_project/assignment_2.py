def all_in_string(a_string, s1, s2, s3):
    # assign each boolean to a variable
    a = s1 in a_string
    b = s2 in a_string
    c = s3 in a_string
    # convert each variable value to an integer and add them up. 
    return int(a) + int(b) + int(c)        

def test_only_one_in_string():
    assert all_in_string('abcd', 'a', 'X', 'Y') == 1
    assert all_in_string('abcd', 'X', 'a', 'Y') == 1
    assert all_in_string('abcd', 'Y', 'X', 'a') == 1


def test_two_in_string():
    assert all_in_string('abcd', 'a', 'b', 'X') == 2
    assert all_in_string('abcd', 'a', 'X', 'b') == 2
    assert all_in_string('abcd', 'X', 'a', 'b') == 2


def test_three_in_string():
    assert all_in_string('abcd', 'a', 'b', 'c') == 3

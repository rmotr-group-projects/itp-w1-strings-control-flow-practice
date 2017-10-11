def all_in_string(a_string, s1, s2, s3):
    if s1 in a_string:
        a = 1
    else: a = 0
    if s2 in a_string:
        b = 1
    else: b = 0
    if s3 in a_string:
        c = 1
    else: c = 0
    return a + b + c

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

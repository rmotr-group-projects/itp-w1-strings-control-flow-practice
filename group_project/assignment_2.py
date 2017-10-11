def all_in_string(a_string, s1, s2, s3):
    count = 0
    if s1[0] == a_string[0] or s1[0] == a_string[1] or s1[0] == a_string[2] or s1[0] == a_string[3]:
        count = 1
    if s2[0] == a_string[0] or s2[0] == a_string[1] or s2[0] == a_string[2] or s2[0] == a_string[3]:
        count = count + 1
    if s3[0] == a_string[0] or s3[0] == a_string[1] or s3[0] == a_string[2] or s3[0] == a_string[3]:
        count = count + 1
    return(count)
    



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

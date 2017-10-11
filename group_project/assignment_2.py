def all_in_string(a_string, s1, s2, s3):
    counter = 0
    for i in range(len(a_string)):
        if a_string[ i : i + len(s1) ] == s1:
            counter +=1
        elif a_string[ i : i + len(s2) ] == s2:
            counter +=1 
        elif a_string[ i : i + len(s3) ] == s3:
            counter +=1    
    return counter
    

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

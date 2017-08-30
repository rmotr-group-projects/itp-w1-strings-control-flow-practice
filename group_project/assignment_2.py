def all_in_string(a_string, s1, s2, s3):
    counter = 0
    counter = a_string.count(s1)
    counter = counter + a_string.count(s2)
    counter = counter + a_string.count(s3)
    return counter
  
print (all_in_string('abcd', 'a', 'X', 'Y'))
print (all_in_string('abcd', 'X', 'a', 'Y'))
print (all_in_string('abcd', 'Y', 'X', 'a'))

print (all_in_string('abcd', 'a', 'b', 'X'))
print (all_in_string('abcd', 'a', 'X', 'b'))
print (all_in_string('abcd', 'X', 'a', 'b'))

print (all_in_string('abcd', 'a', 'b', 'c'))


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

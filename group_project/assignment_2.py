def all_in_string(a_string, s1, s2, s3):
    valor = 0
    a_string1 = a_string
    for x in a_string1:
        s = a_string1[0:1]
        if s == s1:
            valor = valor + 1
        a_string1 = a_string1[1:]
    
    a_string2 = a_string
    for x in a_string2:
        s = a_string2[0:1]
        if s == s2:
            valor = valor + 1
        a_string2 = a_string2[1:]
    
    a_string3 = a_string
    for x in a_string3:
        s = a_string3[0:1]
        if s == s3:
            valor = valor + 1
        a_string3 = a_string3[1:]
    return valor

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

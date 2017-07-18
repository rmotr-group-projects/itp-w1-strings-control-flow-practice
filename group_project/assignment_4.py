def how_many_times(a_string, a_word):
    return a_string.count(a_word)


def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0





# str.count(sub [, start[, end]] )
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

# str.decode([encoding[, errors]])
# string.count(thing_to_find)

"""str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found."""
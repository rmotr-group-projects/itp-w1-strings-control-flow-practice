def how_many_times(a_string, a_word):
    count = a_string.count(a_word)
    return count

print(how_many_times('Dov is the coolest Dov in the world!', 'Dov'))


def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0

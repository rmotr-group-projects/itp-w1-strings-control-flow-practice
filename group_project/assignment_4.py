def how_many_times(a_string, a_word):
    word_list = a_string.split(" ")
    total = 0
    for word in word_list:
        if word == a_word:
            total = total + 1
        else:
            total = total
    return total

def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0

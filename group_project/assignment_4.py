def how_many_times(a_string, a_word):
    b_string = a_string.split(' ')
    summarize = 0
    for i in range(len(b_string)):
        if a_word == b_string[i]:
            summarize += 1
            
    c_string = ' '.join(b_string)
    return summarize


def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0

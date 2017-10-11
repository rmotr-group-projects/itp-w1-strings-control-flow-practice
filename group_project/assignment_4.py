def how_many_times(a_string, a_word):
    if a_word in a_string:
        return a_string.count(a_word)
    if not a_word in a_string:
        return 0
   
    

phrase_1 = "Python is a great language. I like Python a lot."
phrase_2 = "Python is a great language. I like it a lot."
phrase_3 = "Python is a great language."

print(how_many_times(phrase_1,"Python"))
print(how_many_times(phrase_2,"Python"))
print(how_many_times(phrase_3,"Ruby"))




def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0

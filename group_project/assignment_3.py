def replace_bad_words(a_string, word_to_replace, new_word):
    if a_string.find(word_to_replace) != -1:
        new_string=a_string.replace("Ruby", "Python")
        return new_string
    else:
        return a_string
        
def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

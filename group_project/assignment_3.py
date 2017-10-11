def replace_bad_words(a_string, word_to_replace, new_word):
    if word_to_replace in a_string:
        new_string = a_string.replace(word_to_replace, new_word)
        return(new_string)
    return(a_string)   


def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

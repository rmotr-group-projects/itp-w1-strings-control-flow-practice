
def replace_bad_words(a_string, word_to_replace, new_word):
    find_word = a_string.find(word_to_replace)
    word_length = len(word_to_replace)
    replace = find_word + word_length
    if find_word != -1:
        a_string = a_string.replace(word_to_replace, new_word)
        print (a_string)
        return (a_string)
    return a_string


def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

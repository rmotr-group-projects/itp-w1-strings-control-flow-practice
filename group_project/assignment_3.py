def replace_bad_words(a_string, word_to_replace, new_word):
    texto = a_string
    new_str = texto.replace(word_to_replace,new_word)
    if texto == new_str:
        return texto
    return new_str


def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

def replace_bad_words(a_string, word_to_replace, new_word):
    return a_string.replace(word_to_replace,new_word)

string_a = "Ruby is a great language! Yay Ruby!"

string_b = "Hello World"

print(replace_bad_words(string_a,"Ruby","Python"))
print(replace_bad_words(string_b,"Ruby","Python"))


def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

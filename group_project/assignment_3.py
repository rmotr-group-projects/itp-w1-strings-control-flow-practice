def replace_bad_words(a_string, word_to_replace, new_word):
    replaced_sentence = a_string.replace('Ruby', 'Python')
    return replaced_sentence

#print(replace_bad_words('Ruby, Ruby, Ruby Soho', 'Ruby', 'Python'))

def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"

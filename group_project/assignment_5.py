def positions(a_string, first_word, second_word, third_word):
    word_list = [first_word, second_word, third_word]
    pos_list = []
    for word in word_list:
        pos = a_string.find(word)
        if pos == -1:
            pos_list.append('-')
        else:
            pos_list.append(str(pos))
    return ",".join(pos_list)


def test_three_occurrences():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'like') == "0,26,34"


def test_two_occurrences_missing_third():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'Ruby') == "0,26,-"


def test_two_occurrences_missing_first():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Ruby', 'Wise', 'like') == "-,26,34"


def test_one_occurrence_first_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Javascript', 'Ruby') == "0,-,-"


def test_one_occurrence_second_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'like', 'Ruby') == "-,34,-"


def test_one_occurrence_third_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'Ruby', 'Wise') == "-,-,26"

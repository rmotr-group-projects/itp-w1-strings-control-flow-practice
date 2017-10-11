def positions(a_string, first_word, second_word, third_word):
    index1 = a_string.find(first_word)
    if index1 != -1:
        a = index1
    else:
        a = '-'
    index2 = a_string.find(second_word)
    if index2 != -1:
        b = index2
    else:
        b = '-'
    index3 = a_string.find(third_word)
    if index3 != -1:
        c = index3
    else:
        c = '-'
    return "{},{},{}".format(a, b, c)

a_string = "Python is good. Python is Wise. I like Python"
first_word = 'Python'
second_word = 'Wise'
third_word = 'Ruby'

testcode = positions(a_string, first_word, second_word, third_word)
print(testcode)


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

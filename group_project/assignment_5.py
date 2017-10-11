phrase = "Python is good. Python is Wise. I like Python"

def positions(a_string, first_word, second_word, third_word):
    first_found = a_string.find(first_word)
    if first_found < 0:
        first_found = '-'
    second_found = a_string.find(second_word)
    if second_found < 0:
        second_found = '-'
    third_found = a_string.find(third_word)
    if third_found < 0:
        third_found = '-'
    return str(first_found) + ',' + str(second_found) + ',' + str(third_found)

print(positions(phrase, 'Python', 'Wise', 'like'))
print(positions(phrase, 'Python', 'Wise', 'Ruby'))
print(positions(phrase, 'Ruby', 'Wise', 'like'))
print(positions(phrase, 'Python', 'Javascript', 'Ruby'))
print(positions(phrase, 'Javscript', 'like', 'Ruby'))
print(positions(phrase, 'Javscript', 'Ruby', 'Wise'))

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

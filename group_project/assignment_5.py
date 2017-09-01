def positions(a_string, first_word, second_word, third_word):
    if first_word in a_string:
        first_word_loc = a_string.find(first_word)
    else:    
        first_word_loc = '-'
    
    if second_word in a_string:
        second_word_loc = a_string.find(second_word)
    else:
        second_word_loc = '-'
    
    if third_word in a_string:
        third_word_loc = a_string.find(third_word)
    else:
        third_word_loc = '-'
    
    response = str(first_word_loc) + ',' + str(second_word_loc) + ',' + str(third_word_loc)
    return response
    
print(positions('The Jax is back and youre gonna be in trouble.', 'Jax', 'two', 'trouble'))




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

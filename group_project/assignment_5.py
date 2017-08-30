def positions(a_string, first_word, second_word, third_word):

    if first_word not in a_string:
        pos1 = "-"
    else:
        pos1 = a_string.index(first_word)
        
    if second_word not in a_string:
        pos2 = "-"
    else:
        pos2 = a_string.index(second_word)        

    if third_word not in a_string:
        pos3 = "-"
    else:
        pos3 = a_string.index(third_word)
        
    pos = str(pos1) + "," + str(pos2) + "," + str(pos3)
    return pos

# For troubleshooting and testing purposes      
phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Python', 'Wise', 'like'))

phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Python', 'Wise', 'Ruby'))

phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Ruby', 'Wise', 'like'))

phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Python', 'Javascript', 'Ruby'))

phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Javscript', 'like', 'Ruby'))

phrase = "Python is good. Python is Wise. I like Python"
print(positions(phrase, 'Javscript', 'Ruby', 'Wise'))

# Provided test cases
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

def positions(a_string, first_word, second_word, third_word):
    pos1 = a_string.find(first_word)
    pos2 = a_string.find(second_word)
    pos3 = a_string.find(third_word)
    
    if pos1 == -1:
       pos1 = '-'
    else:
       pos1 = str(pos1)    
    if pos2 == -1:
       pos2 = '-'
    else:
       pos2 = str(pos2)
    if pos3 == -1:
       pos3 = '-'
    else:
       pos3 = str(pos3)

    myfinalresult = pos1 + ',' + pos2 + ',' + pos3
    return myfinalresult
   
phrase = "Python is good. Python is Wise. I like Python"
print (positions(phrase, 'Python', 'Wise', 'like'))
print (positions(phrase, 'Python', 'Wise', 'like'))
print (positions(phrase, 'Python', 'Wise', 'Ruby'))
print (positions(phrase, 'Ruby', 'Wise', 'like'))
print (positions(phrase, 'Python', 'Javascript', 'like'))
print (positions(phrase, 'Javascript', 'Wise', 'like'))
print (positions(phrase, 'Javascript', 'Ruby', 'wise'))




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

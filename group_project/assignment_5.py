def positions(a_string, first_word, second_word, third_word):
    pos_1st = a_string.find(first_word)
    pos_2nd = a_string.find(second_word)
    pos_3rd = a_string.find(third_word)
    if pos_1st == -1:
        pos_1st = '-'
    else:
        pos_1st = str(pos_1st)
    if pos_2nd == -1:
        pos_2nd = '-'
    else:
        pos_2nd = str(pos_2nd)
    if pos_3rd == -1:
        pos_3rd = '-'
    else:
        pos_3rd = str(pos_3rd)
    
    myfinalresult = pos_1st + ',' + pos_2nd + ',' + pos_3rd
    return myfinalresult

    

print(positions("Python is good. Python is Wise. I like Python", 'Python', 'Wise', 'like'))
print(positions("Python is good. Python is Wise. I like Python",'Python', 'Wise', 'Ruby'))
print(positions("Python is good. Python is Wise. I like Python", 'Ruby', 'Wise', 'like'))
print(positions("Python is good. Python is Wise. I like Python", 'Python', 'Javascript', 'Ruby'))
print(positions("Python is good. Python is Wise. I like Python", 'Javscript', 'like', 'Ruby'))
print(positions("Python is good. Python is Wise. I like Python", 'Javscript', 'Ruby', 'Wise'))


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

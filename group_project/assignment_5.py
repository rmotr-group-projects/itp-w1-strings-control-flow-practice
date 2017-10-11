def positions(a_string, first_word, second_word, third_word):
    
    #Checking if the third_word exists in a_string before looking for index
    #Looking for index of a string not present will throw an error (ValueError: substring not found)
    if third_word in a_string:
        #Creating a variable i3 to hold integer index of third_word
        i3 = a_string.index(third_word)
        #Casting integer into a String to be able to concatenate into one String
        i3 = str(i3)
    else:
        #Since third_word doesn't exists in a_string, setting index to '-'
        i3 = '-'
    if second_word in a_string:
        i2 = str(a_string.index(second_word))
        i2 = str(i2)
    else:
        i2 = '-'
    
    if first_word in a_string:
        i1 = str(a_string.index(first_word))
        i1 = str(i1)
    else:
        i1 = '-'
    
    #Concatenating 3 indexes into 1 string
    indexText = i1 + ',' + i2 + ',' + i3
    
    #Function returns String indexText when executed.
    return indexText

#Test passes    
def test_three_occurrences():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'like') == "0,26,34"

#Test passes
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

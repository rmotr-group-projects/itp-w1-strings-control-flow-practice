def find_position(text, search):
    # take text and a search 
    if search in text:
       # if the search is in the text find the starting position  
       # find will return the index of the search so we return it 
       return text.find(search)
    else:
        # if the search is not here return a -
        return "-"

def positions(a_string, first_word, second_word, third_word):
    # these are the words we want to search for 
    words = [first_word, second_word, third_word]
    
    results = ''
    
    # loop through the words 
    for word in words:
        # call find_position then add a , to the end 
        results += str(find_position(a_string, word)) + ","
    # return the final array up to the last comma but don't include it 
    return results[0:-1]


##########
## Goal ##
##########

# take 3 inputs and print out the character location of the first letter in the
# search strings. If a word is missing print out only - 

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

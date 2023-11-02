list_of_words = ['flabberghasted', 'jovial', 'taxidermy', 'nucleus', 'erudite', 'hey', 'youdidit']
must_start_with = {'h', 'y'}

def print_upper_words(list, must_start_with=None):
    """ 
    #this is a docstring! 
    """
    for word in list:
        if must_start_with is None or any(word.lower().startswith(char.lower()) for char in must_start_with):
            print(f"\n{word.upper()}")
        
    



#check for index of first letter in word
#if it's an 'h' or a 'y' the print

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                   must_start_with={"h", "y"})
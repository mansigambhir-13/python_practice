#takes a string and replaces all occurrences of a word with another word

def replace_word_in_string(string, word_to_replace, replacement_word):

    str = "may name is mansi !!"

    string = "The original string"
    word_to_replace = input(word_to_replace)
    replacement_word = input(replacement_word)
    
    
    return (string.replace(word_to_replace, replacement_word))
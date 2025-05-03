word_dict = {
    "python": "a high-level programming language.",
    "variable": "a name that refers to a value.",
    "function": "a reusable block of code.",
    "loop": "a control structure that repeats actions."
}

def get_word_definition(word):
    """Return the definition of a word if it exists in the dictionary."""
    return word_dict.get(word.lower(), "Word not found in the dictionary.")


#exmample usage
while True :
    word = input("Enter a word to get its definition (or 'exit' to quit): ").strip()
    if word.lower() == 'exit':
        break
    definition = get_word_definition(word)
    print(f"Definition of '{word}': {definition}")
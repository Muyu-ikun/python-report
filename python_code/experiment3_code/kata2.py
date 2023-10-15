def duplicate_encode(word):
    #your code here
    word = word.lower()
    new_word = ""
    for char in word:
        if word.count(char) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word
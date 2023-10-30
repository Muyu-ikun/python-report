def is_pangram(s):

    s = s.lower()

    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    for char in s:
        if char.isalpha():
            alphabet.discard(char)


    return not alphabet

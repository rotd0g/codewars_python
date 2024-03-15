def is_isogram(string):
    string = string.lower()
    restring = ''
    for letter in string:
        if letter not in restring:
            restring += letter
            # print(restring)
        else:
            return False
    return True

print(is_isogram("Dermatoglyphdics"))
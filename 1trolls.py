


def disemvowel(string_):
    assert type(string_) == str

    vowels_list = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    resulting_string = ""

    for symbol in string_:
        if symbol in vowels_list:
            pass
        else:
            resulting_string += symbol

    return resulting_string
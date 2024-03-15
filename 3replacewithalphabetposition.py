"""Welcome.

In this kata you are required togiven a stringreplace every letter with its position in the alphabet.

If anything in the text isn't a letter ignore it and don't return it.

"a" = 1, "b" = 2etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""

def alphabet_position(text):
    assert type(text) == str

    letter_number_list = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    result = ""

    for symbol in text:
        symbol = symbol.lower()
        if symbol in letter_number_list:
            result += str(letter_number_list.index(symbol) + 1) + " "

    return result.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))

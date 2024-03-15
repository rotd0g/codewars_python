# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
#
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):

    # 1 convert - to _ V
    # 2 Capitalize Next Symbol after _
    # 3 Remove _
    assert type(text) == str
    if not text:
        return text
    text = text.replace('-', '_')
    aftergap = [0]
    camel = text[0]
    print(camel)

    for i in range(len(text)):
        if text[i] == "_":
            aftergap.append(i+1)
            camel += text[i+1].upper()
        else:
            if i not in aftergap:
                camel += text[i].lower()
    return camel

print(to_camel_case(''))
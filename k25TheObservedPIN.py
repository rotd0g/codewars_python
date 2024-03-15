# DESCRIPTION:
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
#
# The keypad has the following layout:
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.
#
# Detective, we are counting on you!

def get_pins(observed):

    # TODO: This is your job, detective!
    # 1. Map each number with adjacent - create dict: {1 : [1, 2, 4]}
    # 2. create resulting list
    # 3.
    # 4. post all results as strings to the list

    adjacent = {'0': ['0', '8'], '1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['6', '2', '3'],
                '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'],
                '7': ['4', '7', '8'], '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9']}

    result = []
    for digit1 in adjacent[observed[0]]:
        if len(observed) == 1:
            result.append(digit1)
            continue
        for digit2 in adjacent[observed[1]]:
            if len(observed) == 2:
                result.append(digit1 + digit2)
                continue
            for digit3 in adjacent[observed[2]]:
                if len(observed) == 3:
                    result.append(digit1 + digit2 + digit3)
                    continue
                for digit4 in adjacent[observed[3]]:
                    if len(observed) == 4:
                        result.append(digit1 + digit2 + digit3 + digit4)
                        continue
                    for digit5 in adjacent[observed[4]]:
                        if len(observed) == 5:
                            result.append(digit1 + digit2 + digit3 + digit4 + digit5)
                            continue
                        for digit6 in adjacent[observed[5]]:
                            if len(observed) == 6:
                                result.append(digit1 + digit2 + digit3 + digit4 + digit5 + digit6)
                                continue
                            for digit7 in adjacent[observed[6]]:
                                if len(observed) == 7:
                                    result.append(digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7)
                                    continue
                                for digit8 in adjacent[observed[7]]:
                                    if len(observed) == 8:
                                        result.append(digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + digit8)

    return result



print(get_pins("03691238"))

"""test_cases = [
    ('8', ['5', '7', '8', '9', '0']),
    ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
    ('369', [
        "339", "366", "399", "658", "636", "258", "268", "669", "668", "266",
        "369", "398",
        "256", "296", "259", "368", "638", "396", "238", "356", "659", "639",
        "666", "359",
        "336", "299", "338", "696", "269", "358", "656", "698", "699", "298",
        "236", "239"
    ])"""
"""
a = {
        "339", "366", "399", "658", "636", "258", "268", "669", "668", "266",
        "369", "398",
        "256", "296", "259", "368", "638", "396", "238", "356", "659", "639",
        "666", "359",
        "336", "299", "338", "696", "269", "358", "656", "698", "699", "298",
        "236", "239"}

b = set(['636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699', '236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399'])

print(a == b)"""
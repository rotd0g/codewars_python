"""The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]"""

def open_or_senior(data:[[int],[int]]):

    if type(data) is not list:
        return

    output = []
    for d in data:
        age = d[0]
        handicap = d[1]

        if age >= 55 and handicap > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output


"""
        if age in data[x]:
            and data[0] >= 55
            output +=
            print(age, handicap)
    return output
"""


print(open_or_senior([[55, 7], [45, 0], [0,1], [37, 6], [21, 21], [78, 9], [-88, -4]]))
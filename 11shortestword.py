# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    slist = s.split()
    minl = len(slist[0])
    for word in slist:
        if len(word) < minl:
            minl = len(word)
    return minl

    # l: shortest word length
# print(slist)
#     print(slist[2])

print(find_short('bitcoin take over the world maybe who knows perhaps'))
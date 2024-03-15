"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, 
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


# from k17deleteifmorethanNtimes import delete_nth


def delete_nth(order, max_e):
    neworder = []
    for element in order:
        if neworder.count(element) < max_e:
            neworder.append(element)
    return neworder


def longest(a1, a2):
    # 1. check a1, a2 = str
    # 2. create newstring = ''
    # 3. take all from a1 -> newstring,
    # 4. take all  from a2 -> newstring
    # 5. remove all copies,sort

    assert type(a1) == str
    assert type(a2) == str

    newstring = sorted(a1 + a2)
    newstring = ''.join(delete_nth(newstring, 1))

    return newstring


print(longest("xyaabbbccccdef", "abcdefghijklmnopqrstuvwxyz"))

"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""


def xo(s):
    s = s.lower()
    x = 0
    o = 0
    for char in s:
        if char == 'x':
            x += 1
        if char == 'o':
            o += 1
    return x == o


print(xo("oox0x"))

# if s.count('x') == s.count('o'):
#     return True
# else:
#     return False

# return s.count('x') == s.count('o')

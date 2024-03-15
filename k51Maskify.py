# return masked string
def maskify(cc):
    return '#' * len(cc[0:-4]) + cc[-4:]

print(maskify('535'))

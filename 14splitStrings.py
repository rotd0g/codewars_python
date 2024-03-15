

def solution(s):
    assert type(s) == str
    split = []

    if len(s) % 2 != 0:
        s += '_'
    for pair in range(0, len(s), 2):
        split.append(s[pair:pair+2])
    return split
    # [::]

print(solution('abcadadadadxa'))
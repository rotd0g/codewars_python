def sum_strings(x, y):
    if x == '':
        x = '0'
    if y == '':
        y = '0'


    if len(str(x)) < 4300 or len(str(y)) < 4300:
        a = int(x) + int(y)
        return ''.join(str(a))

    if len(x) > len(y):
        y = y.zfill(len(x))
    # print(x, y)

    if len(x) < len(y):
        x = x.zfill(len(y))
    # print(x, y)

    summa = ''
    desyatki = 0

    for i in range(len(y) - 1, -1, -1):
        desyatki, edinizi = divmod((desyatki + int(x[i]) + int(y[i])), 10)

        summa += str(edinizi)
        print(x[i], y[i], summa)
    if desyatki > 0:
        summa += str(desyatki)
    return summa[::-1]

print(sum_strings("88", "11"))

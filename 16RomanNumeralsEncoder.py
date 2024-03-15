# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Example:
#
# solution(1000) # should return 'M'
# Help:
#
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(n):
    x = []
    dp = 1
    while n:
        rem = n % 10
        x.append(roman_decimals(dp, rem))

        n //= 10
        dp *= 10

    return ''.join(reversed(x))

def roman_decimals(dp, qty):
    roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
             8: 'VIII', 9: 'IX', 10: 'X',
             50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    if qty in (4,9):
        x = roman[dp]+roman[(qty+1) * dp]
    if qty < 4 :
        x = roman[dp]*qty
    if 9 > qty >= 5:
        x = roman[5 * dp] + roman[dp]*(qty-5)
    if qty == 0:
        x = ''

    return x

print(solution(94))


print(n,rem,x)

# x += int_to_roman(n*10)
# x += int_to_roman(rem)

def int_to_roman(n):

    # TODO convert int to roman string
    # 1. create dictionary Symbol == Value
    # 2. минусуем n начиная с самых больших чисел: 1000, 500, 100, 50, 10
    # 3. превращаем, с помощью деления  //  или округления к ближайшему числу и запоминаем



    roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
             8: 'VIII', 9: 'IX', 10: 'X',
             50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    x = None

    if n in (4,9):
        x = roman[1]+roman[n+1]
    if n < 4 :
        x = roman[1]*n
    if 9 > n >= 5:
        x =roman[5] + roman[1]*(n-5)
    if n >= 10:
        x = roman[n]

    return x

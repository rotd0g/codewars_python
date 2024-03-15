# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    nmax = None
    nmin = None
    for num in numbers.split(' '):
        if nmax is None:
            nmax = int(num)
        if int(num) > nmax:
            nmax = int(num)
        if nmin is None:
            nmin = int(num)
        if int(num) < nmin:
            nmin = int(num)
    return f'{nmax} {nmin}'

print(high_and_low("-2221 -2 -3 1110 -5"))
"""The goal is to create a function of two inputs number and power,
that "raises" the number up to power (ie multiplies number by itself power times).

Examples
number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
number_to_pwr(10, 6) # -> 1000000
"""


def number_to_pwr(number, p):
    # if p == 0:
    #     return 1
    a = 1
    count = p
    while count > 0:
        a = a * number
        count -= 1
    return a

print(number_to_pwr(0, 20))

# No ** allowed: False should equal True
"""
   0. round inputs
   1. find optimal ways to convert r values to first 2 output values
   2. repeat for g,b
   3. test output vs 6 long
   4. form an output string
   """



def rgb(r, g, b):
    # The rgb function is incomplete.
    # Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
    # Valid decimal values for RGB are 0 - 255.
    # Any values that fall out of that range must be rounded to the closest valid value.
    #
    # Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
    #
    # Examples (input --> output):
    # 255, 255, 255 --> "FFFFFF"
    # 255, 255, 300 --> "FFFFFF"
    # 0, 0, 0       --> "000000"
    # 148, 0, 211   --> "9400D3"

    colors = [r, g, b]
    dic16 = '0123456789ABCDEF'
    output = ''

    for i, colorcode in enumerate([r, g, b]):
        colorcode = 0 if colorcode < 0 else colorcode
        colorcode = 255 if colorcode > 255 else colorcode
        colors[i] = colorcode
    (r, g, b) = colors

    for colorcode in (r, g, b):
        r1 = colorcode // 16
        output += dic16[r1]
        r1 = colorcode % 16
        output += dic16[r1]
    return output

print(rgb(0,-256,255))
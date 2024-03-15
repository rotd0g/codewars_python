"""How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""

def rot13(message):
    #1. input and output create dict
    #2. new string = ''
    #3.
    # message
    input = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    output = ' NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890'

    output_dict = dict(zip(input, output))
    # print(output_dict)
    decode = ''
    for c in message:
        if c in output_dict:
            decode += output_dict[c]
        else:
            decode += c
    return decode

print(rot13("EBG13 rknzcyr."))

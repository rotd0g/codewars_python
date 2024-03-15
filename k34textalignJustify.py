"""
Your task in this Kata is to emulate text justification in monospace font.
You will be given a single-lined text and the expected justification width.
The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
"""

from random import randint, choices
from string import ascii_letters


def word_separation(text, width):
    """
    part 2
    separate input to words
    """
    if ' ' not in text:
        return text

    text = list(text)
    print("word_separation", text)
    while len(''.join(text)) < width:
        for i in range(len(text)):
            if text[i].startswith(' ') and len(''.join(text)) < width:
                text[i] += ' '
                # print(''.join(text))
    return ''.join(text)
    # print(text, len(text))

# print(word_separation('Lorem ipsum dolor sit ametas,', 30))

def justify(text, width):
    """
    part 1
    separate text into lines:
    step by step take 1 line up to _width_
    adjust this line to the closest space on the left
    memorize this space position and repeat step 1 from 'ifrom'
    """
    text = text.strip()
    ifrom = 0
    lines = []
    position = 0
    result_list = []

    while True:
        position += width

        if position >= len(text): #check if it's last letter, if yes move it to last_line
            last_line = text[ifrom:position].strip()
            print('its enough')
            break
        # print(position, text[position])

        if text[position] != ' ': #we got into word, find a space before it
            for i in range(position, -1, -1):
                if text[i] == ' ':
                    lines.append(text[ifrom:i].strip())
                    position = i + 1
                    ifrom = position
                    break
        else:
            lines.append(text[ifrom:position].strip())
            position += 1
            ifrom = position
        # print(position, lines[-1])
    # print(lines, result_list)

    for line in lines:
        result_list.append(word_separation(line, width))
    result_list.append(last_line)
    return "\n".join(result_list)


testtext = 'Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc.'
testtext1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
testtext2 = """
MrYzGuMss dOA Pojy xyeSeCV r c QPdgsDJC MzTBuwwEEh BiSWYoVi THsWD bOcYoES g fQszTG LhTNIqbr QpNSSYn GAfYc jGJbczsyV l OONmNqR Ubw M slup vyIzXm KaloLEK HvNpEKfB kiRMfHhWi Gwt efnJ dNlZ ZV D Tfpmvmpn K bZW W afuBuqBB ujjsVN rgcqVFlh royAGAl lDjXQuyn ZSmOPstK vmCd"""
testtext3 = """
plBHQbf voRrlhsSg WNb qnLoEiMQE UlUf zFfdVB IGdzbA HnAlSCva Syg mTTAyNrX tdCVNKSiPB lYTmlrsuZu XyEZc oD PyPZsaeG lLAwNaol mNweqnsSwY OImm xnJFlq JUnpm hTycwr lnTkZSzak PHahUQx O KZamIsEg DO gDLprLY vjZIN NfrlJHDe Yihtzs A H XhihuVytAF EIPqf jGsPdS gFeczUrTOl lRCkdsEi HjwT HwNt mAoDUAfaU s BqY
"""
print(justify(testtext3, 23))










#
# def random_tests():
#     def make_random_word():
#         return "".join(choices(ascii_letters, k=randint(1, 10)))
#
#     for _ in range(50):
#         width = randint(10, 50)
#         text = " ".join(make_random_word() for _ in range(randint(25, 50)))
#
#         print(f'Testing text = "{text}" with width = {width}')
#         print(justify(text, width))
#
#
# random_tests()
#


# if text[i] != ' ':
                #     continue

 # for pos in range(ifrom, len(text), width):
# print(text[pos])
# print(list(range(ifrom, len(text), width)))
# result = lines[1].ljust(width)

"""amet,        consectetur
adipiscing  elit, sit
adipiscing  elit,  sit
adipiscing   elit,  sit
adipiscing   elit,   sit
amet,  consectetur
amet,   consectetur
amet,    consectetur
amet,     consectetur
amet,      consectetur
amet,       consectetur
amet,        consectetur
Lorem  ipsum  dolor  sit
amet,        consectetur
adipiscing   elit,   sit
amet,        consectetur
adipiscing elit.

Lorem  ipsum  dolor sit
amet,       consectetur
adipiscing   elit,  sit
amet,       consectetur
adipiscing elit.



ujjsVN rgcqVFlh royAGAl lDjXQuyn ZSmOPstK
Testing text = "MrYzGuMss dOA Pojy xyeSeCV r c QPdgsDJC MzTBuwwEEh BiSWYoVi THsWD bOcYoES g fQszTG LhTNIqbr QpNSSYn GAfYc jGJbczsyV l OONmNqR Ubw M slup vyIzXm KaloLEK HvNpEKfB kiRMfHhWi Gwt efnJ dNlZ ZV D Tfpmvmpn K bZW W afuBuqBB ujjsVN rgcqVFlh royAGAl lDjXQuyn ZSmOPstK vmCd" with width = 46

"""

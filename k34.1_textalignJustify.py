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


def add_spaces_to_line(line, width):
    strline = ''.join(line)
    if len(line) == 1:
        return strline
    spaces_to_add = width - len(strline)
    i = 0
    while spaces_to_add > 0:
        line[i] += ' '
        spaces_to_add -= 1
        i += 1
        i = i % (len(line)-1)

    return ''.join(line)


print(add_spaces_to_line(['fringilla'], 15))
print(add_spaces_to_line(['Donec', 'lorem'], 15))
print(add_spaces_to_line(['Donec', 'lorem', 'eclip'], 18))


def is_word_fits_in_line(line, word, width):
    strline = ' '.join(line)
    return len(strline + ' ' + word) <= width

# print(is_word_fits_in_line(['Donec', 'lorem'], 'eclipsis', 21), True)
# print(is_word_fits_in_line(['Donec', 'lorem'], 'eclipsis', 19), False)


def justify(text, width):
    """
    1. split text into words
    2. form lines up to width
    3. add spaces to lines which are less than width
    4. avoid adding spaces to last line
    5. '\n' join to form justified string
    """

    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if is_word_fits_in_line(current_line, word, width):
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]
    lines.append(current_line)
    # print(lines)

    spaced_lines = []
    for line in lines:
        if line != lines[-1]:
            spaced_lines.append(add_spaces_to_line(line, width))
    lastline = ' '.join(lines[-1])
    spaced_lines.append(lastline)

    return '\n'.join(spaced_lines)



testtext = 'Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc.'
testtext4 = "EJFWleB HZiGZU vHbIwMVdU mbJNjGjq PDMZU yUpAbQB MZxlGLQK WDlmuDZy aJxIhUG u Kj inISaAq McH ndrnPKy NDJhP wxSi jtLv bwfwAjY My aXyX ZWIDouEq rrLoTBab P ASJR xnUCRDoKM cmkBK wpGJufPKAa foXoJANl ihmzskJud WnnTJsvix jDcu KrU J"
# print(justify(testtext4, 33))


testtext = 'Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc.'
testtext1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
testtext2 = """
MrYzGuMss dOA Pojy xyeSeCV r c QPdgsDJC MzTBuwwEEh BiSWYoVi THsWD bOcYoES g fQszTG LhTNIqbr QpNSSYn GAfYc jGJbczsyV l OONmNqR Ubw M slup vyIzXm KaloLEK HvNpEKfB kiRMfHhWi Gwt efnJ dNlZ ZV D Tfpmvmpn K bZW W afuBuqBB ujjsVN rgcqVFlh royAGAl lDjXQuyn ZSmOPstK vmCd"""
testtext3 = """
plBHQbf voRrlhsSg WNb qnLoEiMQE UlUf zFfdVB IGdzbA HnAlSCva Syg mTTAyNrX tdCVNKSiPB lYTmlrsuZu XyEZc oD PyPZsaeG lLAwNaol mNweqnsSwY OImm xnJFlq JUnpm hTycwr lnTkZSzak PHahUQx O KZamIsEg DO gDLprLY vjZIN NfrlJHDe Yihtzs A H XhihuVytAF EIPqf jGsPdS gFeczUrTOl lRCkdsEi HjwT HwNt mAoDUAfaU s BqY
"""


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

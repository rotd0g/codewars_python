"""
Write a function that,
given a string of text (possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words,
in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, backslash, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words,
then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
"""



def top_3_words(text):
    if not text:
        return []

    cleantext = ''

    alphabet = "'abcdefghijklmnopqrstuvwxyz"

    text = text.lower()

    for s in text:
        if s in alphabet:
            cleantext += s
        else:
            cleantext += ' '
    # print(cleantext)
    if cleantext[-1] == ' ':
        cleantext = cleantext.strip()

    result = cleantext.split()
    finalresult = {}

    for word in result:
        if len(word) == word.count("'"):
            continue
        counter = result.count(word)
        # print(word, counter)
        finalresult[word] = counter



    finalresult = sorted(finalresult.items(), key= lambda x: x[1], reverse=True)[0:3]

    # print(finalresult)
    top3 = []
    for key in finalresult:
        top3.append(key[0])

    return top3

print(top_3_words("""In' '' a village ''''' of La Mancha, the name of which I have no desire to call to
mind, there lived not long ' since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad of on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))

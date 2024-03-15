"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""

def order(sentence):
    if not sentence:
        return ''
    order_str = []
    words = sentence.split(' ')
    # print(words)

    for i in range(1, len(words)+1):
        for word in words:
            if str(i) in word:
                order_str.append(word)
    # print(order_str)
    return ' '.join(order_str)

print(order("is2 Thi1s T4est 3a"))

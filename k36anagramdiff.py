"""
  Given two words, how many letters do you have to remove from them to make them anagrams?
  Example
  First word : c od e w ar s (4 letters removed)
  Second word : ha c k er r a nk (6 letters removed)
  Result : 10
  Hints
  A word is an anagram of another word if they have the same letters (usually in a different order).
  Do not worry about case. All inputs will be lowercase.
  """

# 1. first check if every letter of word1 is in word2
# 2. if it's not count letters to be removed
# 3. check if every letter of word2 is in word1
# 4. if it's not + count letters to be removed
# 5. return result

def anagram_difference(w1, w2):
    result = 0

    dictword1 = {k:w1.count(k) for k in w1}
    print(dictword1)

    dictword2 = {k: w2.count(k) for k in w2}
    print(dictword2)

    for letter, count in dictword1.items():
        if letter in dictword2 and count != dictword2[letter]:
            result += abs(count - dictword2[letter])
            print(result)



    for letter in w1:
        if letter not in w2:
            print(letter)
            result += 1
        # elif w2.count(letter) > 1:
        #     repeats += 1
        #     w2.remove(letter)
            print(w2, result)


    for letter in w2:
        if letter not in w1:
            print(letter)
            result += 1
        # elif w1.count(letter) > 1:
        #     repeats += 1
        #     w1.remove(letter)
            print(w1, result)
    return result

    # the number of characters to remove from w1 and w2 to make them anagrams of each other

print(anagram_difference('bovbwb', 'dgbnl'))

"""
import codewars_test as test
from solution import anagram_difference

sample_test_cases = (
    ('', '', 0),
    ('a', '', 1),
    ('', 'a', 1),
    ('ab', 'a', 1),
    ('ab', 'ba', 0),
    ('ab', 'cd', 4),
    ('codewars', 'hackerrank', 10)
)

@test.describe('Sample tests')
def sample_tests():
    @test.it('')
"""
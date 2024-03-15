def to_jaden_case(string):
    if not string:
        return string

    j_string = string[0].upper()
    index_after_space = [0]

    for i in range(len(string)):
        if string[i] == " ":
            index_after_space.append(i+1)
            j_string += " " + string[i+1].upper()
        else:
            if i not in index_after_space:
                j_string += string[i].lower()
    return j_string

#print(index_after_space)

print(to_jaden_case("HOW   CAN MIRRORS BE REAL  IF OUR EYES AREN'T REAL"))






"""
from solution import to_jaden_case
import codewars_test as test


@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")"""
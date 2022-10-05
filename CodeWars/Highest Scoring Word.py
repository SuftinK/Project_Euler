import string

def high(x) -> str:
    letters = string.ascii_lowercase
    ch_dict = dict()
    ch_count = 1
    for i_ch in letters:
        ch_dict[i_ch] = ch_count
        ch_count += 1

    answer_score = 0
    answer = str()
    for i_word in x.split(" "):
        i_word_value= 0
        for i_ch_value in i_word:
            i_word_value += ch_dict.get(i_ch_value)
        if i_word_value > answer_score:
            answer_score = i_word_value
            answer = i_word

    return answer

print(high("d bb"))

"""@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")"""
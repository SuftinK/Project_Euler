def binary_to_string(binary) -> str:
    answer_list = [binary[x:x + 8] for x in range(0, len(binary), 8)]
    temp = list(map(lambda x: int(x, 2), answer_list))
    temp2 = list(map(lambda x: chr(x), temp))
    answer = "".join(temp2)
    return answer

"""test.assert_equals(binary_to_string('0100100001100101011011000110110001101111'), 'Hello')
test.assert_equals(binary_to_string('00110001001100000011000100110001'), '1011')"""

a = '0100100001100101011011000110110001101111'
b = '00110001001100000011000100110001'

print(binary_to_string(b))
def reverse_alternate(string) -> str:
    answer = string.split(" ")
    print(answer)
    res = list()
    for j in range(0, len(answer)):
        if len(answer[j]) != 0:
            res.append(answer[j])
    print(res)
    for i in range(0, len(res)):
        if i % 2 != 0:
            res[i] = res[i][::-1]
    answer = (" ".join(res))
    return answer

"""test.describe("Basic tests")
test.assert_equals(reverse_alternate("Did it work?"), "Did ti work?")
test.assert_equals(reverse_alternate("I really hope it works this time..."), "I yllaer hope ti works siht time...")
test.assert_equals(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
test.assert_equals(reverse_alternate("Have a beer"), "Have a beer")
test.assert_equals(reverse_alternate(""), "")"""

print(reverse_alternate("This       si a  test "))
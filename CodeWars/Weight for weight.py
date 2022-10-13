def sum_of_numb(s:str) -> int:
    s_l = [int(x) for x in s]
    return sum(s_l)

def order_weight(strng):
    s_n_l = [(sum_of_numb(x), x) for x in strng.split(" ") if x!=""]
    answer_l = [x[1] for x in sorted(s_n_l)]
    return " ".join(answer_l)

a = "   103 123   4444 99 2000 "
b = "2000 10003 1234000 44444444 9999 11 11 22 123"
print(order_weight(b))

"""test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
        test.assert_equals(order_weight(""), "")"""
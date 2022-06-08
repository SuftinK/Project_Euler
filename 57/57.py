"""
Можно убедиться в том, что квадратный корень из двух можно выразить в виде бесконечно длинной дроби.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

Приблизив это выражение для первых четырех итераций, получим:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985, является первым случаем, в котором количество цифр в числителе превышает количество цифр в знаменателе.

У скольких дробей длина числителя больше длины знаменателя в первой тысяче приближений выражения?
"""
import time
from decimal import Decimal
from math import *
from fractions import Fraction
import sys

sys.setrecursionlimit(10000)

# print(Fraction(10,20) + Fraction(20, 10))

# print(f"Квадратный корень из 2 = {2**0.5}")

start = time.time()
res_list = list()


def recursia(n):
    if len(res_list) == n:
        return 2
    # temp = n + 1/2
    res_list.append(1)
    # print(res_list, len(res_list))
    a = Fraction(2) + Fraction(1, recursia(n))

    # print(f" {a}")
    return a


count = 0
for i in range(1000):
    res_list = list()
    temp = recursia(i)
    answer = Fraction(1) + Fraction(1, temp)

    # print(f"{i+1}) {answer.numerator}")
    if len(str(answer.numerator)) > len(str(answer.denominator)):
        print(f"{i + 1}) {answer}")
        count += 1

finish = time.time() - start
print(
    f"Было найдено {count} дробей, где длинна числителя в символах больше длинны знаминателя. \n "
    f"Потрачено времени - {round(finish, 2)} сек.")
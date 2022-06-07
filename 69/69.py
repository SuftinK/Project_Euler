"""Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n, которые взаимно просты с n. К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.

n	Взаимно простые числа	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.

Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
"""

from math import *
import time

start = time.time()

dictionary = dict()
for i in range(2, 1000001):

    for j in range(i, 1, -1):
        if gcd(i, j) == 1:
            if i in dictionary:
                dictionary.get(i).append(j)
            else:
                dictionary[i] = [1]
                dictionary.get(i).append(j)

print(dictionary)
maximum = 0
maximum_i = 0
maximum_len = 0
maximum_comb = list()
for k, v in dictionary.items():
    temp = k / len(v)
    print(f"k = {k}, v = {v}, len(v) = {len(v)}, k / len(v) = {temp}")
    if temp > maximum:
        maximum = temp
        maximum_i = k
        maximum_len = len(v)
        maximum_comb = v[:]

print(f"Ответ: максимум n/φ(n)={maximum} наблюдается при n={maximum_i}, \nдлинна взаимно простых чисел ={maximum_len}\n"
      f"Сама комбинация = {maximum_comb}")
print(f"Задача выполнялась {time.time() - start} секунд.")
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

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def relatively_prime(i:int, m:int):
    count = 0
    extrem = i // m
    for j in range(i, 0, -1):
        if gcd(i, j) == 1:
            count += 1
            if count > extrem:
                return 0
    answer = i / count
    return answer


start = time.time()

maximum = 2
answer = 1

for i in range(400000, 1, -1):

    temp = relatively_prime(i, maximum)
    #print(f"temp {temp}, max = {maximum}")
    if temp >= maximum:
        maximum = temp
        answer = i
        print(f"При n = {answer}, max обновлен {maximum}")
    else:
        continue

print(f"При n = {answer}, max = {maximum}")
#print(f"Первая часть задачи выполнена за {time.time() - start} сек.")

# ответ 510510
print(f"Задача выполнялась {round(time.time() - start, 2)} секунд.")
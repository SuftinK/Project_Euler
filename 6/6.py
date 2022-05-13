"""Сумма квадратов первых десяти натуральных чисел равна

12 + 22 + ... + 102 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел."""


import time

start = time.time()
n = 100

def sum_of_pow(n:int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += pow(i, 2)
    return sum

summ_of_pow = sum_of_pow(n)
print(summ_of_pow)

def pow_of_sum(n:int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return pow(sum,2)

pow_of_summ = pow_of_sum(n)
print(pow_of_summ)

answer = pow_of_summ - summ_of_pow

print(answer)

print(f"this problem realization took me {round(time.time() - start, 2)} sec.")
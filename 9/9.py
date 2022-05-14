"""Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a2 + b2 = c2
Например, 32 + 42 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc. """

import math
import time

start = time.time()

for a in range(1, 333):
	for b in range(a +1, 500):
		c = math.sqrt(pow(a,2) + pow(b,2))
		if a + b + c == 1000:
			print(f"a={a}, b={b}, c={c} and a*b*c={a*b*c}")
			break


print(f"this problem realization took me {round(time.time() - start, 2)} sec.")
"""
Квадратный корень из 2 можно записать в виде бесконечной непрерывной дроби.

√2 = 1 +
1
 	2 +
1
 	 	2 +
1
 	 	 	2 +
1
 	 	 	 	2 + ...
Бесконечную непрерывную дробь можно записать, воспользовавшись обозначением √2 = [1;(2)], где (2) указывает на то, что 2 повторяется до бесконечности. Подобным образом, √23 = [4;(1,3,1,8)].

Оказывается, что последовательность частичных значений непрерывных дробей предоставляет наилучшую рациональную аппроксимацию квадратного корня. Рассмотрим приближения √2.

1 +
1
= 3/2

2

1 +
1
= 7/5
 	2 +
1

2

1 +
1
= 17/12
 	2 +
1

 	 	2 +
1


2

1 +
1
= 41/29
 	2 +
1
 	 	2 +
1

 	 	 	2 +
1


2

Таким образом, последовательность первых десяти приближений для √2 имеет вид:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
Самое удивительное, что важная математическая константа
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

Первые десять членов последовательности приближений для e перечислены ниже:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
Сумма цифр числителя 10-го приближения равна 1 + 4 + 5 + 7 = 17.

Найдите сумму цифр числителя 100-го приближения непрерывной дроби для e.
"""

import time


start = time.time()

# n_i = m_i * n_i-1 + n_i-2

b = [x for x in range(102) if x % 2 == 0 and x != 0]

m_list = [1] * 2

for i in b:
	m_list.append(i)
	m_list.append(1)
	m_list.append(1)

e_list = [2, 3]

for i_elem in range(100):
    if i_elem < 2:
        continue
    else:
        i = m_list[i_elem] * e_list[i_elem-1] + e_list[i_elem-2]
        e_list.append(i)


answer = e_list[99]

answer_sum = list(map(int,str(answer)))

print("Ответ: сумма чисел в числителе 100 приближения числа е =", sum(answer_sum))


print(f"Задача решена за {round((time.time() - start),2)} сек.")
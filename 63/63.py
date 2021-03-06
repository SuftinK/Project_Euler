"""Пятизначное число 16807 = 7^5 является также пятой степенью натурального числа. Аналогично, девятизначное число 134217728 = 8^9 является девятой степенью.

Сколько существует n-значных натуральных чисел, являющихся также и n-ми степенями натуральных чисел?
"""
count = 0
for i_numb in range(1, 300):

    for i_step in range(1, 300):
        temp = i_numb ** i_step

        if len(str(temp)) == i_step:
            count += 1
            print(f"{count}) {temp} = {i_step}")

print(f"Всего было найдено {count} чисел.")
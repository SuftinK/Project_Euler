import time
import math

start = time.time()

x_max = 0
a = 1001
d_answer = 0
y_max = 0
# answer_list = list()
for d in (x for x in range(2, a) if x ** 0.5 % 1 != 0):
    print("d=", d)
    y_in = 1
    while True: # шенерируем саисок квадратов для y
        y = y_in ** 2
        k = 1 + d * y

        x = math.sqrt(k)
        if x % 1 == 0:

            if x > x_max:
                print(f"Найден новый максимальный х при d={d} x={x} y={y}")
                x_max = x
                d_answer = d
                y_max = y_in
            print(f"Breake при d= {d}, x= {int(x)}, y= {y_max}")
            break

print(f"Ответ = {d_answer} при максимальном x = {int(x_max)}. \nРешение потребоволо {time.time() - start} сек.")

"""y= 10000000000
Ответ = 934 при максимальном x = 3034565. 
Решение потребоволо 860.2241826057434 сек."""


"""y= 1000000000000
Ответ = 688 при максимальном x = 24248647. 
Решение потребоволо 4914.718577861786 сек."""
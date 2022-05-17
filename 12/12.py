import math, time
ti = time.time()
import math

t_n, step = 0, 0
while True:
    step += 1
    t_n += step
    cnt = 2
    for i in range(2, int(t_n ** (0.5)) + 1):
        if t_n % i == 0:
            cnt += 2

    if cnt > 500:
        print(t_n, cnt)
        break
print("Time taken(secs):", time.time() - ti)
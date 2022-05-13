"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import time

start = time.time()

def divided_with_out_remainder(n:int) -> bool:
    n_str = str(n)
    if int(n_str[len(n_str)-1:]) != 0:
        return False
    if n % 2 != 0:
        return False
    for i in range(3, 20):
        if n % i != 0:
            return False
    return True

count = 1
while True:
    if divided_with_out_remainder(count):
        break
    count += 1

print(f"answer is {count}")

print(f"this problem realization took me {round(time.time() - start, 2)} sec.")

# answer is 232792560
# this problem realization took me 100.15 sec.

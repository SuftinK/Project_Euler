from itertools import *

def sc_perm_comb(num):
    num = str(num)
    res = list()

    for j in range(1, len(num) + 1):
        for i in permutations(num, j):
            if i[0] == "0":
                continue
            res.append(int("".join(i)))
    return sum(list(set(res)))



print(sc_perm_comb(333))
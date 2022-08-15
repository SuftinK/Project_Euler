from itertools import permutations as perm

def proc_arr(arr):
    answ = set()
    for i in perm(arr):
        temp = int("".join(i))
        answ.add(temp)
        res = list(answ)
    return [len(res), min(res), max(res)]

a = ['1','2','2','3','2','3']

print(proc_arr(a))
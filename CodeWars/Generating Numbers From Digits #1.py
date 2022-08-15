from itertools import permutations as perm

# def proc_arr(arr):
#     answ = set()
#     for i in perm(arr):
#         temp = int("".join(i))
#         answ.add(temp)
#     return [len(answ), min(answ), max(answ)]

def proc_arr(arr):
    answ = set(int("".join(i)) for i in perm(arr))
    return [len(answ), min(answ), max(answ)]

a = ['1','2','2','3','2','3']
b = ['8', '7', '6', '4', '2', '2', '1'] #[2520, 1224678, 8764221]
c = ['1','2','3','0','5','1','1','3'] #[3360, 1112335, 53321110]

print(proc_arr(c))
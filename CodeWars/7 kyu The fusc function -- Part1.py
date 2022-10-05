def fusc(n):
    assert type(n) == int and n >= 0
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    res = int()
    if n % 2 == 0:
        res += fusc(int(n/2))
    else:
        res += fusc(int(n/2)) + fusc(int(n/2)+1)
    return res

print(fusc(0))
print(fusc(1))
print(fusc(85))

for i in range(21):
    print(fusc(i), end=", ")
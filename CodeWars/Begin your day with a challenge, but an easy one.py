def one_digit_gen(n):
    return int(n * "1")


def nines(n):
    if n % 9 == 0:
        return int("9" * (n // 9))
    i = round(n / 9, 3)
    i_n = str(i).split(".")
    i_nines = i_n[0]
    the_rest = i_n[1][0]
    res = "9" * int(i_nines) + the_rest
    return int(res)


def one_two_three(n):
    if n == 0:
        return [0, 0]
    elif 0 < n < 10:
        return [n, one_digit_gen(n)]
    else:
        return [nines(n), one_digit_gen(n)]
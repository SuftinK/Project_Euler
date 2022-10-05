
def time_in_seconds(l: list) -> int:
    if len(l) == 0:
        return 0
    s_h = int(l[0]) * 3600
    s_m = int(l[1]) * 60
    s = int(l[2])
    total_time: int = s_h + s_m + s
    return total_time


def zero_add(x:int) -> str:
    if len(str(x)) < 2:
        return "0" + str(x)
    return str(x)


def time_back(x: int) -> str:
    h = x // 3600
    m = (x - (h * 3600)) // 60
    s = x - (h * 3600) - (m * 60)
    result = zero_add(h) + "|" + zero_add(m) + "|" + zero_add(s)
    return result


def stat(strg):
    strg = strg.replace(" ", "")
    strg_list = strg.split(",")
    strg_list_2 = [x.split("|") for x in strg_list]
    strg_in_sec_list = sorted([time_in_seconds(x) for x in strg_list_2])
    strq_len = len(strg_in_sec_list)
    range = max(strg_in_sec_list) - min(strg_in_sec_list)
    average = sum(strg_in_sec_list) / strq_len
    ind = strq_len // 2
    if strq_len % 2 == 0:
        median = (strg_in_sec_list[ind - 1] + strg_in_sec_list[ind]) / 2
    else:
        median = strg_in_sec_list[ind]
    return f"Range: {time_back(range)} Average: {time_back(int(average))} Median: {time_back(int(median))}"


a = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"  # "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"
b = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"  # "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00"
print("Test of function ", stat(b))
# print(a)
# a = a.replace(" ", "")
# print(a)
# aa = a.split(",")
# print("aa", aa)
#
# # a_list = list(aa)
# # print("list t ", a_list)
#
# aaa = aa[0].split("|")
# print("aaa", aaa)

#
# t = datetime.strptime(aa[0], "%H|%M|%S")
# tt = datetime.strptime(aa[1], "%H|%M|%S")
# # t = time.strftime("%H|%M|%S")
#
# t_list = [datetime.strptime(x, "%H|%M|%S") for x in aa]
# print(t_list)
# dth = t.hour
# dth2 = tt.hour
# dthr = dth + dth2
# print("H= ", dth, "H2= ", dth2, "H3= ", dthr)
# # z = timedelta(t_list[0] - t_list[4]) #t_list[0] - t_list[4]
# # print(z)
# # tt = t("01|15|59")
# print(t.time(), type(t.time()))
# print(tt.time(), type(tt.time()))
# ttt = tt - t
# ttt_str = str(ttt)
# result = ttt_str.split(":")
# r = ("|").join(result)
# print(r, type(r))

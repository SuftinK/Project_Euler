import string

def is_a_valid_message(message):
    num = string.digits
    num_list = [int(x) for x in num]
    if len(message) == 0:
        return True
    elif message[0] not in num:
        return False
    res_dict = dict()
    for i_ch in message:
        ch_count = 0
        if i_ch in num:
            temp = int(i_ch)

        else:
            ch_count += 1
    pass

a = "3hey5hello2hi"
b = "fg"
print(b[0])

print(is_a_valid_message(b))
# num = string.digits
# print([int(x) for x in num])
# if str(5) in a:
#     print("Yes")
#
# for i in a:
#     print(i)
#     if i in num:
#         print("Yes")
def clean_string(s):
    s_list = list(s)
    while True:
        if s == "":
            return "Пусто"
        elif set(s) == {"#"}:
            return "Одни решетки"
        elif "#" not in s_list:
            return "".join(s_list)
        else:
            index = s_list.index("#")
            if index == 0:
                s_list.pop(index)
            else:
                s_list.pop(index)
                s_list.pop(index-1)



# print(clean_string(""))
# print(clean_string("####"))

a = "abc##d"
# b = set(a)
# print(b)
print(clean_string(a))
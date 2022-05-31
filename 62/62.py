"""Можно найти перестановки куба 41063625 (3453), чтобы получить еще два куба: 56623104 (3843) и
66430125 (4053). К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами."""


def int_sorted(i: int) -> list:
    sort_i = sorted(list(str(i)))
    return tuple(sort_i)


# организуем цикл, в нем возводим в 3 степень. ответ собираем в словарь. делаем проверку на кол-во найденных корней 3 степени для одного ключа

# словарь для хранения всех найденных кубов
dic = dict()

for i_numb in range(10000):
    kub = i_numb ** 3
    combination = int_sorted(kub)
    if combination not in dic:
        dic[combination] = []
        dic[combination].append([kub, i_numb])
    else:
        dic[combination].append([kub, i_numb])

    if len(dic[combination]) >= 5:
        print(sorted(dic[combination]))
        break
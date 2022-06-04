
import time
from itertools import *

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
            if k%i==0:
            	return False
    return True



start = time.time()

# Шаг 1 создаем функцию и с ее помощью словарь комбинаций для чисел с длинной от 3 до 10 символов
def combination_generator(l:str) -> list:
	"""Эта функция принимает строку из нулей и 11 и делает на выходе список с возможными комбинациями. далее они используются для замены на цифры"""
	l2 = set()
	for i in permutations(l):
		temp = "".join(list(i))
		l2.add(temp)
	return sorted(list(l2))
	
# создадим словарь с комбинациями для дальнейшего удобного использования
dict_comb = dict()
for i_numb in range(4,11):
	n = "111" + "0" * (i_numb-3)
	i_comb = combination_generator(n)
	dict_comb[i_numb] = i_comb

print(f"Получился словарь с комбинациями \n {dict_comb[5]}")
# ==========Шаг1 завешен==============

# Шаг 2 Создаем функцию замены числа

def number_changer(list_original:list, list_comb:list, numb_to_change:int) -> int:

	for i in range(len(list_comb)):
		if int(list_comb[i]) == 0:
			continue
		elif int(list_comb[i]) == 1:
			list_original[i] = str(numb_to_change)
		else:
			print("ошибка")
			return False

	return int("".join(list_original))


# ===Шаг2 завершен ========

#Шаг3 запуск перебора		
final_answer = list()
# перебераем числа грубым перебором	
for i_number in range(1000, 1000000000):
	if len(final_answer) > 0:
		break
	#перебераем все комбинации для n-значного числа. берем лист с комбинациями из словаря который подготовили на шаге 1
	for i_combination in dict_comb[len(str(i_number))]:
		# перебираем подставляемые числа от 0 до 9
		count = 0
		answer_list = []
		for i_numb_to_change in range(10):
			temp = number_changer(list(str(i_number)), list(i_combination), i_numb_to_change)
			print(temp)
			if isitPrime(temp) and (len(str(i_number)) == len(str(temp))):
				print(f"Найдено простое число {temp}")
				count += 1
				answer_list.append(temp)
		print(answer_list)
		if count >= 8:
			final_answer = answer_list[:]
			print("вышли по breake условию")
			print(final_answer)
			print(len(final_answer))
			break

print(f"задача решена. найдена семья чисел у которой при перестановок {len(final_answer)}чисел являются простыми")
print(sorted(final_answer))

# вышли по breake условию
# [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
# 8
# задача решена. найдена семья чисел у которой при перестановок 8чисел являются простыми
# [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
# this problem realization took me 375.96 sec.

# В данном решении этот алгоритм по генерации простых чисел не использовался
#def prime_sieve_Eratosthenes(N):

#    A=[True]*N
#    primelist=[]
#    A[0]=A[1]=False
#    for k in range(2,N):
#        if A[k]:
#            for m in range(2*k,N,k):
#                A[m]=False
#    for k in range(N):
#        if A[k]:
#            primelist.append(k)
#    return primelist

print(f"this problem realization took me {round(time.time() - start, 2)} sec.")
def polyndrom_check(n) -> bool:
	return True if str(n)[::-1] == str(n) else False

#print(polyndrom_check(a))
polyndrom_list = list()
for i in range(100, 1000):
	for j in range(100, 1000):
		temp = i * j
		if polyndrom_check(temp):
			polyndrom_list.append(temp)

print(f"the answer is {max(polyndrom_list)}")
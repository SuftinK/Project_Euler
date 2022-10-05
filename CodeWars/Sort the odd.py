def sort_array(source_array):
	odds = sorted([x for x in source_array if x % 2 != 0])
	temp2 = [x if x % 2 == 0 else "odd" for x in source_array]
	for i in range(len(temp2)-1, -1, -1):
		if temp2[i] == "odd":
			temp2[i] = odds.pop()
	return temp2

a = [5, 8, 6, 3, 4]
print(sort_array(a))
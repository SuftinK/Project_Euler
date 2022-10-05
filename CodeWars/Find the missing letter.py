import string

def find_missing_letter(chars):
	length = len(chars)
	first_ch = chars[0]
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	set_ch = set(chars)
	if 65 <= ord(chars[0]) <= 90:
		start = upper.index(first_ch)
		original_str = upper[start: start + length + 1]
		result = list(set(original_str) - set(chars))
		return result[0]

	start = lower.index(first_ch)
	original_str = lower[start: start + length + 1]
	result = list(set(original_str) - set(chars))
	return result[0]



a = ['a','b','c','d','f'] # 'e'
aa = ['a','b','c','d']
b = ['O','Q','R','S'] # 'P'

print(find_missing_letter(a))

#upper = string.ascii_uppercase # from 65 to 90
#lower = string.ascii_lowercase # from 97 to 122

#for i in lower: 
#	print(ord(i))

#print(set(upper))

#if "F" in upper:
#	print("yes")
#a1 = set(a)
#print(a1)
#a2 = set(aa)
#print(a2)
#print(a1 - a2)


# list_upper = list(upper)
# list_lower = list(lower)
# print(list_upper)
# upper_ord = list(map(lambda x: ord(x), list_upper))
# print(upper_ord)
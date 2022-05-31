"""Каждый символ в компьютере имеет уникальный код, предпочитаемым является стандарт ASCII (American Standard Code
for Information Interchange - Американский стандартный код для обмена информацией).
Для примера, A верхнего регистра = 65, звездочка (*) = 42, а k нижнего регистра = 107.

Современный метод шифровки состоит в том, что берется текстовый файл, конвертируется в байты по ASCII,
а потом над каждым байтом выполняется операция XOR с определенным значением, взятым из секретного ключа.
Преимущество функции XOR состоит в том, что применяя тот же ключ к зашифрованному тексту, получается исходный;
к примеру, 65 XOR 42 = 107, тогда 107 XOR 42 = 65.

Для невзламываемого шифрования ключ должен быть такой же длины, что и сам текст, и ключ должен быть составлен
из случайных байтов. Тогда, если пользователь хранит зашифрованное сообщение и ключ шифрования в разных местах,
то без обеих "половинок" расшифровать сообщение просто невозможно.

К сожалению, этот метод непрактичен для большинства пользователей, поэтому упрощенный метод использует в
качестве ключа пароль. Если пароль короче текстового сообщения, что наиболее вероятно, то ключ циклично
повторяется на протяжении всего сообщения. Идеальный пароль для этого метода достаточно длинный, чтобы быть
надежным, но достаточно короткий, чтобы его можно было запомнить.

Ваша задача была упрощена, так как пароль состоит из трех символов нижнего регистра.
Используя cipher1.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
содержащий зашифрованные коды ASCII, а также тот факт, что сообщение должно содержать распространенные
английские слова, расшифруйте сообщение и найдите сумму всех значений ASCII в исходном тексте."""
import string
from itertools import *
from functools import reduce
import math


def check(example:tuple, etalon:tuple) -> bool:
	"""Эта функция проверяет каждый элемент
	в получившейся расшифровке на значения. если значения получившихся элементов не соответствуют эталонному
	списку, и хотябы один из них отрицательный, то функция возвращает False. Если все элементы
	соответствуют, то возвращает True
	"""
	for i_elem in example:
		if (i_elem < 0) or (i_elem not in etalon):
			return False
	return True
#Тест для функции check
#print(check(a, letters_symbols_in_digits))


# чтобы найти сумму всех чисел в списке:
def summa(l:list) -> int:
	"""Эта функция находит финальную сумму всех элементов для итогового правильного ответа"""
	s = reduce(lambda x, y: x + y, l)
	return s


def chr_to_ord(t:tuple) -> list:
	"""Эта функция переводит все буквы в кортедже в их значения по уодеровке"""
	l_of_digits = [ord(x) for x in t]
	return l_of_digits


def ord_to_chr(t:tuple) -> list:
	"""Эта функция переводит все цифровые значения кодировки в кортедже в их  исходные значения"""
	l_of_chr = [chr(x) for x in t]
	return l_of_chr


def map_xor(a:tuple, b:tuple) -> list:
	c = map(lambda x, y: x ^ y, a, b)
	return tuple(c)


# откроем и прочитаем файл
with open("p059_cipher.txt", "r") as file:
	text = file.read()
	# переведем в список символов
	script = tuple(text.split(","))
	lenght = int((len(script) / 3))


# поменяем тип данных в списке с str на int и переведем в кортедж
script_int = tuple([int(x) for x in script])


# получим все мимволы нижнего региcтра и также все знаки припинания и добавим пробел
let = string.ascii_lowercase

lowercase = string.ascii_lowercase

uppercase = string.ascii_uppercase

digits = string.digits

punctuation = string.punctuation
punctuation += " "

letters_symbols_for_check= tuple(lowercase + uppercase + digits + punctuation)

letters_symbols_for_check_int = chr_to_ord(letters_symbols_for_check)


# организуем перебор вмех возможных комбинаций
count = 1
for i in permutations(let, 3):
	# получаем список числовых значений комбинации букв в картеже
	temp = chr_to_ord(i)
	#увеличивпем его до размерномти самого шифра
	temp2 = temp * lenght #список
	#применяем XOR
	text = map_xor(script_int, tuple(temp2))
	#проверяем на только правильные символы и буквы
	if check(text, tuple(letters_symbols_for_check_int)):
		unscript = ord_to_chr(text)
		unscript = "".join(unscript)
		#проверяем на популярные слова
		if "the" and "from" in unscript:
			print(f"The scripted text: \n {unscript},\n the password is: {i}")
			#находим сумму - ответ
			answer = summa(list(text))
			print(f"The answer is: {answer}")

	count += 1

print("finish")
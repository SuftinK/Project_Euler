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
import math

with open("p059_cipher.txt", "r") as file:
	text = file.read()
	l = text.split(",")
print(len(l), l)

letters = string.ascii_lowercase
print(letters)



count = 1
for i in permutations(letters, 3):
	print(f"{count}) {i}")
	#i = int("".join(i))
	#print(f"{count}) {i}, {pow(i, 1/3)}")
	count += 1

print(chr(122), ord("z"))
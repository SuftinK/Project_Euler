import string

def alphabet_position(text) -> str:
    letters = string.ascii_lowercase
    letters_list = list(letters)
    only_text = "".join([x for x in text.lower() if x in letters])
    answer = [str(letters_list.index(x) + 1) for x in only_text]
    return " ".join(answer)


a = "The sunset sets at twelve o' clock."
b = "The narwhal bacons at midnight."
print(alphabet_position(b))

"""from random import randint
test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
"""


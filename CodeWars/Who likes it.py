def likes(names):
    l = len(names)
    if l == 0:
        return 'no one likes this'
    elif l == 1:
        return f'{names[0]} likes this'
    elif l == 2:
        return f'{names[0]} and {names[1]} like this'
    elif l == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    return f'{names[0]}, {names[1]} and {l - 2} others like this'

"""
@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
    """

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
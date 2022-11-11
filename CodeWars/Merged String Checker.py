def is_merge(s, part1, part2):
    print(s, part1, part2)
    if len(s) != len(part1 + part2):
     return False
    for i in s:
     print(i, type(i))
     if i not in part1 and i not in part2:
      return False
     elif len(part1) != 0 and i == part1[0]:
      print("yes", end="---")
      part1 = part1[1:]
      print(part1)
     elif len(part2) !=0 and i == part2[0]:
      print("O yes", end="---")
      part2 = part2[1:]
      print(part2)
     else:
      return False
    return True

print(is_merge('Can we merge it? Yes, we can!', 'Can eitYs ea', ' wemrge ? e,w cn!'))
#print(is_merge('codewars', 'cdw', 'oears'))
#print(is_merge('codewars', 'cod', 'wars'))

#('codewars', 'code', 'wars'), True)
#('codewars', 'cdw', 'oears'),True)
#('codewars', 'cod', 'wars'),False)
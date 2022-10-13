def number_decomposition(x:int):
    variation = [1000, 900, 500, 400, 100, 90, 50, 40, 10]
    answer = list()
    for i in variation:
          temp = x // i
          if temp > 0:
               x = x - i * temp
               answer.append([i, temp])
          else:
               continue
    if 0 < x < 10:
        answer.append([x, 1])
    return answer

#print(number_decomposition(1000))
def solution(n:int) -> str:
    d = {1:"I",
         2:"II",
         3:"III",
         4:"IV",
         5:"V",
         6:"VI",
         7:"VII",
         8:"VIII",
         9:"IX",
         10:"X",
         40:"XL",
         50:"L",
         90:"XC",
         100:"C",
         400:"CD",
         500:"D",
         900:"CM",
         1000:"M"
         }
    dec = number_decomposition(n)
    answer = str()
    for i_numb in dec:
        temp = str(d.get(i_numb[0])) * i_numb[1]
        answer += temp
    return answer

print(solution(1984))

"""def fixed_tests():
        test.assert_equals(solution(1),'I', "solution(1),'I'")
        test.assert_equals(solution(4),'IV', "solution(4),'IV'")
        test.assert_equals(solution(6),'VI', "solution(6),'VI'")
        test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
        test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
        test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
        test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        test.assert_equals(solution(1000), 'M', 'solution(1000), M')
        test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")"""
def multiplication_table(size) -> list:
    answer = [[x] for x in range(1, size + 1)]
    for i_list in answer:
        for y in range(2, size + 1):
            i_list.append(i_list[0] * y)
    return answer


print(multiplication_table(5))
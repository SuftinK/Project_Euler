import numpy as np

def print_matrix(a: list) -> None:
    for i_list in a:
        print(i_list)


def rotate(matrix: list, direction: str) -> list:
    len_row = len(matrix)
    len_elements = len(matrix[0])
    answer = list()
    if direction == "clockwise":
        for col in range(0, len_elements):
            temp = list()
            for row in range(len_row - 1, -1, -1):
                temp.append(matrix[row][col])
            answer.append(temp[:])

    elif direction == "counter-clockwise":
        for col in range(len_elements - 1, -1, -1):
            temp = list()
            for row in range(0, len_row):
                temp.append(matrix[row][col])
            answer.append(temp[:])
    return answer
matrix = [[1,2,3],[4,5,6], [7,8,9],[10,11,12]]
print_matrix(matrix)
test = np.rot90(matrix, 3).tolist()
print(type(test))
print(test)
#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#rotate(a, "counter-clockwise")
#print(rotate(matrix, "counter-clockwise"))
#rotate(a, "clockwise")
#print(rotate(matrix, "clockwise"))


# def rotate(matrix: list, direction: str) -> list:
#     print("Initial matrix is:")
#     print_matrix(matrix)
#     len_row = len(matrix)
#     len_elements = len(matrix[0])
#     answer = list()
#     if direction == "counter-clockwise":
#
#         for col in range(0, len_elements):
#             temp = list()
#             for row in range(len_row - 1, -1, -1):
#                 temp.append(matrix[row][col])
#             answer.append(temp[:])
#
#     elif direction == "clockwise":
#         for col in range(len_elements - 1, -1, -1):
#             temp = list()
#             for row in range(0, len_row):
#                 temp.append(matrix[row][col])
#             answer.append(temp[:])
#
#     print(f"{direction} matrix is:")
#     print_matrix(answer)
#     return answer
def transpose(matrix):
    new_matrix = []
    row_idx = len(matrix)
    for col_idx in range(len(matrix[0])):
        new_row = []
        for row in range(row_idx):
            new_row.append(matrix[row][col_idx])
        new_matrix.append(new_row)

    return new_matrix




        


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

print(transpose(matrix))

matrix_2_by_3 = [
    [3, 4, 1],
    [9, 7, 5]
]
print(transpose(matrix_2_by_3))

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
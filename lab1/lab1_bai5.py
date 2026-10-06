def gaussian_elimination(aug_matrix):
    matrix = [row[:] for row in aug_matrix]
    rows = len(matrix)
    cols = len(matrix[0])
    for k in range(min(rows, cols - 1)):
        pivot_row = max(range(k, rows), key=lambda i: abs(matrix[i][k]))
        if abs(matrix[pivot_row][k]) < 1e-12:
            continue
        matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
        for i in range(k + 1, rows):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, cols):
                matrix[i][j] -= factor * matrix[k][j]
    return [[round(value, 2) for value in row] for row in matrix]


augmented_matrix = [[2.0, 1.0, -1.0, 8.0], [-3.0, -1.0, 2.0, -11.0], [-2.0, 1.0, 2.0, -3.0]]
print("Ma trận bậc thang:")
for row in gaussian_elimination(augmented_matrix):
    print(row)
print("Độ phức tạp thời gian của khử Gauss với ma trận vuông n x n là O(n^3).")

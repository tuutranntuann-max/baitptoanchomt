def mat_mul_2x2(A, B):
    result = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_power_fast(P, D_diag, P_inv, k):
    D_k = [[D_diag[0] ** k, 0.0], [0.0, D_diag[1] ** k]]
    return mat_mul_2x2(mat_mul_2x2(P, D_k), P_inv)


P = [[2.0, 1.0], [1.0, -1.0]]
P_inv = [[1 / 3, 1 / 3], [1 / 3, -2 / 3]]
D_diag = [5, 2]
result = matrix_power_fast(P, D_diag, P_inv, 3)
print("A^3:")
for row in result:
    print([round(value, 2) for value in row])

def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])
    A_T = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            A_T[j][i] = A[i][j]
    return A_T


A = [[1, 2, 3], [4, 5, 6]]
print("Ma trận chuyển vị A_T:")
for row in transpose_matrix(A):
    print(row)

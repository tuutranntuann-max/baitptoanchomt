def matrix_multiply(A, B):
    if not A or not B or len(A[0]) != len(B):
        print("Lỗi: Số cột của A phải bằng số hàng của B")
        return None
    if any(len(row) != len(A[0]) for row in A) or any(len(row) != len(B[0]) for row in B):
        print("Lỗi: Ma trận không hợp lệ")
        return None
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    multiply_count = 0
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
                multiply_count += 1
    print("Tổng số phép nhân:", multiply_count)
    return C


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 1], [2, 3]]
print("Ma trận C:")
for row in matrix_multiply(A, B):
    print(row)

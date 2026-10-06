def matrix_vector_multiply(W, x):
    if not W or len(W[0]) != len(x):
        print("Lỗi: Số cột của W phải bằng số phần tử của x")
        return None
    y = []
    for row in W:
        if len(row) != len(x):
            print("Lỗi: Ma trận W không hợp lệ")
            return None
        total = 0
        for j in range(len(x)):
            total += row[j] * x[j]
        y.append(round(total, 10))
    return y


W = [[0.2, 0.5, -0.1], [0.8, -0.3, 0.4]]
x = [10, 2, 5]
print("Vector y:", matrix_vector_multiply(W, x))

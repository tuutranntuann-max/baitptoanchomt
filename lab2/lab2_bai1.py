def compute_linear_combination(B, c):
    if not B or len(B) != len(c):
        return None
    dim = len(B[0])
    v = [0.0] * dim
    for i in range(len(B)):
        if len(B[i]) != dim:
            return None
        for j in range(dim):
            v[j] += c[i] * B[i][j]
    return v


B = [[1, 0], [1, 1]]
c = [-2, 7]
print("Vector kết quả v:", compute_linear_combination(B, c))

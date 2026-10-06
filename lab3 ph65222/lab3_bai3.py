def mean_centering(X):
    rows = len(X)
    cols = len(X[0])
    means = []
    for j in range(cols):
        means.append(sum(X[i][j] for i in range(rows)) / rows)
    centered = []
    for row in X:
        centered.append([row[j] - means[j] for j in range(cols)])
    return centered


def compute_covariance_matrix(X_centered):
    rows = len(X_centered)
    cols = len(X_centered[0])
    if rows < 2:
        return None
    covariance = [[0.0 for _ in range(cols)] for _ in range(cols)]
    for i in range(cols):
        for j in range(cols):
            total = 0
            for k in range(rows):
                total += X_centered[k][i] * X_centered[k][j]
            covariance[i][j] = total / (rows - 1)
    return covariance


X = [[2, 4], [4, 8], [6, 10]]
centered = mean_centering(X)
print("Dữ liệu đã trừ trung bình:", centered)
print("Ma trận hiệp phương sai:")
for row in compute_covariance_matrix(centered):
    print([round(value, 2) for value in row])

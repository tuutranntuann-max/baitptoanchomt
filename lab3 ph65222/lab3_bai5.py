def mean_centering(X):
    means = [sum(row[j] for row in X) / len(X) for j in range(len(X[0]))]
    return [[row[j] - means[j] for j in range(len(row))] for row in X]


def compute_covariance_matrix(X_centered):
    rows = len(X_centered)
    cols = len(X_centered[0])
    return [[sum(X_centered[k][i] * X_centered[k][j] for k in range(rows)) / (rows - 1) for j in range(cols)] for i in range(cols)]


def normalize(vector):
    length = sum(value * value for value in vector) ** 0.5
    return [value / length for value in vector]


def matrix_vector_multiply(A, vector):
    return [sum(A[i][j] * vector[j] for j in range(len(vector))) for i in range(len(A))]


def power_iteration(A, start_vector, orthogonal_to=None, iterations=100):
    vector = normalize(start_vector)
    for _ in range(iterations):
        next_vector = matrix_vector_multiply(A, vector)
        if orthogonal_to is not None:
            dot = sum(next_vector[i] * orthogonal_to[i] for i in range(len(vector)))
            next_vector = [next_vector[i] - dot * orthogonal_to[i] for i in range(len(vector))]
        vector = normalize(next_vector)
    return vector


def pca_reduce_2d(data):
    centered = mean_centering(data)
    covariance = compute_covariance_matrix(centered)
    pc1 = power_iteration(covariance, [1.0] * len(covariance))
    pc2 = power_iteration(covariance, [1.0, -1.0, 1.0, -1.0], pc1)
    reduced = []
    for row in centered:
        reduced.append([sum(row[j] * pc1[j] for j in range(len(row))), sum(row[j] * pc2[j] for j in range(len(row)))])
    return reduced, covariance, pc1, pc2


medical_data = [[120, 95, 210, 24.5], [140, 130, 250, 29.0], [110, 85, 180, 21.5], [155, 160, 280, 32.0], [130, 105, 220, 26.0]]
eigenvalues = [145.2, 32.8, 4.5, 1.2]
reduced, covariance, pc1, pc2 = pca_reduce_2d(medical_data)
ratio = (eigenvalues[0] + eigenvalues[1]) / sum(eigenvalues)
print("Ma trận hiệp phương sai:")
for row in covariance:
    print([round(value, 3) for value in row])
print("PC1:", [round(value, 4) for value in pc1])
print("PC2:", [round(value, 4) for value in pc2])
print("Dữ liệu 2 chiều:")
for row in reduced:
    print([round(value, 3) for value in row])
print("Tỷ lệ phương sai giữ lại:", round(ratio * 100, 2), "%")
# Tỷ lệ trên 90% cho thấy hai chiều đầu giữ lại phần lớn thông tin quan trọng nên việc bỏ hai chiều cuối thường không làm thay đổi đáng kể bản chất dữ liệu. Biểu đồ 2D giúp chuyên gia y tế quan sát nhóm bệnh nhân và điểm bất thường dễ hơn.

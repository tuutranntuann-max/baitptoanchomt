def project_data_1d(X_centered, pc_vector):
    if not X_centered or len(X_centered[0]) != len(pc_vector):
        return None
    projections = []
    for row in X_centered:
        total = 0
        for j in range(len(pc_vector)):
            total += row[j] * pc_vector[j]
        projections.append(total)
    return projections


X_centered = [[-2, -3], [0, 0], [2, 3]]
pc_vector = [0.5547, 0.8321]
print("Dữ liệu sau khi chiếu:", [round(value, 4) for value in project_data_1d(X_centered, pc_vector)])

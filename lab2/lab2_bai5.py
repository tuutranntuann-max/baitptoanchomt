import math


def multiply_3x3(A, B):
    result = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result


def create_affine_matrix(sx, sy, angle_deg, tx, ty):
    rad = math.radians(angle_deg)
    scale = [[sx, 0.0, 0.0], [0.0, sy, 0.0], [0.0, 0.0, 1.0]]
    rotate = [[math.cos(rad), -math.sin(rad), 0.0], [math.sin(rad), math.cos(rad), 0.0], [0.0, 0.0, 1.0]]
    translate = [[1.0, 0.0, tx], [0.0, 1.0, ty], [0.0, 0.0, 1.0]]
    return multiply_3x3(translate, multiply_3x3(rotate, scale))


def transform_bounding_box(bbox, affine_matrix):
    result = []
    for x, y in bbox:
        new_x = affine_matrix[0][0] * x + affine_matrix[0][1] * y + affine_matrix[0][2]
        new_y = affine_matrix[1][0] * x + affine_matrix[1][1] * y + affine_matrix[1][2]
        result.append([round(new_x, 2), round(new_y, 2)])
    return result


# Tọa độ đồng nhất 3x3 gộp co giãn, xoay và tịnh tiến thành một phép nhân ma trận. Nhiều điểm ảnh có thể được xếp thành ma trận và GPU thực hiện các phép nhân giống nhau song song, giảm số bước xử lý.
bbox = [[0, 0], [2, 0], [2, 1], [0, 1]]
affine_matrix = create_affine_matrix(1.5, 1.5, 30, 5, 2)
print("Ma trận affine:")
for row in affine_matrix:
    print([round(value, 3) for value in row])
print("Bounding box mới:", transform_bounding_box(bbox, affine_matrix))

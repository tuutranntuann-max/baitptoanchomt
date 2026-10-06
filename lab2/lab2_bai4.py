import math


def scale_points(points, sx, sy):
    return [[round(x * sx, 2), round(y * sy, 2)] for x, y in points]


def rotate_points(points, angle_degrees):
    rad = math.radians(angle_degrees)
    cos_value = math.cos(rad)
    sin_value = math.sin(rad)
    result = []
    for x, y in points:
        new_x = x * cos_value - y * sin_value
        new_y = x * sin_value + y * cos_value
        result.append([round(new_x, 2), round(new_y, 2)])
    return result


points = [[1, 1], [2, 1], [2, 3], [1, 3]]
print("Sau khi co giãn:", scale_points(points, 2, 0.5))
print("Sau khi xoay 90 độ:", rotate_points(points, 90))

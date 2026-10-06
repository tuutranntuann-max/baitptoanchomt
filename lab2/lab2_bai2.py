def is_linearly_dependent_2d(v1, v2):
    det = v1[0] * v2[1] - v1[1] * v2[0]
    return abs(det) < 1e-9


print(is_linearly_dependent_2d([2, 4], [4, 8]))
print(is_linearly_dependent_2d([2, 4], [1, 5]))

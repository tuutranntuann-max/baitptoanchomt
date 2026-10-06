import math


def custom_grid_search(param_grid):
    keys = list(param_grid.keys())
    configurations = []

    def backtrack(index, current):
        if index == len(keys):
            configurations.append(dict(current))
            return
        key = keys[index]
        for value in param_grid[key]:
            current[key] = value
            backtrack(index + 1, current)
        current.pop(key, None)

    backtrack(0, {})
    return configurations


def count_configurations(param_grid):
    total = 1
    for values in param_grid.values():
        total *= len(values)
    return total


def dirichlet_collision(total_models, server_buckets):
    return math.ceil(total_models / server_buckets)


param_grid = {"learning_rate": [0.001, 0.01, 0.1], "batch_size": [16, 32, 64], "optimizer": ["Adam", "SGD"]}
configurations = custom_grid_search(param_grid)
print("Số cấu hình sinh được:", len(configurations))
print("Số cấu hình theo nguyên lý nhân:", count_configurations(param_grid))
for config in configurations:
    print(config)
minimum_same_bucket = dirichlet_collision(105, 10)
print("Ít nhất một cụm máy chủ chứa", minimum_same_bucket, "mô hình.")
print("Nếu phân phối không đều, một cụm phải xử lý nhiều mô hình hơn, làm tăng tải và thời gian chờ.")

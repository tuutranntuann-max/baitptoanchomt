def generate_subsets_backtracking(features):
    all_subsets = []

    def backtrack(start_index, current_path):
        all_subsets.append(list(current_path))
        for i in range(start_index, len(features)):
            current_path.append(features[i])
            backtrack(i + 1, current_path)
            current_path.pop()

    backtrack(0, [])
    return all_subsets


features = ["Age", "Income", "Score"]
subsets = generate_subsets_backtracking(features)
print("Tổng số tập con:", len(subsets))
for subset in subsets:
    print(subset)

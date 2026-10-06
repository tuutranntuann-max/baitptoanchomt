def generate_permutations(n):
    if n <= 0:
        return []
    a = list(range(1, n + 1))
    results = [a[:]]
    while True:
        i = n - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        if i < 0:
            break
        k = n - 1
        while a[k] <= a[i]:
            k -= 1
        a[i], a[k] = a[k], a[i]
        a[i + 1:] = reversed(a[i + 1:])
        results.append(a[:])
    return results


permutations = generate_permutations(3)
print("Tổng số hoán vị:", len(permutations))
for permutation in permutations:
    print(permutation)

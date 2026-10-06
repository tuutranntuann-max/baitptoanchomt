def generate_binary_strings(n):
    if n < 0:
        return []
    results = []
    a = [0] * n
    while True:
        results.append("".join(str(bit) for bit in a))
        i = n - 1
        while i >= 0 and a[i] == 1:
            a[i] = 0
            i -= 1
        if i < 0:
            break
        a[i] = 1
    return results


binary_list = generate_binary_strings(3)
print("Tổng số chuỗi:", len(binary_list))
print("Danh sách chuỗi:", binary_list)

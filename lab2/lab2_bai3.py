def rref(matrix):
    A = [[float(value) for value in row] for row in matrix]
    rows = len(A)
    cols = len(A[0])
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if abs(A[row][col]) > 1e-10:
                pivot = row
                break
        if pivot is None:
            continue
        A[pivot_row], A[pivot] = A[pivot], A[pivot_row]
        pivot_value = A[pivot_row][col]
        A[pivot_row] = [value / pivot_value for value in A[pivot_row]]
        for row in range(rows):
            if row != pivot_row:
                factor = A[row][col]
                A[row] = [A[row][j] - factor * A[pivot_row][j] for j in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return A


def find_kernel_basis_2x3(A):
    reduced = rref(A)
    pivot_cols = []
    for row in reduced:
        for col, value in enumerate(row):
            if abs(value) > 1e-9:
                pivot_cols.append(col)
                break
    free_cols = [col for col in range(3) if col not in pivot_cols]
    basis = []
    for free_col in free_cols:
        vector = [0.0, 0.0, 0.0]
        vector[free_col] = 1.0
        for row_index in range(len(pivot_cols) - 1, -1, -1):
            pivot_col = pivot_cols[row_index]
            vector[pivot_col] = -sum(reduced[row_index][j] * vector[j] for j in free_cols)
        basis.append([round(value, 6) for value in vector])
    return basis, len(basis)


A = [[1, 2, 3], [2, 4, 6]]
basis, nullity = find_kernel_basis_2x3(A)
print("Cơ sở Ker(f):", basis)
print("Số chiều Ker(f):", nullity)

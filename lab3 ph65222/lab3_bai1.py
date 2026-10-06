def verify_eigen(A, x, lambda_val, eps=1e-6):
    Ax = []
    for i in range(len(A)):
        total = 0
        for j in range(len(x)):
            total += A[i][j] * x[j]
        Ax.append(total)
    lambda_x = [lambda_val * value for value in x]
    is_valid = all(abs(Ax[i] - lambda_x[i]) < eps for i in range(len(Ax)))
    return is_valid, Ax, lambda_x


A = [[4, 2], [1, 3]]
x = [2, 1]
is_valid, Ax, lambda_x = verify_eigen(A, x, 5)
print("Ax:", Ax)
print("Lambda*x:", lambda_x)
print("x là vector riêng:", is_valid)

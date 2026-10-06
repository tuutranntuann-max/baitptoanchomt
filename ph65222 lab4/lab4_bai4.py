def solve_n_queens(n):
    solutions = []
    positions = [-1] * n
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                board.append("." * positions[r] + "Q" + "." * (n - positions[r] - 1))
            solutions.append(board)
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            positions[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return len(solutions), solutions


count, boards = solve_n_queens(4)
print("Tổng số cách xếp:", count)
for number, board in enumerate(boards, 1):
    print("Cách", number)
    for row in board:
        print(row)

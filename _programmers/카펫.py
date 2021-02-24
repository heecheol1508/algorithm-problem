def solution(brown, yellow):
    total = brown + yellow
    row_plus_col = brown // 2 + 2
    for col in range(1, int(total ** 0.5) + 1):
        row = row_plus_col - col
        if row * col == total:
            return [row, col]


print(solution(24, 24))

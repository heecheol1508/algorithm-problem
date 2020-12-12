def solution(matrix_sizes):
    n = len(matrix_sizes) + 1

    data = [matrix_sizes[0][0]] * n
    for i in range(n-1):
        data[i+1] = matrix_sizes[i][1]

    inf = float('inf')
    table = [[inf] * n for _ in range(n)]

    for i in range(n-1):
        table[i][i+1] = 0

    for i in range(n-2):
        table[i][i+2] = data[i] * data[i+1] * data[i+2]

    for d in range(3, n):
        for a in range(n-d):
            c = a + d
            for b in range(a+1, c):
                table[a][c] = min(table[a][c], table[a][b] + table[b][c] + (data[a]*data[b]*data[c]))

    answer = table[0][-1]

    return answer


print(solution([[5, 3], [3, 10], [10, 11], [11, 6]]))

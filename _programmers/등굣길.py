def solution(m, n, puddles):
    board1 = [[0] * m for _ in range(n)]
    board2 = [[1] * m for _ in range(n)]

    for [a, b] in puddles:
        board2[b-1][a-1] = 0

    for i in range(n):
        if board2[i][0] == 1:
            board1[i][0] = 1
        else:
            break

    for j in range(1, m):
        if board2[0][j] == 1:
            board1[0][j] = 1
        else:
            break

    for i in range(1, n):
        for j in range(1, m):
            if board2[i][j]:
                board1[i][j] = board1[i][j-1] + board1[i-1][j]

    return board1[n-1][m-1] % 1000000007


print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)
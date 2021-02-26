def solution(n, results):

    board = [['U'] * n for _ in range(n)]     # Unknown

    for [i, j] in results:
        board[i-1][j-1] = 'W'
        board[j-1][i-1] = 'L'

    for k in range(n):
        for i in range(n):
            if board[i][k] == 'U':
                continue
            for j in range(n):
                if board[i][j] == 'U' and board[i][k] == board[k][j]:
                    board[i][j] = board[i][k]

    for i in range(n):
        board[i][i] = '-'

    answer = 0

    for row in board:
        if 'U' not in row:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

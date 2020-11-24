def solution(n):
    N = sum(list(range(1, n + 1)))

    board = [[0] * n for _ in range(n)]
    adj_list = [(1, 0), (-1, -1), (0, 1)]

    idx1, idx2, d = 0, 0, 0
    board[0][0] = 1
    num = 1

    while num < N:
        num += 1
        for dd in range(3):
            nd = (d - dd) % 3
            nxt1, nxt2 = idx1 + adj_list[nd][0], idx2 + adj_list[nd][1]
            if 0 <= nxt1 < n and 0 <= nxt2 < n and board[nxt1][nxt2] is 0:
                board[nxt1][nxt2] = num
                idx1, idx2, d = nxt1, nxt2, nd
                break

    answer = []
    for i in range(n):
        answer.extend(board[i][:i+1])

    return answer


print(solution(5))

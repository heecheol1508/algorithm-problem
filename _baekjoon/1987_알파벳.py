import sys
sys.stdin = open('input.txt', 'r')


R, C = map(int, input().split())

board = [[] for _ in range(R)]
alphabet = set()


def alpha_to_int(alpha):
    return ord(alpha) - 65


for i in range(R):
    row = list(map(alpha_to_int, list(input())))
    board[i] = row
    alphabet.update(row)

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [False] * 26
visit[board[0][0]] = True

max_length = len(alphabet)
answer = 0


def dfs(idx1, idx2, cnt):
    global answer

    if cnt > answer:
        answer = cnt

    if answer == max_length:
        return

    for adj in adj_list:
        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
        if 0 <= nxt1 < R and 0 <= nxt2 < C and visit[board[nxt1][nxt2]] is False:
            visit[board[nxt1][nxt2]] = True
            dfs(nxt1, nxt2, cnt+1)
            visit[board[nxt1][nxt2]] = False


dfs(0, 0, 1)
print(answer)

import sys
sys.stdin = open('input.txt', 'r')


r1, c1, r2, c2 = map(int, input().split())
idx1, idx2 = -r1, -c1

r3, c3 = r2 - r1, c2 - c1

board = [['0'] * (c3+1) for _ in range(r3+1)]
cnt = (r3+1) * (c3+1)
num = 1

if 0 <= idx1 <= r3 and 0 <= idx2 <= c3:
    board[idx1][idx2] = str(num)
    cnt -= 1

edge = 1
d = 1
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while cnt > 0:
    edge += 1
    for _ in range(edge//2):
        num += 1
        idx1 += adj_list[d][0]
        idx2 += adj_list[d][1]
        if 0 <= idx1 <= r3 and 0 <= idx2 <= c3:
            board[idx1][idx2] = str(num)
            cnt -= 1
    d = (d-1) % 4

blank = '%{}s'.format(max(len(board[0][0]), len(board[r3][c3])), len(board[0][c3]), len(board[r3][0]))

answer = []
for i in range(r3+1):
    temp = []
    for j in range(c3+1):
        temp.append(blank % str(board[i][j]))
    answer.append(' '.join(temp))

print('\n'.join(answer))

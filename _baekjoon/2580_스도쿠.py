import sys
sys.stdin = open('input.txt', 'r')


board = [input().split() for _ in range(9)]
arr = []


def fill_blank(i, j):
    base = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    line = set()
    for k in range(9):
        line.add(board[i][k])
        line.add(board[k][j])

    box = set()
    for a in range((i // 3) * 3, (i // 3 + 1) * 3):
        for b in range((j // 3) * 3, (j // 3 + 1) * 3):
            box.add(board[a][b])

    return list(base - line - box)


def recursion(k):
    if k == len(arr):
        return True

    i, j = arr[k]
    for num in fill_blank(i, j):
        board[i][j] = num
        if recursion(k+1):
            return True
        else:
            board[i][j] = '0'

    return False


for x in range(9):
    for y in range(9):
        if board[x][y] == '0':
            res = fill_blank(x, y)
            if len(res) == 1:
                board[x][y] = res.pop()
            else:
                arr.append((x, y))

recursion(0)
for row in board:
    print(' '.join(row))




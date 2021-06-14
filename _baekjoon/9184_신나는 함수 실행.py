import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', 'r')


def w(i, j, k):
    if i <= 0 or j <= 0 or k <= 0:
        return 1
    if i > 20 or j > 20 or k > 20:
        return w(20, 20, 20)
    if dp[i][j][k] == 0:
        if i < j < k:
            res = w(i, j, k-1) + w(i, j-1, k-1) - w(i, j-1, k)
            dp[i][j][k] = res
            return res
        else:
            res = w(i-1, j, k) + w(i-1, j-1, k) + w(i-1, j, k-1) - w(i-1, j-1, k-1)
            dp[i][j][k] = res
            return res
    else:
        return dp[i][j][k]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
step = [int(input()) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0][1] = step[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + step[i]
    dp[i][2] = dp[i-1][1] + step[i]

print(max(dp[-1][1], dp[-1][2]))

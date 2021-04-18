import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    ti, pi = map(int, input().split())
    T[i] = ti
    P[i] = pi

dp = [0] * (N+1)
for i in range(N):
    dp[i] = max(dp[i], dp[i-1])
    j = i + T[i]
    if j <= N:
        dp[j] = max(dp[j], dp[i] + P[i])

print(max(dp[-1], dp[-2]))

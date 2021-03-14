import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
path = [[] for _ in range(N+1)]
dp = [[0] * 7 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    path[u].append(v)
    path[v].append(u)


def recursion(n, cnt):
    if dp[n][cnt] == 0:
        if cnt == 6:
            dp[n][cnt] = len(path[n])
        else:
            temp = 0
            for m in path[n]:
                temp += recursion(m, cnt + 1)
            dp[n][cnt] = temp

    return dp[n][cnt]


answer = 0
for i in range(1, N+1):
    if path[i]:
        answer += recursion(i, 0)

print(answer % (10**9 + 7))

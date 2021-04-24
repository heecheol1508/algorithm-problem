import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())

root = list(range(N+1))
for _ in range(M):
    u, v = map(int, input().split())
    root_u, root_v = root[u], root[v]

    if root_u > root_v:
        for i in range(1, N+1):
            if root[i] == root_u:
                root[i] = root_v
    elif root_v > root_u:
        for i in range(1, N+1):
            if root[i] == root_v:
                root[i] = root_u

answer = 0
for i in range(1, N+1):
    if i == root[i]:
        answer += 1
print(answer)

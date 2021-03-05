import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(20000)


N, M = map(int, input().split())
parent = list(range(N+1))
delete = 0


def find(v):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(x, y):
    global delete

    x, y = find(x), find(y)
    if x == y:
        delete += 1
    else:
        parent[x] = y


for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

group = -1
for i in range(1, N + 1):
    if parent[i] == i:
        group += 1

print(delete + group)

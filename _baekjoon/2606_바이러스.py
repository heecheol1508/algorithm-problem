# 14:43 ~ 14:48

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

visit = [False] * (N+1)
visit[1] = True
queue = [1]
while queue:
    cur = queue.pop(0)
    for nxt in edge[cur]:
        if visit[nxt] is False:
            visit[nxt] = True
            queue.append(nxt)

print(visit.count(True) - 1)

import sys
sys.stdin = open('input.txt', 'r')
# prim
import heapq


V, E = map(int, input().split())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([c, b])
    edges[b].append([c, a])

visit = [False] * (V+1)
visit[1] = True
queue = []
for k in range(len(edges[1])):
    val, node1 = edges[1][k]
    heapq.heappush(queue, (val, node1))

answer = 0
cnt = 0
while True:
    value, node2 = heapq.heappop(queue)
    if visit[node2]:
        continue
    else:
        visit[node2] = True
        answer += value
        for k in range(len(edges[node2])):
            val, node3 = edges[node2][k]
            heapq.heappush(queue, (val, node3))
        cnt += 1
        if cnt == V-1:
            break

print(answer)

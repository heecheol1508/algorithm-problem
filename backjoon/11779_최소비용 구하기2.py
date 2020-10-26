import sys
sys.stdin = open('input.txt', 'r')
import heapq
import collections


N = int(input())
E = int(input())

edges = collections.defaultdict(dict)

for _ in range(E):
    a, b, c = map(int, input().split())
    if b not in edges[a].keys():
        edges[a][b] = c
    elif c < edges[a][b]:
        edges[a][b] = c

inf = float('inf')
costs = [inf] * (N+1)

A, B = map(int, input().split())
queue = []

heapq.heappush(queue, [0, [A]])
costs[A] = 0

while queue:
    [cost, path] = heapq.heappop(queue)
    cur = path[-1]
    if cur == B:
        print(cost)
        print(len(path))
        answer = list(map(str, path))
        print(' '.join(answer))
        break

    if cost > costs[cur]:
        continue

    for nxt, fare in edges[cur].items():
        temp = cost + fare
        if temp < costs[nxt]:
            costs[nxt] = temp
            heapq.heappush(queue, [temp, path[:]+[nxt]])

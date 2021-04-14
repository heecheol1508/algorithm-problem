import sys
import heapq
sys.stdin = open('input.txt', 'r')


N, P, K = map(int, input().split())
nodes = [[] for _ in range(N+1)]
set_cost = set()

for _ in range(P):
    n1, n2, p = map(int, input().split())
    nodes[n1].append((n2, p))
    nodes[n2].append((n1, p))
    set_cost.add(p)


def dfs():
    queue = [1]
    visit = [False] * (N+1)
    visit[1] = True

    while queue:
        idx = queue.pop(0)
        if idx == N:
            return True
        for nxt, val in nodes[idx]:
            if visit[nxt] is False:
                visit[nxt] = True
                queue.append(nxt)
    return False


def dijkstra(w):
    queue = []
    heapq.heappush(queue, (0, 1))
    visit = [False] * (N+1)

    while queue:
        cnt, idx = heapq.heappop(queue)
        if cnt > K:
            return False
        if idx == N:
            return True
        if visit[idx]:
            continue
        visit[idx] = True
        for nxt, val in nodes[idx]:
            if visit[nxt]:
                continue
            if val > w:
                heapq.heappush(queue, (cnt+1, nxt))
            else:
                heapq.heappush(queue, (cnt, nxt))


def binary_search(left, right):
    if left == right:
        return left
    mid = (left + right) // 2
    if dijkstra(cost[mid]):
        return binary_search(left, mid)
    else:
        return binary_search(mid+1, right)


if dfs() is False:
    print(-1)
else:
    cost = sorted(list(set_cost))
    answer = binary_search(0, len(cost))
    if answer == 0:
        print(0)
    else:
        print(cost[answer])


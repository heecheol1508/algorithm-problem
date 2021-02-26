import heapq


def solution(n, costs):
    answer = 0
    connected = [False] * n

    bridges = [[] for _ in range(n)]
    for cost in costs:
        bridges[cost[0]].append([cost[1], cost[2]])
        bridges[cost[1]].append([cost[0], cost[2]])

    queue = []
    connected[0] = True
    for [a, b] in bridges[0]:
        heapq.heappush(queue, (b, a))

    while n > 1:
        cost, nxt = heapq.heappop(queue)
        if connected[nxt] is False:
            n -= 1
            connected[nxt] = True
            answer += cost
            for [a, b] in bridges[nxt]:
                heapq.heappush(queue, (b, a))

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

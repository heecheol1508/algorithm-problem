def solution(n, edge):

    near = [[] for _ in range(n+1)]
    for a, b in edge:
        near[a].append(b)
        near[b].append(a)

    visited = [False] * (n+1)
    queue = [1]
    visited[1] = True
    answer = 0

    while queue:
        flag = True
        for _ in range(len(queue)):
            cur = queue.pop(0)
            for nxt in near[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    if flag:
                        flag = False
                        answer = 0
                    answer += 1
                    queue.append(nxt)
        if flag:
            return answer

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

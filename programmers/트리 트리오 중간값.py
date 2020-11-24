import collections


def solution(n, edges):
    edge = [[] for _ in range(n+1)]

    for a, b in edges:
        edge[a].append(b)
        edge[b].append(a)

    visit = [False] * (n+1)
    node = 1
    visit[node] = True
    queue = collections.deque([node])

    while queue:
        num_root_node = len(queue)
        for _ in range(len(queue)):
            node = queue.popleft()
            for next_node in edge[node]:
                if visit[next_node] is False:
                    visit[next_node] = True
                    queue.append(next_node)

    # print(num_root_node)

    inf = float('inf')
    depth_of_tree = [inf] * (n+1)
    depth_of_tree[node] = 0
    queue = collections.deque([node])
    visit = [False] * (n+1)
    visit[node] = True

    depth = 0
    while queue:
        depth += 1
        num_leaf_node = len(queue)
        for _ in range(len(queue)):
            node = queue.popleft()
            for next_node in edge[node]:
                if visit[next_node] is False:
                    visit[next_node] = True
                    depth_of_tree[next_node] = depth
                    queue.append(next_node)

    # print(num_leaf_node)
    if num_root_node > 1 or num_leaf_node > 1:
        return depth - 1
    else:
        return depth - 2



print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))

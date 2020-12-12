import collections


def solution(n, path, order):

    near = collections.defaultdict(list)

    for i in range(n-1):
        a, b = path[i]
        near[a].append(b)
        near[b].append(a)

    b_list = [b for a, b in order]
    visited = [False] * n

    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop(0)
        for nxt in near[node]:
            if not visited[nxt] and nxt not in b_list:
                visited[nxt] = True
                queue.append(nxt)

    def is_possible(num):
        temp = set()
        temp.add(num)
        queue_temp = [num]
        while queue_temp:
            x = queue_temp.pop(0)
            for y in near[x]:
                if visited[y]:
                    return True
                elif y in b_list or y in temp:
                    continue
                else:
                    queue_temp.append(y)
                    temp.add(y)
        return False

    while True:
        flag_new_visit = False
        node_left = 0

        for i in range(len(order)-1, -1, -1):
            a, b = order[i]
            if visited[a]:
                if visited[b]:
                    order.pop(i)
                    b_list.pop(i)
                    continue
                if is_possible(b):
                    visited[b] = True
                    flag_new_visit = True
                else:
                    node_left += 1

            elif is_possible(a):
                visited[a] = True
                flag_new_visit = True
                if is_possible(b):
                    visited[b] = True
                else:
                    node_left += 1

            else:
                node_left += 1

        if node_left == 0:
            return True
        elif not flag_new_visit:
            return False


p = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
o = [[4,1],[8,7],[6,5]]
print(solution(9, p, o))

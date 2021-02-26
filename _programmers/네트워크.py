def solution(n, computers):
    network = [0] * n
    k = 0

    for i in range(n):
        if network[i] == 0:
            k += 1
            stack = [i]
            while stack:
                a = stack.pop()
                if network[a] == 0:
                    network[a] = k
                    for b in range(n):
                        if computers[a][b] == 1 and network[b] == 0:
                            stack.append(b)

    return k


print(solution(3, [[1, 0, 1], [0, 1, 1], [1, 1, 1]]))

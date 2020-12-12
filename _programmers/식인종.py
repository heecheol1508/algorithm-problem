def solution(n, m, p):
    if n > p or m > p:
        return -1
    queue = [[[n, m], [0, 0], [0, 0], 0, 0]]
    people_set = []

    while queue:
        island_A, boat, island_B, status, cnt = queue.pop(0)
        # print(island_A, boat, island_B, status)

        if status == 0:
            if 0 < island_A[0] <= p:
                queue.append([[0, island_A[1]], [island_A[0], 0], island_B, 1, cnt])
            if 0 < island_A[1] <= p:
                queue.append([[island_A[0], 0], [0, island_A[1]], island_B, 1, cnt])

        elif status == 1:
            cnt += 1
            if sum(island_A) == 0:
                return cnt
            temp = (island_A[0], island_A[1], island_B[0], island_B[1])
            if temp not in people_set:
                people_set.append(temp)
                queue.append([island_A, [0, 0], [island_B[0]+boat[0], island_B[1]+boat[1]], 2, cnt])

        elif status == 2:
            if island_B[0] == 0 and island_B[1] > 0:
                for b in range(1, min(island_B[1], p) + 1):
                    queue.append([island_A, [0, b], [0, island_B[1]-b], 3, cnt])
            elif island_B[1] == 0 and island_B[0] > 0:
                for b in range(1, min(island_B[0], p) + 1):
                    queue.append([island_A, [b, 0], [island_B[0]-b, 0], 3, cnt])
            if 0 < island_B[0] <= p:
                queue.append([island_A, [island_B[0], 0], [0, island_B[1]], 3, cnt])
            if 0 < island_B[1] <= p:
                queue.append([island_A, [0, island_B[1]], [island_B[0], 0], 3, cnt])

        elif status == 3:
            cnt += 1
            temp = (island_A[0], island_A[1], island_B[0], island_B[1])
            if temp not in people_set:
                people_set.append(temp)
                queue.append([[island_A[0]+boat[0], island_A[1]+boat[1]], [0, 0], island_B, 0, cnt])

    return -1


print(solution(2, 2, 1))

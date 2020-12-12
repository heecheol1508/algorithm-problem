def solution(key0, lock):
    m = len(key0)
    n = len(lock)

    new_lock = [[0] * (m+n-1) for _ in range(m+n-1)]
    holes = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i+m-1][j+m-1] = 1
            else:
                holes.append((i+m-1, j+m-1))

    def matching(a, b, key):
        for x, y in holes:
            if 0 <= x - a < m and 0 <= y - b < m and key[x - a][y - b] == 1:
                continue
            else:
                return False

        for x in range(m-1, m+n-1):
            for y in range(m-1, m+n-1):
                if new_lock[x][y]:
                    if 0 <= x - a < m and 0 <= y - b < m:
                        if key[x - a][y - b] == 0:
                            continue
                        else:
                            return False
        return True

    key90 = [[0] * m for _ in range(m)]
    key180 = [[0] * m for _ in range(m)]
    key270 = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            if key0[i][j]:
                key90[j][m-i-1] = 1
                key180[m-i-1][m-j-1] = 1
                key270[m-j-1][i] = 1

    for i in range(m+n-1):
        for j in range(m+n-1):
            if matching(i, j, key0) or matching(i, j, key90) or matching(i, j, key180) or matching(i, j, key270):
                return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

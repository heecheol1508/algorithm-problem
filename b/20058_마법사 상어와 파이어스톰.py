import sys
sys.stdin = open('input.txt', 'r')


N, Q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**N)]
storm = list(map(int, input().split()))

max_level = max(storm)
storm_type = list(set(storm))
size = 2**N

after_storm = [[[0] * (len(storm_type)+1) for _ in range(size)] for __ in range(size)]

for i in range(size):
    for j in range(size):
        for level in storm_type:
            L = 2**level
            da, a = divmod(i, L)
            db, b = divmod(j, L)

            na, nb = b, L - a - 1
            after_storm[i][j][level] = (na + L * da, nb + L * db)

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
temp_ice = [[0] * size for _ in range(size)]
for level in storm:
    if level > 0:
        for i in range(size):
            for j in range(size):
                ni, nj = after_storm[i][j][level]
                temp_ice[ni][nj] = ice[i][j]
    else:
        for i in range(size):
            for j in range(size):
                temp_ice[i][j] = ice[i][j]

    for i in range(size):
        for j in range(size):
            if temp_ice[i][j] == 0:
                ice[i][j] = 0
                continue
            cnt = 0
            for adj in adj_list:
                ni, nj = i + adj[0], j + adj[1]
                if 0 <= ni < size and 0 <= nj < size and temp_ice[ni][nj] > 0:
                    cnt += 1
            if cnt >= 3:
                ice[i][j] = temp_ice[i][j]
            else:
                ice[i][j] = temp_ice[i][j] - 1

total_ice = 0
max_size_of_ice = 0
for i in range(size):
    for j in range(size):
        if ice[i][j] > 0:
            total_ice += ice[i][j]
            ice[i][j] = 0
            queue = [(i, j)]
            cnt = 0
            while queue:
                idx1, idx2 = queue.pop(0)
                cnt += 1
                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < size and 0 <= nxt2 < size and ice[nxt1][nxt2] > 0:
                        total_ice += ice[nxt1][nxt2]
                        ice[nxt1][nxt2] = 0
                        queue.append((nxt1, nxt2))
            if cnt > max_size_of_ice:
                max_size_of_ice = cnt

print(total_ice)
print(max_size_of_ice)

import sys
sys.stdin = open('input.txt', 'r')


def find_the_nearest_customer(tx, ty, fuel):
    if board[tx][ty] > 1:
        customer_number = board[tx][ty]
        board[tx][ty] = 0
        return customer_number, tx, ty, fuel

    visit = [[False] * N for _ in range(N)]
    visit[tx][ty] = True
    customer_found = []
    queue = [(tx, ty)]
    while queue:
        fuel -= 1
        if fuel < 0:
            return False

        for _ in range(len(queue)):
            idx1, idx2 = queue.pop(0)
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N and visit[nxt1][nxt2] is False:
                    visit[nxt1][nxt2] = True
                    if board[nxt1][nxt2] == 0:
                        queue.append((nxt1, nxt2))
                    elif board[nxt1][nxt2] > 1:
                        customer_found.append((nxt1, nxt2))

        if customer_found:
            break

    if customer_found:
        cx, cy = min(customer_found)
        customer_number = board[cx][cy]
        board[cx][cy] = 0
        return customer_number, cx, cy, fuel
    else:
        return False


def to_destination(tx, ty, dx, dy, fuel):
    distance = 0
    visit = [[False] * N for _ in range(N)]
    visit[tx][ty] = True

    queue = [(tx, ty)]
    while queue:
        distance += 1
        if distance > fuel:
            return False

        for _ in range(len(queue)):
            idx1, idx2 = queue.pop(0)
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N and visit[nxt1][nxt2] is False:
                    visit[nxt1][nxt2] = True
                    if nxt1 == dx and nxt2 == dy:
                        fuel += distance
                        return dx, dy, fuel
                    elif board[nxt1][nxt2] == 1:
                        continue
                    else:
                        queue.append((nxt1, nxt2))

    return False


N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

c1, c2 = map(int, input().split())
destinations = [[] for _ in range(M+2)]

for i in range(2, M+2):
    a, b, c, d = map(int, input().split())
    board[a-1][b-1] = i
    destinations[i] = [c-1, d-1]

t1, t2 = c1-1, c2-1

for _ in range(M):
    customer_info = find_the_nearest_customer(t1, t2, F)
    if customer_info is False:
        F = -1
        break
    customer_num, customer_x, customer_y, F = customer_info
    destination_x, destination_y = destinations[customer_num]

    moving_info = to_destination(customer_x, customer_y, destination_x, destination_y, F)
    if moving_info is False:
        F = -1
        break
    t1, t2, F = moving_info

print(F)

import sys
sys.stdin = open('input.txt', 'r')


def add_100(n):
    return int(n) + 100


N = int(input())
point_init = list(map(add_100, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
E = int(input())

answer = 0
stack = [(N, 0, point_init[:])]
while stack:
    people, night, point = stack.pop()
    answer = max(answer, night)

    if people == 1:
        break

    elif people % 2:
        p_max = 0
        k = 0
        for i in range(N):
            if point[i] > p_max:
                p_max, k = point[i], i
        if k != E:
            point[k] = 0
            stack.append((people - 1, night, point[:]))

    else:
        for i in range(N):
            if point[i] > 0 and i != E:
                point_temp = point[:]
                point_temp[i] = 0
                for j in range(N):
                    if point_temp[j]:
                        point_temp[j] += board[i][j]
                stack.append((people - 1, night + 1, point_temp[:]))

print(answer)

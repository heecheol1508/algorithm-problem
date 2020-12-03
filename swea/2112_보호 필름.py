import sys
sys.stdin = open('input.txt', 'r')

import copy


def test():
    for j in range(W):
        value = film_info[0][j]
        cnt = 1
        for i in range(1, D):
            if film_info[i][j] == value:
                cnt += 1
                if cnt == K:
                    break
            else:
                value = film_info[i][j]
                cnt = 1
        else:
            return False

    return True


def dfs(a, b):
    global answer

    if b >= answer:
        return

    if test():
        answer = b
        return

    for i in range(a, D):
        film_info[i] = [0] * W
        dfs(i+1, b+1)
        film_info[i] = [1] * W
        dfs(i+1, b+1)
        film_info[i] = copy.copy(film_init[i])


T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    film_init = [list(map(int, input().split())) for _ in range(D)]
    film_info = copy.deepcopy(film_init)

    answer = 0

    if K != 1 and test() is False:
        answer = D
        for r in range(D-1, -1, -1):
            film_info[r] = [0] * W
            dfs(r+1, 1)
            film_info[r] = [1] * W
            dfs(r+1, 1)
            film_info[r] = copy.copy(film_init[r])

    print('#{} {}'.format(t, answer))

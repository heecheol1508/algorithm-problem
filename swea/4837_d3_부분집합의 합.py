import sys
sys.stdin = open('input.txt', 'r')


def solution(n, k, i):
    global answer

    if n == N:
        if k == K:
            answer += 1
        return

    for j in range(i+1, 13):
        if k + j > K:
            return
        solution(n+1, k+j, j)


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    answer = 0
    solution(0, 0, 0)
    print('#{} {}'.format(t, answer))

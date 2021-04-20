import sys
sys.stdin = open('input.txt', 'r')


def solution(n, r, c):
    if n == 0:
        return 0

    k = 2 ** (n-1)
    if r < k:
        if c < k:
            return solution(n-1, r, c)
        else:
            return k ** 2 + solution(n-1, r, c - k)
    else:
        if c < k:
            return (k ** 2) * 2 + solution(n-1, r - k, c)
        else:
            return (k ** 2) * 3 + solution(n-1, r - k, c - k)


N, R, C = map(int, input().split())
print(solution(N, R, C))

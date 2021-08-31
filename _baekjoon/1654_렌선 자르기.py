import sys
sys.stdin = open('input.txt', 'r')


def can_make_n(length):
    cnt = 0
    for i in range(K):
        t = lines[i] // length
        if t == 0:
            return False
        cnt += t
        if cnt >= N:
            return True
    return False


def binary_search(left, right):
    if right - 1 == left:
        return left

    mid = (left + right) // 2
    if can_make_n(mid):
        return binary_search(mid, right)
    else:
        return binary_search(left, mid)


K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

lines.sort(reverse=True)
MAX = sum(lines) // N

answer = binary_search(1, MAX + 1)
print(answer)

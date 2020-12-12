import sys
sys.stdin = open('input.txt', 'r')


def recursion(k, arr):
    if k == M:
        print(' '.join(map(str, arr)))
    else:
        for num in range(arr[-1], N+1):
            arr.append(num)
            recursion(k+1, arr)
            arr.pop()


N, M = map(int, input().split())
numbers = list(range(1, N+1))
for n in range(1, N+1):
    recursion(1, [n])

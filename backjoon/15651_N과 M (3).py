import sys
sys.stdin = open('input.txt', 'r')


def recursion(k, arr):
    if k == M:
        print(' '.join(arr))
    else:
        for num in numbers:
            arr.append(num)
            recursion(k+1, arr)
            arr.pop()


N, M = map(int, input().split())
numbers = list(map(str, list(range(1, N+1))))
recursion(0, [])

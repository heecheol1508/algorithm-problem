import sys
sys.stdin = open('input.txt', 'r')


def recursion(k, arr):
    if k == M:
        print(' '.join(map(str, arr)))
    else:
        for num in numbers:
            if num not in arr:
                arr.append(num)
                recursion(k+1, arr)
                arr.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

recursion(0, [])

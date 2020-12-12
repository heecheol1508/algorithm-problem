import sys
sys.stdin = open('input.txt', 'r')


def recursion(k, arr):
    if k == M:
        print(' '.join(map(str, arr)))
    else:
        for num in numbers:
            if num > arr[-1]:
                arr.append(num)
                recursion(k+1, arr)
                arr.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for n in numbers:
    recursion(1, [n])

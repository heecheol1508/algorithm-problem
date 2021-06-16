import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
arr = [1, 1, 1, 2, 2]

for _ in range(T):
    N = int(input())
    if N > len(arr):
        for _ in range(N - len(arr)):
            arr.append(arr[-1] + arr[-5])
    print(arr[N-1])

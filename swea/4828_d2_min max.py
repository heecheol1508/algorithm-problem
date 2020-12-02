import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{} {}'.format(t, numbers[-1]-numbers[0]))

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
if N % 2:
    for i in range(N-1, N//2, -1):
        answer += numbers[i] * 2
    answer += numbers[N//2]
else:
    for i in range(N-1, N//2-1, -1):
        answer += numbers[i] * 2

print(answer)

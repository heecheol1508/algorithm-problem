import sys
sys.stdin = open('input.txt', 'r')
import itertools


N = int(input())
arr = list(input())
num = [0] * N
for i in range(0, N, 2):
    num[i] = int(arr[i])


def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return n1 * n2


answer = -2 ** 31
for order in itertools.permutations(list(range(1, N, 2)), N//2):
    numbers = num[:]
    visit = [False] * N

    for k in order:
        if visit[k-1] is False:
            numbers[k-1] = calculate(numbers[k-1], numbers[k+1], arr[k])
            visit[k-1] = visit[k] = visit[k+1] = True
        else:
            idx = k - 2
            while idx > 0 and visit[idx]:
                idx -= 2
            numbers[idx+1] = calculate(numbers[idx+1], numbers[k+1], arr[k])
            visit[k] = visit[k+1] = True

    if numbers[0] > answer:
        answer = numbers[0]

print(answer)

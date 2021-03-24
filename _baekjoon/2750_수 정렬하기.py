import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
print('\n'.join(map(str, numbers)))

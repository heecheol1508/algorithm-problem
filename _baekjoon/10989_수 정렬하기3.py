import sys
sys.stdin = open('input.txt', 'r')


N = int(sys.stdin.readline())
numbers = [0] * 10001

for _ in range(N):
    n = int(sys.stdin.readline())
    numbers[n] += 1

for i in range(1, 10001):
    if numbers[i]:
        for _ in range(numbers[i]):
            sys.stdout.write('{}\n'.format(i))

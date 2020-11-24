import sys
sys.stdin = open('input.txt', 'r')
import collections


N = int(input())
total = int(10**N * 0.8)

is_prime = [True] * total
is_prime[0] = is_prime[1] = False

for i in range(3, total, 2):
    if is_prime[i]:
        for j in range(i, total, 2*i):
            if is_prime[j]:
                is_prime[j] = False
        is_prime[i] = True

odd_numbers = ['1', '3', '7', '9']
queue = collections.deque(['2', '3', '5', '7'])

for _ in range(N-1):
    for __ in range(len(queue)):
        front = queue.popleft()
        for back in odd_numbers:
            num = int(front + back)
            if is_prime[num]:
                queue.append(str(num))

print('\n'.join(queue))

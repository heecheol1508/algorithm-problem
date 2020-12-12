import sys
sys.stdin = open('input.txt', 'r')

import collections


def is_prime(n):
    for m in range(2, int(n**(1/2)) + 1):
        if n % m == 0:
            return False
    return True


N = int(input())
num_list = collections.deque([2, 3, 5, 7])

num_next = [1, 3, 7, 9]

for _ in range(N-1):
    for __ in range(len(num_list)):
        a = num_list.popleft()
        for b in num_next:
            new = 10*a + b
            if is_prime(new):
                num_list.append(new)

for num in num_list:
    print(num)

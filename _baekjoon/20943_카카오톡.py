import sys
sys.stdin = open('input.txt', 'r')

import collections

N = int(input())
gradient = collections.defaultdict(int)
inf = float('inf')

for _ in range(N):
    a, b, c = map(int, input().split())
    if b:
        gradient[a/b] += 1
    elif a > 0:
        gradient[inf] += 1
    else:
        gradient[-inf] += 1

answer = 0
for cnt in gradient.values():
    answer += (N - cnt) * cnt

print(answer // 2)

# 48분

import heapq
import collections
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

balls = []
for i in range(N):
    c, s = map(int, input().split())
    heapq.heappush(balls, (s, c, i))

answer = [''] * N
color_info = collections.defaultdict(int)
color_info['total'] = 0
size_standard = 0
temp = []

for _ in range(N):
    size, color, index = heapq.heappop(balls)
    if size > size_standard:
        size_standard = size
        for k in range(len(temp)):
            t_size, t_color = temp[k]
            color_info[t_color] += t_size
            color_info['total'] += t_size
        temp = []

    temp.append((size, color))
    answer[index] = str(color_info['total'] - color_info[color])

print('\n'.join(answer))

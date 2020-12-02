import sys
sys.stdin = open('input.txt', 'r')

import collections
import heapq


T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(input())

    cards = collections.defaultdict(int)
    for num in data:
        cards[num] += 1

    queue = []
    for num, cnt in cards.items():
        heapq.heappush(queue, (-cnt, -int(num)))

    a, b = heapq.heappop(queue)
    print('#{} {} {}'.format(t, -b, -a))

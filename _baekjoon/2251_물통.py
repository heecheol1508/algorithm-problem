# 13:21 ~ 13:45
import collections
import sys
sys.stdin = open('input.txt', 'r')


volume = list(map(int, input().split()))

dp = [(0, 0, volume[2])]
answer = set()

queue = collections.deque([(0, 0, volume[2])])
while queue:
    a, b, c = queue.popleft()
    if a > 0:
        if b < volume[1]:
            d = min(a, volume[1] - b)
            if (a-d, b+d, c) not in dp:
                dp.append((a-d, b+d, c))
                queue.append((a-d, b+d, c))
        if c < volume[2]:
            d = min(a, volume[2] - c)
            if (a-d, b, c+d) not in dp:
                dp.append((a-d, b, c+d))
                queue.append((a-d, b, c+d))
    elif a == 0:
        answer.add(c)
    if b > 0:
        if a < volume[0]:
            d = min(b, volume[0] - a)
            if (a+d, b-d, c) not in dp:
                dp.append((a+d, b-d, c))
                queue.append((a+d, b-d, c))
        if c < volume[2]:
            d = min(b, volume[2] - c)
            if (a, b-d, c+d) not in dp:
                dp.append((a, b-d, c+d))
                queue.append((a, b-d, c+d))
    if c > 0:
        if a < volume[0]:
            d = min(c, volume[0] - a)
            if (a+d, b, c-d) not in dp:
                dp.append((a+d, b, c-d))
                queue.append((a+d, b, c-d))
        if b < volume[1]:
            d = min(c, volume[1] - b)
            if (a, b+d, c-d) not in dp:
                dp.append((a, b+d, c-d))
                queue.append((a, b+d, c-d))

print(' '.join(map(str, sorted(list(answer)))))

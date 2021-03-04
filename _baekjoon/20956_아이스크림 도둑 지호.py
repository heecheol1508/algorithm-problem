import sys
sys.stdin = open('input.txt', 'r')

import collections


N, M = map(int, input().split())
ice_cream_info = list(map(int, input().split()))

indexes = collections.defaultdict(list)
flag = True
answer = []

for i, size in enumerate(ice_cream_info, 1):
    indexes[size].append(i)

ice_cream_size = sorted(indexes.keys())
for _ in range(M):
    size = ice_cream_size[-1]

    if len(indexes[size]) == 1:
        answer.append(str(indexes[size][0]))
        ice_cream_size.pop()
    elif flag:
        answer.append(str(indexes[size].pop(0)))
    else:
        answer.append(str(indexes[size].pop()))

    if size % 7 == 0:
        flag = not flag

print('\n'.join(answer))

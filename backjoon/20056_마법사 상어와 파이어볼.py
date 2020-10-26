import sys
sys.stdin = open('input.txt', 'r')
import collections


N, M, K = map(int, input().split())

before_move = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    before_move[(r-1, c-1)] = [(m, s, d)]

adj_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    after_move = collections.defaultdict(list)
    for pos, info in before_move.items():
        idx1, idx2 = pos
        for m, s, d in info:
            nxt1, nxt2 = (idx1 + s*adj_list[d][0]) % N, (idx2 + s*adj_list[d][1]) % N
            after_move[(nxt1, nxt2)].append((m, s, d))

    before_move = collections.defaultdict(list)
    for pos, info in after_move.items():
        if len(info) == 1:
            before_move[pos] = info
        else:
            sum_m = 0
            sum_s = 0
            set_d = set()
            for m, s, d in info:
                sum_m += m
                sum_s += s
                set_d.add(d % 2)

            new_m = sum_m // 5
            new_s = sum_s // len(info)

            if new_m == 0:
                continue
            elif len(set_d) == 1:
                for i in range(4):
                    before_move[pos].append((new_m, new_s, 2*i))
            else:
                for i in range(4):
                    before_move[pos].append((new_m, new_s, 2*i+1))

answer = 0
for info in before_move.values():
    for m, s, d in info:
        answer += m

print(answer)

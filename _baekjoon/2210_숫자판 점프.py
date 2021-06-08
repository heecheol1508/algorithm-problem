# 13:12 ~ 13:20
import collections
import sys
sys.stdin = open('input.txt', 'r')


board = [input().split() for _ in range(5)]
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

numbers = set()
for i in range(5):
    for j in range(5):
        queue = collections.deque([(i, j, board[i][j])])
        while queue:
            idx1, idx2, temp = queue.popleft()
            if len(temp) == 6:
                numbers.add(temp)
                continue
            for di, dj in adj:
                nxt1, nxt2 = idx1 + di, idx2 + dj
                if 0 <= nxt1 < 5 and 0 <= nxt2 < 5:
                    queue.append((nxt1, nxt2, temp+board[nxt1][nxt2]))

# print(numbers)
print(len(numbers))

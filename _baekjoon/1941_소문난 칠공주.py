import itertools
import sys
sys.stdin = open('input.txt', 'r')


board = [list(input()) for _ in range(5)]
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

students = []
for i in range(5):
    for j in range(5):
        students.append((i, j))

answer = 0

for group in itertools.combinations(students, 7):
    ds = 0
    for i, j in group:
        if board[i][j] == 'S':
            ds += 1
    if ds >= 4:
        visit = {}
        for pos in group:
            visit[pos] = False

        queue = [group[0]]
        visit[group[0]] = True

        while queue:
            pos1 = queue.pop(0)
            for di, dj in adj:
                pos2 = (pos1[0]+di, pos1[1]+dj)
                if pos2 in group and visit[pos2] is False:
                    visit[pos2] = True
                    queue.append(pos2)

        if False not in visit.values():
            answer += 1

print(answer)

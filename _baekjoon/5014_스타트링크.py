import sys
sys.stdin = open('input.txt', 'r')


F, S, G, U, D = map(int, input().split())

floor = [False] * (F+1)
floor[S] = True

cnt = 0
queue = [S]

while queue:
    if floor[G] is True:
        break
    cnt += 1
    for _ in range(len(queue)):
        C = queue.pop(0)
        uC, dC = C + U, C - D
        if uC <= F and floor[uC] is False:
            floor[uC] = True
            queue.append(uC)
        if dC > 0 and floor[dC] is False:
            floor[dC] = True
            queue.append(dC)
if floor[G] is True:
    print(cnt)
else:
    print("use the stairs")

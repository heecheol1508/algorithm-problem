import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
taxi = list(map(int, input().split()))
move = list(map(int, input().split()))

nxt = taxi[0] + move[0]
idx = 1
cnt = 0
answer = -1

while True:
    if nxt >= M:
        answer = cnt
        break
    new_nxt = 0
    for i in range(idx, N):
        if taxi[i] > nxt:
            idx = i
            break
        elif taxi[i] + move[i] > new_nxt:
            new_nxt = taxi[i] + move[i]
    else:
        idx = N

    if new_nxt:
        nxt = new_nxt
        cnt += 1
    else:
        break

print(answer)

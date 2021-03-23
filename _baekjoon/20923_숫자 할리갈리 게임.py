import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
deck_do = [0] * N
deck_su = [0] * N

for i in range(1, N+1):
    deck_do[-i], deck_su[-i] = map(int, input().split())

ground_do = []
ground_su = []
idx_do = 0
idx_su = 0

flag = False
for i in range(M):
    if i % 2:
        ground_su.append(deck_su[idx_su])
        idx_su += 1
        if idx_su == len(deck_su):
            flag = 'do'
            break

        if ground_su[-1] == 5:
            deck_do += ground_su + ground_do
            ground_do = []
            ground_su = []
        elif ground_do and ground_su[-1] + ground_do[-1] == 5:
            deck_su += ground_do + ground_su
            ground_do = []
            ground_su = []

    else:
        ground_do.append(deck_do[idx_do])
        idx_do += 1
        if idx_do == len(deck_do):
            flag = 'su'
            break

        if ground_do[-1] == 5:
            deck_do += ground_su + ground_do
            ground_do = []
            ground_su = []
        elif ground_su and ground_su[-1] + ground_do[-1] == 5:
            deck_su += ground_do + ground_su
            ground_do = []
            ground_su = []

if flag:
    print(flag)
else:
    deck_do_length = len(deck_do) - idx_do
    deck_su_length = len(deck_su) - idx_su
    if deck_do_length > deck_su_length:
        print('do')
    elif deck_do_length < deck_su_length:
        print('su')
    else:
        print('dosu')

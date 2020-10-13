import sys
sys.stdin = open('input.txt', 'r')


fish_info = {}
board = {}

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish_info[data[2*j]] = [i, j, data[2*j+1]]
        board[(i, j)] = data[2*j]

eaten = board[(0, 0)]
fish_info[0] = fish_info.pop(eaten)
board[(0, 0)] = 0
adj_list = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]

answer = 0


def fish_move(f, b):
    for fish_a in range(1, 17):
        if fish_a in f.keys():
            idx1, idx2, d = f[fish_a]
            for k in range(8):
                nd = (d+k) % 8
                nxt1, nxt2 = idx1 + adj_list[nd][0], idx2 + adj_list[nd][1]
                if (nxt1, nxt2) not in b.keys():
                    continue
                elif b[(nxt1, nxt2)] > 0:
                    fish_b = b[(nxt1, nxt2)]
                    b[(idx1, idx2)], b[(nxt1, nxt2)] = fish_b, fish_a
                    f[fish_a], f[fish_b] = [nxt1, nxt2, nd], [idx1, idx2, f[fish_b][2]]
                    break
                elif b[(nxt1, nxt2)] == -1:
                    b[(idx1, idx2)], b[(nxt1, nxt2)] = -1, fish_a
                    f[fish_a] = [nxt1, nxt2, nd]
                    break


def solution(f, b, score):
    global answer

    if score > answer:
        answer = score

    fish_move(f, b)
    idx1, idx2, d = f[0]
    for k in range(1, 4):
        nxt1, nxt2 = idx1 + k*adj_list[d][0], idx2 + k*adj_list[d][1]
        if 0 <= nxt1 < 4 and 0 <= nxt2 < 4:
            if b[(nxt1, nxt2)] > 0:
                tf = f.copy()
                tb = b.copy()

                fish_eaten = b[(nxt1, nxt2)]
                tf[0] = [nxt1, nxt2, tf.pop(fish_eaten)[2]]
                tb[(idx1, idx2)], tb[(nxt1, nxt2)] = -1, 0
                solution(tf, tb, score+fish_eaten)
        else:
            break


solution(fish_info, board, eaten)
print(answer)

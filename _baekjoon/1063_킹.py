import sys
sys.stdin = open('input.txt', 'r')


def nxt(move, i, j):
    if move == 'R':
        return i, j + 1
    elif move == 'L':
        return i, j - 1
    elif move == 'B':
        return i - 1, j
    elif move == 'T':
        return i + 1, j
    elif move == 'RT':
        return i + 1, j + 1
    elif move == 'LT':
        return i + 1, j - 1
    elif move == 'RB':
        return i - 1, j + 1
    elif move == 'LB':
        return i - 1, j - 1
    else:
        print(move)
        return i, j


king, stone, N = input().split()
ki1 = ord(king[1]) - ord('1')
kj1 = ord(king[0]) - ord('A')
si1 = ord(stone[1]) - ord('1')
sj1 = ord(stone[0]) - ord('A')

for _ in range(int(N)):
    cmd = input()
    ki2, kj2 = nxt(cmd, ki1, kj1)

    if 0 <= ki2 < 8 and 0 <= kj2 < 8:
        if ki2 == si1 and kj2 == sj1:
            si2, sj2 = nxt(cmd, si1, sj1)
            if 0 <= si2 < 8 and 0 <= sj2 < 8:
                ki1, kj1 = si1, sj1
                si1, sj1 = si2, sj2
        else:
            ki1, kj1 = ki2, kj2

print(chr(kj1 + 65) + chr(ki1 + ord('1')))
print(chr(sj1 + 65) + chr(si1 + ord('1')))

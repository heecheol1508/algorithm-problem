import itertools
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
palette = []

for _ in range(N):
    palette.append(list(map(int, input().split())))

rgb_G = list(map(int, input().split()))
rgb_M = 987654321

for n in range(2, min(N+1, 8)):
    for comb in itertools.combinations(range(N), n):
        rgb = [0, 0, 0]
        for i in comb:
            rgb[0] += palette[i][0]
            rgb[1] += palette[i][1]
            rgb[2] += palette[i][2]

        diff = 0
        for i in range(3):
            diff += abs(rgb_G[i] - rgb[i] // n)

        if diff < rgb_M:
            rgb_M = diff

print(rgb_M)

# 13:46 ~ 13:52
import sys
sys.stdin = open('input.txt', 'r')


heights = [int(input()) for _ in range(9)]
d = sum(heights) - 100
flag = False

for i in range(8):
    if heights[i] < d:
        for j in range(i+1, 9):
            if heights[i] + heights[j] == d:
                del heights[j]
                del heights[i]
                flag = True
                break
        if flag:
            break
print('\n'.join(map(str, sorted(heights))))

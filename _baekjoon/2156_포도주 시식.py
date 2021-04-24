import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
temp = [0, 0, 0]
for _ in range(N):
    num = int(input())
    temp[0], temp[1], temp[2] = max(temp), temp[0] + num, temp[1] + num

print(max(temp))

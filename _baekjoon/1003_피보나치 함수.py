import sys
sys.stdin = open('input.txt', 'r')


list_N = [int(input()) for _ in range(int(input()))]
M = max(list_N)

dp_0 = [1, 0]
dp_1 = [0, 1]
for i in range(2, M+1):
    dp_0.append(dp_0[i - 2] + dp_0[i - 1])
    dp_1.append(dp_1[i - 2] + dp_1[i - 1])

for N in list_N:
    print(dp_0[N], dp_1[N])

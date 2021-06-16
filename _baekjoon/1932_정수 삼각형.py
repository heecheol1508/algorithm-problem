import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
dp = [0, 0]

for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(i+1):
        nums[j] += max(dp[j], dp[j+1])
    dp = [0] + nums + [0]

print(max(dp))

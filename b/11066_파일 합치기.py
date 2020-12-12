import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
answer = [0] * T

for t in range(T):
    K = int(input())
    data = list(map(int, input().split()))

    inf = float('inf')
    table = [[inf] * K for _ in range(K)]

    for i in range(K-1):
        table[i][i] = 0
        table[i][i+1] = data[i] + data[i+1]
    table[-1][-1] = 0

    for c in range(2, K):
        for a in range(K-c):
            temp = sum(data[a:a+c+1])
            for b in range(a, a+c):
                table[a][a+c] = min(table[a][a+c], table[a][b] + table[b+1][a+c] + temp)

    answer[t] = str(table[0][-1])

print('\n'.join(answer))

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())

    M = N // 4
    password = set()
    for i in range(N):
        temp = ''
        for j in range(i-M, i):
            temp += numbers[j]
        password.add(int(temp, 16))

    password_sorted = sorted(list(password), reverse=True)
    print('#{} {}'.format(t, password_sorted[K-1]))

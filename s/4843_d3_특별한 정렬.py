import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())

    data = list(map(int, input().split()))
    data.sort()

    answer = [0] * 10
    for i in range(5):
        answer[2*i+1] = str(data[i])
    for i in range(5):
        answer[2*i] = str(data[-i-1])

    print('#{} {}'.format(t, ' '.join(answer)))

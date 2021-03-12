import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

inf = float('inf')
arr1 = [-1] * 7
arr2 = [0] * 7

for i in range(N):
    r = A[i] % 7
    if arr1[r] == -1:
        temp = 0
        flag = False
        for j in range(M):
            temp += B[j]
            if (r + temp) % 7 == 0:
                if not flag:
                    flag = True
                    arr1[r] = j
                temp -= B[j]

        arr2[r] = temp

        if flag is False:
            arr1[r] = inf

        if -1 not in arr1:
            break

max_r = max(arr1)
answer = []

for i in range(N):
    r = A[i] % 7

    if arr1[r] == max_r:
        answer.append(str((A[i] + arr2[r]) % (10**9 + 7)))

print(len(answer))
print(' '.join(answer))

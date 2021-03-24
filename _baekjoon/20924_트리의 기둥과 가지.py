import sys
sys.setrecursionlimit(200000)
sys.stdin = open('input.txt', 'r')


N, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, v = map(int, input().split())
    arr[n1].append((n2, v))
    arr[n2].append((n1, v))


def recursion(a, b, cnt):
    if len(arr[b]) == 1:
        if cnt > answer[1]:
            answer[1] = cnt
        return

    for c, d in arr[b]:
        if c != a:
            recursion(b, c, cnt+d)


arr[R].append((0, 0))
A = 0
B = R
answer = [0, 0]
max_branch = 0

found_giga = False
while True:
    if len(arr[B]) == 1:
        break
    if len(arr[B]) == 2:
        for C, D in arr[B]:
            if C != A:
                A, B = B, C
                answer[0] += D
                break
    else:
        found_giga = True
        break

if found_giga:
    recursion(A, B, 0)
    print(answer[0], answer[1])
else:
    print(answer[0], answer[1])

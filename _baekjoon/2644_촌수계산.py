import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
A, B = map(int, input().split())

parent = [0] * (N+1)

for _ in range(int(input())):
    x, y = map(int, input().split())
    parent[y] = x

parent_A = []
parent_B = []

while A != 0:
    parent_A.append(A)
    A = parent[A]

while B != 0:
    parent_B.append(B)
    B = parent[B]

flag = False
for i in range(len(parent_A)):
    for j in range(len(parent_B)):
        if parent_A[i] == parent_B[j]:
            flag = True
            break
    if flag:
        break
if flag:
    print(i + j)
else:
    print(-1)

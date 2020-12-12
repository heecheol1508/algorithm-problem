import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


N = int(input())
data = list(map(int, input().split()))

h = 0
while 2**h < N:
    h += 1

inf = float('inf')
tree = [inf] * (2**(h+1))

for i in range(N):
    tree[i + 2**h] = data[i]


def initialize_tree(k):
    if 2*k < len(tree):
        tree[k] = min(initialize_tree(2*k), initialize_tree(2*k+1))
    return tree[k]


def modify_tree(k):
    if k == 1:
        return
    elif k % 2 == 0:
        if min(tree[k], tree[k+1]) != tree[k//2]:
            tree[k//2] = min(tree[k], tree[k+1])
            modify_tree(k//2)
    else:
        if min(tree[k-1], tree[k]) != tree[k//2]:
            tree[k//2] = min(tree[k-1], tree[k])
            modify_tree(k//2)
    return


def find_minimum(left, right, x, y):
    if left == right:
        return tree[left]
    if x == y:
        return tree[x]
    if left == x and right == y:
        return tree[x//(y-x+1)]

    mid = (left + right) // 2
    if y <= mid:
        return find_minimum(left, mid, x, y)
    elif x > mid:
        return find_minimum(mid + 1, right, x, y)
    else:
        return min(find_minimum(left, mid, x, mid), find_minimum(mid + 1, right, mid + 1, y))


initialize_tree(1)

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        d = b + 2**h - 1
        tree[d] = c
        modify_tree(d)
    else:
        d = b + 2**h - 1
        e = c + 2**h - 1
        print(find_minimum(2**h, 2**(h+1) - 1, d, e))

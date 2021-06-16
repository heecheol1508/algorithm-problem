import sys
sys.stdin = open('input.txt', 'r')


n = int(input())

a, b = 1, 1
for i in range(1, n):
    a, b = b, (a + b) % 15746

print(b)

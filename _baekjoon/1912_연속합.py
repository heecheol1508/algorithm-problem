import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
numbers = list(map(int, input().split()))

answer = max(numbers)
before = 0
for num in numbers:
    if num > 0:
        before += num
        answer = max(answer, before)
    elif before + num > 0:
        before += num
    else:
        before = 0

print(answer)

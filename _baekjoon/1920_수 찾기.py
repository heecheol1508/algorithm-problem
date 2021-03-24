import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
numbers = list(map(int, input().split()))
answers = ['0'] * M


def binary_search(num, left, right):
    if left == right:
        return False
    mid = (left + right) // 2
    if A[mid] == num:
        return True
    elif A[mid] < num:
        return binary_search(num, mid+1, right)
    else:
        return binary_search(num, left, mid)


for i in range(M):
    if binary_search(numbers[i], 0, N):
        answers[i] = '1'

print('\n'.join(answers))

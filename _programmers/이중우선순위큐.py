import collections


def solution(operations):
    queue = collections.deque()

    def recursion(left, right, num):
        if left == right:
            queue.insert(left, num)
        else:
            mid = (left + right) // 2
            if num > queue[mid]:
                recursion(mid+1, right, num)
            elif num == queue[mid]:
                queue.insert(mid, num)
            else:
                recursion(left, mid, num)

    for operation in operations:
        a, b = operation.split()
        if a == 'I':
            recursion(0, len(queue), int(b))
        elif b == '1':
            if queue:
                queue.pop()
        else:
            if queue:
                queue.popleft()

    if queue:
        return [queue[-1], queue[0]]
    else:
        return [0, 0]


print(solution(["I 16", "D 1"]), [0, 0])
print(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])

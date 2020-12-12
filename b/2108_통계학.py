import sys
sys.stdin = open('input.txt', 'r')
import collections
import heapq


N = int(input())

arr = []
freq = collections.defaultdict(int)

for _ in range(N):
    num = int(input())
    arr.append(num)
    arr.sort()
    freq[num] += 1

queue = []
for key, value in freq.items():
    heapq.heappush(queue, (-value, key))

print(round(sum(arr)/N))
print(arr[N//2])

if len(queue) >= 2:
    a, b = heapq.heappop(queue)
    c, d = heapq.heappop(queue)
    if a == c:
        print(d)
    else:
        print(b)
else:
    a, b = heapq.heappop(queue)
    print(b)

print(max(arr)-min(arr))

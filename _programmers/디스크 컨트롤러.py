import heapq


def solution(jobs):
    n = len(jobs)
    requests = []
    for job in jobs:
        heapq.heappush(requests, (job[0], job[1]))

    ms_total = 0
    end = 0
    waiting = []

    while requests or waiting:
        if waiting:
            a, b = heapq.heappop(waiting)
            ms_total += end + a - b
            end += a
        else:
            a, b = heapq.heappop(requests)
            ms_total += b
            end = a + b

        while requests and requests[0][0] <= end:
            c, d = heapq.heappop(requests)
            heapq.heappush(waiting, (d, c))

    answer = ms_total // n
    return answer


print('answer', solution([[0, 3], [1, 9], [2, 6], [19, 2]]))

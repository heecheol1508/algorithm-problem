def checking(weak, dist):

    n_weak = len(weak)
    i = 0   # i <- index in weak

    while i < n_weak:
        if len(dist) == 0:
            return -1

        j = len(dist) - 1     # j <- index in dist

        for k in range(i, n_weak):  # k <- in range
            if weak[k] > weak[i] + dist[j]:
                k -= 1
                break

        for j in range(j-1, -1, -1):    # minimum dist index will be used
            if dist[j] + weak[i] < weak[k]:
                j += 1
                break

        dist.pop(j)
        i = k + 1

    return len(dist)


def solution(n, weak, dist):
    answer = len(dist) + 1

    for i in range(len(dist), 0, -1):   # i <- number of dist for use
        if i >= answer:
            continue

        for j in range(len(weak)):  # j <- start point, I will put large distance first
            temp_weak = weak[j:]
            for k in range(j):
                temp_weak.append(weak[k]+n)     # for numbers which over n
            temp_dist = dist[-i:]

            result = checking(temp_weak, temp_dist)  # return size of dist left
            if result >= 0:
                answer = i - result
                break
        else:
            answer = i + 1
            break

    if answer == len(dist) + 1:
        return -1
    else:
        return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

def solution(distance, rocks, n):

    rocks.sort()
    between = [0] * (len(rocks) + 1)

    for i in range(1, len(rocks)):
        between[i] = rocks[i] - rocks[i-1]

    between[0] = rocks[0]
    between[-1] = distance - rocks[-1]

    for _ in range(n):
        min_value = between[0]
        min_idx = (0, 1)
        for i in range(1, len(between)):
            if between[i] > min_value:
                continue

            elif between[i] == min_value:
                if i + 1 < len(between):
                    a, b, c = min((between[min_idx[0] + between[min_idx[1]]] - min_value, min_idx[0], min_idx[1]),
                                  (between[i - 1], i - 1, i), (between[i + 1], i, i + 1))
                    min_idx = (b, c)
                else:
                    a, b, c = min((between[min_idx[0] + between[min_idx[1]]] - min_value, min_idx[0], min_idx[1]),
                                  (between[i - 1], i - 1, i))
                    min_idx = (b, c)
            else:
                min_value = between[i]
                if i + 1 < len(between):
                    if between[i-1] <= between[i+1]:
                        min_idx = (i-1, i)
                    else:
                        min_idx = (i, i+1)
                else:
                    min_idx = (i-1, i)

        between[min_idx[1]] += between[min_idx[0]]
        between.pop(min_idx[0])

    answer = min(between)
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))

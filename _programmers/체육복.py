def solution(n, lost, reserve):
    set_lost = set(lost)
    set_reserve = set(reserve)
    intersection = set_lost & set_reserve

    set_lost -= intersection
    set_reserve -= intersection

    lost = sorted(list(set_lost))
    reserve = sorted(list(set_reserve))

    answer = n - len(lost)

    for student in lost:
        for i in range(len(reserve)):
            if reserve[i] > student + 1:
                break
            elif abs(reserve[i] - student) == 1:
                answer += 1
                reserve = reserve[i+1:]
                break

    return answer


print(solution(3, [3], [1]))

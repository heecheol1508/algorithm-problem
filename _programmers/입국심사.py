def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n + 1

    while True:
        if right - left == 1:
            return right

        mid = (left + right) // 2
        cnt = 0
        for i in range(len(times)):
            people = mid // times[i]
            if people == 0:
                break
            else:
                cnt += people
                if cnt > n:
                    break

        if cnt > n:
            right = mid
        elif cnt < n:
            left = mid
        else:
            answer = 0
            for i in range(len(times)):
                people = mid // times[i]
                if people == 0:
                    break
                else:
                    answer = max(answer, times[i] * people)
            return answer


print(solution(2, [1, 2]))

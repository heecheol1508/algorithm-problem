def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems)]

    section = set()
    section.add(gems[0])
    i = 0
    j = 1

    while True:
        if len(section) == n:
            if j - i - 1 < answer[1] - answer[0]:
                answer = [i+1, j]
            if j == len(gems):
                break
            section = set()
            i += 1
            for k in range(n):
                section.add(gems[i+k])
            j = i + n

        elif j == len(gems):
            break

        elif j - i == answer[1] - answer[0]:
            section = set()
            i += 1
            for k in range(n):
                section.add(gems[i+k])
            j = i + n

        elif gems[j] not in section:
            section.add(gems[j])
            j += 1

        elif gems[j] == gems[i]:
            i += 1
            j += 1
            while True:
                if gems[i] in gems[i+1:j]:
                    i += 1
                else:
                    break

        else:
            j += 1

    # print(answer)
    return answer


solution(["XYZ", "XYZ", "XYZ"])

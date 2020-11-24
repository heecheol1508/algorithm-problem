def solution(s):
    answer = 9999
    # print(len(s))

    for i in range(1, len(s)//2+1):

        substrings = [s[:i]]
        counts = [1]

        for j in range(1, len(s)//i+1):
            part = s[i*j:i*(j+1)]
            if part == substrings[-1]:
                counts[-1] += 1
            else:
                substrings.append(part)
                counts.append(1)

        print(substrings)
        print(counts)

        length = 0
        for k in range(len(counts)):
            length += len(substrings[k])

            if counts[k] == 1:
                continue
            else:
                length += len(str(counts[k]))

        # print(length)
        # print()
        if length < answer:
            answer = length

    return answer


print(solution("a"))

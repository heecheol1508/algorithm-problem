def solution(number, k):
    answer = ''

    while number:
        _max = '0'
        _idx = 0
        for i in range(min(len(number), k + 1)):
            if number[i] == '9':
                _max = '9'
                _idx = i
                break
            elif number[i] > _max:
                _max = number[i]
                _idx = i

        answer += _max
        number = number[_idx+1:]
        k -= _idx
        if k == 0:
            return answer + number

    return answer[:-k]


print(solution('1231234', 3))

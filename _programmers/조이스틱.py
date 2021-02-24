def solution(name):
    move = len(name) - 1
    flag = False
    for i in range(len(name)):
        if name[i] != 'A':
            flag = True
            left = 0
            for j in range(1, len(name)):
                if name[i-j] != 'A':
                    left = j
            move = min(move, i + left)

    if flag is False:
        return 0

    for i in range(len(name)):
        move += min(ord(name[i]) - 65, 91 - ord(name[i]))

    return move


print(solution('JEROEN'))

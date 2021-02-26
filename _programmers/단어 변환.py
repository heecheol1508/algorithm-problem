def solution(begin, target, words):

    if target not in words:
        return 0

    m = len(begin)
    changed = 0
    queue = [(begin, words)]

    while queue:
        changed += 1
        for _ in range(len(queue)):
            word, arr = queue.pop(0)
            for i in range(len(arr)):
                cnt = 0
                for j in range(m):
                    if word[j] != arr[i][j]:
                        cnt += 1
                        if cnt > 1:
                            break
                if cnt == 1:
                    if arr[i] == target:
                        return changed
                    temp = arr[:i] + arr[i+1:]
                    queue.append((arr[i], temp))

    return 0


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))

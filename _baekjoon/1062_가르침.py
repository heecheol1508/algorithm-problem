import itertools
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
if K > 5:
    set_1 = set('acint')
    K2 = K - 5
    count1 = 0
    count2 = 0

    temp_all = set()
    word_all = []

    for _ in range(N):
        temp = set(input()) - set_1
        if len(temp) > K2:
            continue
        if len(temp) == 0:
            count1 += 1
        else:
            temp_all.update(temp)
            word_all.append(''.join(temp))

    for comb in itertools.combinations(temp_all, min(K2, len(temp_all))):
        cnt = 0
        for i in range(len(word_all)):
            for j in range(len(word_all[i])):
                if word_all[i][j] not in comb:
                    break
            else:
                cnt += 1
        if cnt > count2:
            count2 = cnt

    print(count1 + count2)

else:
    print(0)
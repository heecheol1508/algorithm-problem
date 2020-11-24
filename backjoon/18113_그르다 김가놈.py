import sys
sys.stdin = open('input.txt', 'r')


N, K, M = map(int, input().split())
kimbab = []


def is_satisfied(length):
    cnt = 0
    for i in range(len(kimbab)):
        cnt += kimbab[i] // length
        if cnt >= M:
            return True
    return False


def find_max_length(short, long):
    if short + 1 == long:
        return short
    else:
        mid = (short+long) // 2
        if is_satisfied(mid):
            return find_max_length(mid, long)
        else:
            return find_max_length(short, mid)


for _ in range(N):
    cm = int(input())
    if cm == 2*K or cm <= K:
        continue
    elif cm > 2*K:
        kimbab.append(cm - 2*K)
    else:
        kimbab.append(cm - K)

if sum(kimbab) < M:
    print(-1)
else:
    answer = find_max_length(1, max(kimbab)+1)
    print(answer)

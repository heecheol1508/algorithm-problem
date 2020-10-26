import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    hours_it_takes = list(map(int, input().split()))

    # order A -> B
    list_before = [[] for _ in range(N)]
    list_after = [[] for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        list_before[b-1].append(a-1)
        list_after[a-1].append(b-1)

    hours_of_each_order = [[0] for _ in range(N)]
    hours_we_need = [0] * N
    visit = [False] * N

    E = int(input()) - 1
    flag = True
    while flag:
        for i in range(N):
            if visit[i] is False and len(list_before[i]) == 0:
                visit[i] = True
                hours_we_need[i] = max(hours_of_each_order[i]) + hours_it_takes[i]
                if i == E:
                    flag = False
                    break
                for j in list_after[i]:
                    list_before[j].remove(i)
                    hours_of_each_order[j].append(hours_we_need[i])

    print(hours_we_need[E])

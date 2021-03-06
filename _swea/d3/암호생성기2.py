import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())

    num = list(map(int, input().split()))
    sub = 1

    cut_num = (min(num) // 120) * 120

    for i in range(8):
        num[i] -= cut_num

    while num[-1] > 0:        
        num.append(num.pop(0) - sub)
        if sub == 5:
            sub = 1
        else:
            sub += 1
    num[7] = 0    
    password = ' '.join(list(map(str, num)))
    
    print(f'#{N} {password}')
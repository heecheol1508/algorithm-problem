import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
skill = list(reversed(list(map(int, input().split()))))

answer_top = '1'
answer_mid = []
answer_bot = []

for i in range(1, N):
    if skill[i] == 1:
        answer_mid.append(answer_top)
        answer_top = str(i+1)

    elif skill[i] == 2:
        answer_mid.append(str(i+1))

    else:
        answer_bot.append(str(i+1))

if answer_mid:
    answer_mid.reverse()
    if answer_bot:
        print(answer_top, ' '.join(answer_mid), ' '.join(answer_bot))
    else:
        print(answer_top, ' '.join(answer_mid))
elif answer_bot:
    print(answer_top, ' '.join(answer_bot))
else:
    print(answer_top)

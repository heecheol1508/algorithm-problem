import sys
sys.stdin = open('input.txt', 'r')


arr = []
flag = False

for i in range(36):
    pos = list(input())
    x = ord(pos[0]) - 65
    y = ord(pos[1]) - 49
    if 0 <= x < 6 and 0 <= y < 6:
        arr.append((x, y))
    else:
        flag = True
        break
if flag or len(set(arr)) != 36:
    print('Invalid')
else:
    for i in range(36):
        dx = abs(arr[i][0] - arr[i - 1][0])
        dy = abs(arr[i][1] - arr[i - 1][1])
        if (dx, dy) == (2, 1) or (dx, dy) == (1, 2):
            continue
        else:
            print('Invalid')
            break
    else:
        print('Valid')

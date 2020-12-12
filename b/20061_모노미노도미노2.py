import sys
sys.stdin = open('input.txt', 'r')


def put_block_on_green(t, y):
    if t == 1:
        for r in range(2, 6):
            if green[r][y] == 1:
                green[r-1][y] = 1
                break
        else:
            green[5][y] = 1

    elif t == 2:
        for r in range(2, 6):
            if green[r][y] == 1 or green[r][y+1] == 1:
                green[r-1][y] = green[r-1][y+1] = 1
                break
        else:
            green[5][y] = green[5][y+1] = 1

    else:
        for r in range(2, 6):
            if green[r][y] == 1:
                green[r-2][y] = green[r-1][y] = 1
                break
        else:
            green[4][y] = green[5][y] = 1


def put_block_on_blue(t, x):
    if t == 1:
        for r in range(2, 6):
            if blue[r][x] == 1:
                blue[r-1][x] = 1
                break
        else:
            blue[5][x] = 1

    elif t == 2:
        for r in range(2, 6):
            if blue[r][x] == 1:
                blue[r-2][x] = blue[r-1][x] = 1
                break
        else:
            blue[4][x] = blue[5][x] = 1

    else:
        for r in range(2, 6):
            if blue[r][x] == 1 or blue[r][x+1] == 1:
                blue[r-1][x] = blue[r-1][x+1] = 1
                break
        else:
            blue[5][x] = blue[5][x+1] = 1


def check_and_erase_the_lines():
    global score

    cnt_green = 0
    for i in range(5, 1, -1):
        if 0 not in green[i]:
            green.pop(i)
            cnt_green += 1

    for _ in range(cnt_green):
        green.insert(0, [0, 0, 0, 0])

    cnt_blue = 0
    for i in range(5, 1, -1):
        if 0 not in blue[i]:
            blue.pop(i)
            cnt_blue += 1

    for _ in range(cnt_blue):
        blue.insert(0, [0, 0, 0, 0])

    score += cnt_green + cnt_blue


def check_and_down_the_lines():
    cnt_green = 0
    cnt_blue = 0
    for r in range(2):
        if 1 in green[r]:
            cnt_green += 1
        if 1 in blue[r]:
            cnt_blue += 1

    for _ in range(cnt_green):
        green.pop()
        green.insert(0, [0, 0, 0, 0])

    for _ in range(cnt_blue):
        blue.pop()
        blue.insert(0, [0, 0, 0, 0])


N = int(input())

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

score = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    put_block_on_green(a, c)
    put_block_on_blue(a, b)

    check_and_erase_the_lines()
    check_and_down_the_lines()

blocks = 0
for row in range(2, 6):
    blocks += sum(green[row]) + sum(blue[row])

print(score)
print(blocks)

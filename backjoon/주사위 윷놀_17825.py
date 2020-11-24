import sys
sys.stdin = open('input.txt', 'r')


nums = list(map(int, input().split()))

move = {
    0: [0, 1, 2, 3, 4, 5],
    1: [1, 2, 3, 4, 5, 6],
    2: [2, 3, 4, 5, 6, 7],
    3: [3, 4, 5, 6, 7, 8],
    4: [4, 5, 6, 7, 8, 9],
    5: [5, 11, 12, 13, 14, 29],
    6: [6, 7, 8, 9, 10, 17],
    7: [7, 8, 9, 10, 17, 18],
    8: [8, 9, 10, 17, 18, 19],
    9: [9, 10, 17, 18, 19, 20],
    10: [15, 16, 14, 29, 30, 31],
    11: [11, 12, 13, 14, 29, 30],
    12: [12, 13, 14, 29, 30, 31],
    13: [13, 14, 29, 30, 31, 32],
    14: [14, 29, 30, 31, 32, 32],
    15: [15, 16, 14, 29, 30, 31],
    16: [16, 14, 29, 30, 31, 32],
    17: [17, 18, 19, 20, 21, 25],
    18: [18, 19, 20, 21, 25, 26],
    19: [19, 20, 21, 25, 26, 27],
    20: [20, 21, 25, 26, 27, 28],
    21: [21, 22, 23, 24, 14, 29],
    22: [22, 23, 24, 14, 29, 30],
    23: [23, 24, 14, 29, 30, 31],
    24: [24, 14, 29, 30, 31, 32],
    25: [25, 26, 27, 28, 31, 32],
    26: [26, 27, 28, 31, 32, 32],
    27: [27, 28, 31, 32, 32, 32],
    28: [28, 31, 32, 32, 32, 32],
    29: [29, 30, 31, 32, 32, 32],
    30: [30, 31, 32, 32, 32, 32],
    31: [31, 32, 32, 32, 32, 32]
}
point = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 13, 16, 19, 25, 22, 24, 22, 24, 26, 28, 30, 28, 27, 26, 32, 34, 36, 38, 30, 35, 40, 0]

queue = [[0, [0, 0, 0, 0]]]
result = 0
for num in nums:
    for _ in range(len(queue)):
        score, horse = queue.pop(0)

        for cur in list(set(horse)):
            if cur == 32:
                continue
            nxt = move[cur][num]
            if nxt == 32:
                temp = horse[:]
                temp.remove(cur)
                queue.append([score, temp])
            elif nxt not in horse:
                temp = horse[:]
                temp.remove(cur)
                temp.append(nxt)
                queue.append([score + point[nxt], temp])

    max_sum = max(s for s, arr in queue)
    if max_sum > result:
        result = max_sum

print(result)

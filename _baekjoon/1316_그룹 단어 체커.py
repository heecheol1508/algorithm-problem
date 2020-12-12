import sys
sys.stdin = open('input.txt', 'r')


answer = 0
for _ in range(int(input())):

    word = list(input())
    word_idx = {}
    flag = True
    for i in range(len(word)):
        character = word[i]
        if character not in word_idx.keys():
            word_idx[character] = i
        elif word_idx[character] == i-1:
            word_idx[character] = i
        else:
            flag = False
            break
    if flag:
        answer += 1

print(answer)

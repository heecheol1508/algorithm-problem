import collections


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    set_str1 = collections.defaultdict(int)
    set_str2 = collections.defaultdict(int)
    elements = set()

    for i in range(len(str1)-1):
        element = str1[i:i+2]
        if element.isalpha():
            elements.add(element)
            set_str1[element] += 1

    for i in range(len(str2) - 1):
        element = str2[i:i + 2]
        if element.isalpha():
            elements.add(element)
            set_str2[element] += 1

    intersection_cnt = 0
    sum_of_sets_cnt = 0

    for element in elements:
        intersection_cnt += min(set_str1[element], set_str2[element])
        sum_of_sets_cnt += max(set_str1[element], set_str2[element])

    if sum_of_sets_cnt == 0:
        answer = 65536
    else:
        answer = int(intersection_cnt / sum_of_sets_cnt * 65536)

    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

def solution(n, number):
    if n == number:
        return 1

    result = [set() for _ in range(9)]
    n_str = str(n)
    for k in range(1, 9):
        result[k].add(int(n_str * k))

    for k in range(2, 9):
        for i in range(1, k // 2 + 1):
            j = k - i
            for i_item in result[i]:
                for j_item in result[j]:
                    result[k].add(i_item * j_item)
                    result[k].add(i_item + j_item)
                    if i_item == j_item:
                        result[k].add(1)
                    elif i_item > j_item:
                        result[k].add(i_item - j_item)
                        result[k].add(i_item // j_item)
                    else:
                        result[k].add(j_item - i_item)
                        result[k].add(j_item // i_item)
        if number in result[k]:
            return k

    return -1


print(solution(2, 11))

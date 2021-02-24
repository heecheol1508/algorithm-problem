import itertools


def solution(numbers):
    n_list = sorted(list(numbers), reverse=True)
    n = int(''.join(n_list))

    is_prime = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if is_prime[i]:
            j = 2
            while i * j < n + 1:
                is_prime[i * j] = False
                j += 1

    n_set = set()
    for k in range(1, len(n_list) + 1):
        for comb in itertools.permutations(n_list, k):
            n_set.add(int(''.join(comb)))

    answer = 0
    for num in n_set:
        if is_prime[num]:
            answer += 1

    return answer


print(solution('71'))

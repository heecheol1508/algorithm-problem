def solution(people, limit):
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    answer = 0

    while i <= j:
        if i == j or people[i] + people[j] <= limit:
            j -= 1
        answer += 1
        i += 1

    return answer


print(solution([70, 50, 80, 50], 100))

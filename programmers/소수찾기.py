def solution(numbers):
    nums = list(numbers)
    nums.sort(reverse=True)

    n = int(''.join(nums))

    minority = [True] * (n+1)
    minority[0] = minority[1] = False

    for i in range(2, n+1):
        if minority[i]:
            k = 2
            while i*k < n+1:
                minority[i*k] = False
                k += 1

    print(minority)
    


    answer = 0
    return answer


print(solution("17"))

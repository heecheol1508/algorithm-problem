import itertools
import re


def solution(expression):

    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in itertools.permutations(op)]
    print(op)

    ex = re.split(r'(\D)', expression)
    print(ex)

    return 0


print(solution("100-200*300-500-20"))

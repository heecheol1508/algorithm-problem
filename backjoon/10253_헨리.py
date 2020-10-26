import sys
sys.stdin = open('input.txt', 'r')
# input = lambda: sys.stdin.readline().rstrip()


def reduction(n1, n2):
    n = gcd(n1, n2)
    return int(n1//n), int(n2//n)


def unit_fraction(n1, n2):
    x = 2
    while True:
        if n1/n2 < 1/x:
            x += 1
        else:
            return x


def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)


N = int(input())
for _ in range(N):
    a, b = map(int, input().split())

    a, b = reduction(a, b)
    if a == 1:
        print(b)
        continue

    while True:
        c = unit_fraction(a, b)
        lcm_bc = lcm(b, c)      # lcm of b and c

        a = a*(lcm_bc/b) - (lcm_bc/c)
        b = lcm_bc

        a, b = reduction(a, b)
        if a == 1:
            print(b)
            break

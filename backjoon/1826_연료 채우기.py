import sys
sys.stdin = open('input.txt', 'r')
import collections


gas_data = collections.defaultdict(int)
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if b > gas_data[a]:
        gas_data[a] = b

town, gas_init = map(int, input().split())

stations = sorted(gas_data.keys())
dict_a = {0: gas_init}

before_s = 0
for s in stations:
    if s >= town:
        break

    dict_b = collections.defaultdict(int)
    diff = s - before_s

    for cnt, gas_left in dict_a.items():
        gas_left -= diff
        if gas_left < 0:
            continue

        if gas_left > dict_b[cnt]:
            dict_b[cnt] = gas_left

        if gas_left + gas_data[s] > dict_b[cnt+1]:
            dict_b[cnt+1] = gas_left + gas_data[s]

    dict_a = {}
    for cnt, gas_left in dict_b.items():
        if gas_left > 0:
            dict_a[cnt] = gas_left
    before_s = s

last_distance = town - before_s
answer = 1000001
for a, b in dict_a.items():
    if a < answer and b - last_distance >= 0:
        answer = a

if answer == 1000001:
    print(-1)
else:
    print(answer)

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())

    stations = [0] * (N+1)
    for m in list(map(int, input().split())):
        stations[m] = 1

    stopped = 0
    station_current = 0
    while True:
        station_next = station_current + K
        if station_next >= N:
            break
        for idx in range(station_next, station_current, -1):
            if stations[idx]:
                station_current = idx
                stopped += 1
                break
        else:
            stopped = 0
            break

    print('#{} {}'.format(t, stopped))


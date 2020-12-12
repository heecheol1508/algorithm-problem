import collections


def solution(bridge_length, weight, truck_weights):

    bridge = collections.deque([0] * bridge_length)

    new = truck_weights.pop(0)
    bridge[0] = new
    bridge_weight = new

    time = 1

    while True:
        if truck_weights:
            if bridge_weight - bridge[-1] + truck_weights[0] <= weight:
                time += 1
                bridge_weight += truck_weights[0] - bridge[-1]
                bridge.rotate(-1)
                bridge[0] = truck_weights.pop(0)
            else:
                for i in range(1, bridge_length+1):
                    if bridge[-i] != 0:
                        bridge.rotate(-i)
                        time += i
                        break
                if bridge_weight - bridge[0] + truck_weights[0] <= weight:
                    bridge_weight += truck_weights[0] - bridge[0]
                    bridge[0] = truck_weights.pop(0)
                else:
                    bridge_weight -= bridge[0]
                    bridge[0] = 0
        else:
            for i in range(bridge_length):
                if bridge[i] != 0:
                    time += bridge_length - i
                    break
            break

    answer = time
    return answer


print(solution(100, 100, [10]))

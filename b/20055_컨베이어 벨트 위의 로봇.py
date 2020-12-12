import sys
sys.stdin = open('input.txt', 'r')
import collections


def robot_moving(robot, belt):
    robot[-1] = 0
    for i in range(N-2, -1, -1):
        if robot[i] == 0:
            continue
        elif robot[i+1] == 0 and belt[i+1] > 0:
            robot[i], robot[i+1] = 0, 1
            belt[i+1] -= 1
    return


N, K = map(int, input().split())
durability_of_belt = collections.deque(list(map(int, input().split())))
robot_position = [0] * N

step = 0
while durability_of_belt.count(0) < K:
    step += 1
    durability_of_belt.rotate(1)
    robot_position = [0] + robot_position[:-1]

    robot_moving(robot_position, durability_of_belt)
    if durability_of_belt[0] > 0:
        robot_position[0] = 1
        durability_of_belt[0] -= 1

print(step)

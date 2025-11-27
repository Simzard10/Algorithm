from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    trucks = deque(truck_weights)
    total_weight = 0

    while bridge or trucks:
        time += 1

        for i in range(len(bridge)):
            bridge[i][1] -= 1

        if bridge and bridge[0][1] == 0:
            total_weight -= bridge.popleft()[0]

        if trucks and total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append([truck, bridge_length])
            total_weight += truck

    return time
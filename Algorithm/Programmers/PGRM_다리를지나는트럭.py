'''
스킬체크 초보자 1번 문제(스택/큐 문제)
다리길이 제한이 10000, 무게제한이 10000 트럭의 수 제한이 10000이라 1초씩 카운트해도 최대 1억이라
1초씩 카운트 하는 방식으로 코딩하였음

1초씩 카운트하면서 무게제한에 걸리지 않으면 트럭을 한 대씩 다리 위로 올림, 다리위에 올라간 시각도 같이 올림
가장 앞선 트럭을 확인하면서 트럭이 올라간 시각과 다리 길이의 합이 현재 시간과 같거나 작아지면
트럭이 다리를 건넜다고 판단하고 다리에서 내림
시간을 출력함
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    t = 0
    current_weight = 0
    truck_weights = truck_weights[::-1]
    on_bridge = deque()
    while truck_weights or on_bridge:
        t += 1
        if on_bridge and on_bridge[0][1] + bridge_length <= t:
            current_weight -= on_bridge.popleft()[0]
        if truck_weights and current_weight + truck_weights[-1] <= weight:
            truck_weight = truck_weights.pop()
            current_weight += truck_weight
            on_bridge.append((truck_weight, t))
    return t
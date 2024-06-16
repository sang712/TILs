"""
w길이에 해당하는 다리를 리스트형으로 만들어 놓고
시간을 하나씩 티킹하면서 다리에 차를 하나씩 놓고 빼는 방식으로 구현
"""
sn, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0
while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(time)